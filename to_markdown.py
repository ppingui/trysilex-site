"""Rendered page HTML -> Markdown, for the index.md copy of every page.

Converts the page's <main> plus the helplines block, so the Markdown carries the same
text as the HTML (agents score that parity). Links become absolute, scripts and form
controls drop out, tables stay tables. Standard library only, like build.py.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser
from urllib.parse import urljoin

VOID = {"br", "img", "input", "hr", "meta", "link", "source", "wbr"}
SKIP = {"script", "style", "template", "button", "select", "svg"}
BLOCK = {"p", "div", "section", "article", "aside", "form", "fieldset", "figure",
         "ul", "ol", "table", "h1", "h2", "h3", "h4", "blockquote", "noscript", "main"}


class Node:
    def __init__(self, tag: str, attrs: dict, parent: "Node | None"):
        self.tag, self.attrs, self.parent, self.children = tag, attrs, parent, []


class _Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.cur = Node("root", {}, None)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, dict(attrs), self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def _classes(n: Node) -> set[str]:
    return set((n.attrs.get("class") or "").split())


def _inline(n, base: str) -> str:
    """Inline text of a node, with emphasis, code and links."""
    if isinstance(n, str):
        return re.sub(r"\s+", " ", n)
    if n.tag in SKIP:
        return ""
    if n.tag == "br":
        return "  \n"
    if n.tag == "img":
        alt = n.attrs.get("alt", "")
        return f"![{alt}]({urljoin(base, n.attrs.get('src', ''))})" if alt else ""
    inner = "".join(_inline(c, base) for c in n.children)
    cls = _classes(n)
    if "hl-region" in cls:
        return f"{inner.strip()}: "
    if "hl-note" in cls:
        return f" — {inner.strip()}"
    if n.tag in ("strong", "b") and inner.strip():
        return f"**{inner.strip()}**"
    if n.tag in ("em", "i") and inner.strip():
        return f"*{inner.strip()}*"
    if n.tag == "code":
        return f"`{inner}`"
    if n.tag == "a" and n.attrs.get("href"):
        href = n.attrs["href"]
        if href.startswith("#"):
            return inner
        return f"[{inner.strip()}]({urljoin(base, href)})"
    return inner


def _clean(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s)
    return re.sub(r" *\n *", "\n", s).strip()


def _table(n: Node, base: str) -> str:
    rows = []
    def walk(x):
        for c in x.children:
            if isinstance(c, Node):
                if c.tag == "tr":
                    cells = [_clean(_inline(td, base)).replace("|", "\\|").replace("\n", " ")
                             for td in c.children if isinstance(td, Node) and td.tag in ("td", "th")]
                    rows.append(cells)
                else:
                    walk(c)
    walk(n)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def _blocks(n: Node, base: str, out: list[str], depth: int = 0) -> None:
    """Append Markdown blocks for n's children to out."""
    buf: list[str] = []

    def flush():
        text = _clean("".join(buf))
        if text:
            out.append(text)
        buf.clear()

    for c in n.children:
        if isinstance(c, str) or (c.tag not in BLOCK and c.tag not in ("li", "legend", "label")):
            buf.append(_inline(c, base))
            continue
        flush()
        if c.tag in SKIP:
            continue
        if c.tag in ("h1", "h2", "h3", "h4"):
            out.append("#" * int(c.tag[1]) + " " + _clean(_inline(c, base)))
        elif c.tag == "table":
            out.append(_table(c, base))
        elif c.tag in ("ul", "ol"):
            items, i = [], 0
            for li in c.children:
                if isinstance(li, Node) and li.tag == "li":
                    i += 1
                    sub: list[str] = []
                    _blocks(li, base, sub, depth + 1)
                    marker = f"{i}." if c.tag == "ol" else "-"
                    pad = " " * (len(marker) + 1)
                    body = "\n\n".join(sub).replace("\n", "\n" + pad)
                    items.append(f"{marker} {body}")
            out.append("\n".join(items))
        elif c.tag == "blockquote":
            sub = []
            _blocks(c, base, sub, depth)
            out.append("\n".join("> " + line if line else ">" for line in "\n\n".join(sub).split("\n")))
        elif c.tag == "legend":
            out.append(f"**{_clean(_inline(c, base))}**")
        else:
            _blocks(c, base, out, depth)
    flush()


def page_markdown(page_html: str, url: str, header: str) -> str:
    """Markdown for one rendered page: header, then <main>, then the helplines."""
    main = re.search(r"<main\b.*?</main>", page_html, re.S)
    helplines = re.search(r'<aside class="helplines".*?</aside>', page_html, re.S)
    tree = _Tree()
    tree.feed((main.group(0) if main else "") + (helplines.group(0) if helplines else ""))
    out: list[str] = []
    _blocks(tree.root, url, out)
    # Drop placeholder fragments a script fills in later ("0", "—").
    body = "\n\n".join(b for b in out if not re.fullmatch(r"[\W\d_]{0,3}", b.strip()))
    return header + "\n\n" + re.sub(r"\n{3,}", "\n\n", body) + "\n"
