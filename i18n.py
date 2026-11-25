"""Per-language strings and crisis resources for trysilex.com.

English is the source language; every other locale lives in src/pages/<folder>/
and carries an "en" key in its meta naming the English page it translates, which
is how build.py groups pages for hreflang.

CRISIS RESOURCES ARE SAFETY-CRITICAL. Every number below was verified against an
official or institutional source on 2026-10-26 (see the comment on each); Nordic lines on 2026-11-25. Re-verify
before every publish, the same rule as App/Services/RegionResources.swift. Anything
that could not be confirmed is deliberately absent.
"""

MONTHS = {
    "en": ("January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"),
    "es": ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
           "agosto", "septiembre", "octubre", "noviembre", "diciembre"),
    "pt-br": ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
              "agosto", "setembro", "outubro", "novembro", "dezembro"),
    "de": ("Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
           "August", "September", "Oktober", "November", "Dezember"),
    "fr": ("janvier", "février", "mars", "avril", "mai", "juin", "juillet",
           "août", "septembre", "octobre", "novembre", "décembre"),
    "sv": ("januari", "februari", "mars", "april", "maj", "juni", "juli",
           "augusti", "september", "oktober", "november", "december"),
    "no": ("januar", "februar", "mars", "april", "mai", "juni", "juli",
           "august", "september", "oktober", "november", "desember"),
    "da": ("januar", "februar", "marts", "april", "maj", "juni", "juli",
           "august", "september", "oktober", "november", "december"),
    "fi": ("tammikuuta", "helmikuuta", "maaliskuuta", "huhtikuuta", "toukokuuta",
           "kesäkuuta", "heinäkuuta", "elokuuta", "syyskuuta", "lokakuuta",
           "marraskuuta", "joulukuuta"),
    "ru": ("января", "февраля", "марта", "апреля", "мая", "июня", "июля",
           "августа", "сентября", "октября", "ноября", "декабря"),
}


# --- prices ------------------------------------------------------------------
# App Store prices, read live from App Store Connect (asc subscriptions pricing
# summary) on PRICES_CHECKED: country -> (currency, weekly, annual). The annual plan has
# a 7-day free trial, the weekly plan none. Google Play prices differ a little (SE 37/369,
# NO 35/355, FI 3.39/33.99, GB 2.69/26.99), so pages say the store shows the exact price.
# This is the only place Silex's prices live: pages use {{price_week}}, {{price_year}} and
# {{price_table}}.
PRICES_CHECKED = "2026-11-25"
PRICES = {
    "US": ("USD", "2.99", "29.99"),
    "GB": ("GBP", "2.99", "29.99"),
    "SE": ("SEK", "39", "399"),
    "NO": ("NOK", "39", "399"),
    "DK": ("DKK", "29", "249"),
    "FI": ("EUR", "2.99", "34.99"),
}
COUNTRIES = {
    "en": {"US": "United States", "GB": "United Kingdom", "SE": "Sweden", "NO": "Norway",
           "DK": "Denmark", "FI": "Finland"},
    "sv": {"US": "USA", "GB": "Storbritannien", "SE": "Sverige", "NO": "Norge",
           "DK": "Danmark", "FI": "Finland"},
    "no": {"US": "USA", "GB": "Storbritannia", "SE": "Sverige", "NO": "Norge",
           "DK": "Danmark", "FI": "Finland"},
    "da": {"US": "USA", "GB": "Storbritannien", "SE": "Sverige", "NO": "Norge",
           "DK": "Danmark", "FI": "Finland"},
    "fi": {"US": "Yhdysvallat", "GB": "Iso-Britannia", "SE": "Ruotsi", "NO": "Norja",
           "DK": "Tanska", "FI": "Suomi"},
}
# Offer names for the schema on translated homepages that have their own market.
SCHEMA_OFFERS = {
    "sv": ("Veckovis", "\u00c5rsvis, 7 dagars gratis provperiod"),
    "no": ("Ukentlig", "\u00c5rlig, 7 dagers gratis pr\u00f8veperiode"),
    "da": ("Ugentligt", "\u00c5rligt, 7 dages gratis pr\u00f8veperiode"),
    "fi": ("Viikkotilaus", "Vuositilaus, 7 p\u00e4iv\u00e4n ilmainen kokeilu"),
}
NBSP = "\u00a0"


def country_name(country: str, loc: str) -> str:
    return COUNTRIES.get(loc, COUNTRIES["en"])[country]


def price(country: str, plan: str, loc: str) -> str:
    """One price the way this language writes it."""
    currency, week, year = PRICES[country]
    amount = week if plan == "week" else year
    if loc == "en":
        return {"USD": f"${amount}", "GBP": f"\u00a3{amount}", "EUR": f"\u20ac{amount}"}.get(
            currency, f"{amount}{NBSP}{currency}")
    amount = amount.replace(".", ",")
    home_currency = {"sv": "SEK", "no": "NOK", "da": "DKK"}.get(loc)
    if currency == home_currency:
        return f"{amount}{NBSP}kr." if loc == "da" else f"{amount}{NBSP}kr"
    sign = {"USD": "USD", "GBP": "\u00a3", "EUR": "\u20ac"}.get(currency, currency)
    if loc == "fi" and currency == "EUR":
        return f"{amount}{NBSP}\u20ac"
    return f"{amount}{NBSP}{sign}"


def pretty_date(iso: str, loc: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    if loc == "zh":
        return f"{y}年{m}月{d}日"
    name = MONTHS[loc][m - 1]
    if loc == "en":
        return f"{name} {d}, {y}"
    if loc in ("de", "no", "da", "fi"):
        return f"{d}. {name} {y}"
    if loc in ("es", "pt-br"):
        return f"{d} de {name} de {y}"
    return f"{d} {name} {y}"            # fr, ru, sv


# folder -> settings. "hreflang" is what goes in <link rel=alternate>,
# "html" is the <html lang> value.
LOCALES = {
    "en": dict(
        html="en", hreflang="en", og="en_US", label="English",
        skip="Skip to content", short="Short answer:", faq="Common questions",
        by="By", updated="Updated", home="Home",
        help_title="If you need someone right now",
        disclaimer="Silex helps you build healthier habits around gambling. It is not "
                   "medical care and doesn't diagnose or treat any condition. If you are "
                   "in crisis, use the numbers above.",
        cta_h="Quit gambling. Keep the money.",
        cta_p="Silex blocks gambling across your phone and walks you through 90 days, one at a time.",
        cta_btn="Get Silex on iPhone",
        cta_btn_android="Get Silex on Android",
        price_head=("Country", "Weekly", "Annual", "App Store prices, checked"),
        nav=[("/how-to-stop-gambling/", "How to stop"),
             ("/best-gambling-blocker-apps/", "Blockers"),
             ("/gambling-self-check/", "Self-check"),
             ("/about/", "About")],
        footer=[("/", "Home"), ("/about/", "About"), ("/methodology/", "Methodology"),
                ("/docs/", "Docs"), ("/support/", "Support"), ("/privacy/", "Privacy"),
                ("/terms/", "Terms")],
        built_by="Built by", in_city="in Kyiv, Ukraine",
        also_by="Also by the developer", vr_desc="men's pelvic floor training",
        helplines=[
            ("US", "1-800-MY-RESET", "tel:18006973738",
             "National Problem Gambling Helpline — free, confidential, 24/7"),
            ("US", "988", "tel:988",
             "Suicide &amp; Crisis Lifeline — call or text if it feels like too much"),
            ("UK", "0808 8020 133", "tel:08088020133",
             "National Gambling Helpline (GamCare) — free, confidential, 24/7"),
            ("UK", "116 123", "tel:116123", "Samaritans"),
            ("Elsewhere", "findahelpline.com", "https://findahelpline.com",
             "Crisis lines for your country"),
        ],
    ),

    "es": dict(
        html="es", hreflang="es", og="es_ES", label="Español",
        skip="Saltar al contenido", short="Respuesta corta:", faq="Preguntas frecuentes",
        by="Por", updated="Actualizado", home="Inicio",
        help_title="Si necesitas hablar con alguien ahora",
        disclaimer="Silex te ayuda a construir hábitos más sanos frente al juego. No es "
                   "atención médica y no diagnostica ni trata ninguna enfermedad. Si estás "
                   "en crisis, usa los números de arriba.",
        cta_h="Deja de apostar. Quédate con el dinero.",
        cta_p="Silex bloquea el juego en todo tu teléfono y te acompaña durante 90 días, uno a uno.",
        cta_btn="Descargar Silex para iPhone",
        cta_btn_android="Descargar Silex para Android",
        nav=[("/es/como-dejar-de-apostar/", "Cómo dejarlo"),
             ("/es/test-ludopatia/", "Test"),
             ("/es/bloquear-apuestas-iphone/", "Bloquear en iPhone")],
        footer=[("/es/", "Inicio"), ("/about/", "Sobre Silex (EN)"),
                ("/methodology/", "Metodología (EN)"), ("/privacy/", "Privacidad (EN)")],
        built_by="Hecho por", in_city="en Kiev, Ucrania",
        also_by="Otra app del desarrollador", vr_desc="entrenamiento del suelo pélvico masculino",
        helplines=[
            # sanidad.gob.es/linea024 — Ministerio de Sanidad, 24/7, free
            ("España", "024", "tel:024",
             "Línea de atención a la conducta suicida — gratuita, confidencial, 24 h"),
            # Secretaría de Salud / CONASAMA — 24 h, 365 days, free
            ("México", "800 911 2000", "tel:8009112000",
             "Línea de la Vida — salud mental y adicciones, gratuita, 24 h"),
            ("Online", "gamblingtherapy.org", "https://www.gamblingtherapy.org",
             "Gambling Therapy — apoyo gratuito por chat, en español"),
            ("Otros países", "findahelpline.com", "https://findahelpline.com",
             "Líneas de crisis de tu país"),
        ],
    ),

    "pt-br": dict(
        html="pt-BR", hreflang="pt-BR", og="pt_BR", label="Português",
        skip="Pular para o conteúdo", short="Resposta curta:", faq="Perguntas frequentes",
        by="Por", updated="Atualizado em", home="Início",
        help_title="Se você precisa falar com alguém agora",
        disclaimer="O Silex ajuda você a criar hábitos mais saudáveis em relação às apostas. "
                   "Não é atendimento médico e não diagnostica nem trata nenhuma doença. Se "
                   "você está em crise, use os números acima.",
        cta_h="Pare de apostar. Fique com o dinheiro.",
        cta_p="O Silex bloqueia apostas no celular inteiro e acompanha você por 90 dias, um de cada vez.",
        cta_btn="Baixar o Silex para iPhone",
        cta_btn_android="Baixar o Silex para Android",
        nav=[("/pt-br/como-parar-de-apostar/", "Como parar"),
             ("/pt-br/teste-vicio-em-apostas/", "Teste"),
             ("/pt-br/bloquear-apostas-iphone/", "Bloquear no iPhone")],
        footer=[("/pt-br/como-parar-de-apostar/", "Início"), ("/about/", "Sobre o Silex (EN)"),
                ("/methodology/", "Metodologia (EN)"), ("/privacy/", "Privacidade (EN)")],
        built_by="Feito por", in_city="em Kiev, Ucrânia",
        also_by="Outro app do desenvolvedor", vr_desc="treino do assoalho pélvico masculino",
        helplines=[
            # cvv.org.br — 188, free, 24 h, every day, nationwide
            ("Brasil", "188", "tel:188",
             "CVV — apoio emocional e prevenção do suicídio, gratuito, 24 h"),
            ("Online", "gamblingtherapy.org", "https://www.gamblingtherapy.org",
             "Gambling Therapy — apoio gratuito por chat, em português"),
            ("Outros países", "findahelpline.com", "https://findahelpline.com",
             "Linhas de apoio do seu país"),
        ],
    ),

    "de": dict(
        html="de", hreflang="de", og="de_DE", label="Deutsch",
        skip="Zum Inhalt springen", short="Kurz gesagt:", faq="Häufige Fragen",
        by="Von", updated="Aktualisiert am", home="Start",
        help_title="Wenn du jetzt mit jemandem sprechen willst",
        disclaimer="Silex hilft dir, gesündere Gewohnheiten rund ums Glücksspiel aufzubauen. "
                   "Es ist keine medizinische Behandlung und stellt keine Diagnosen. Wenn du "
                   "in einer Krise bist, nutze die Nummern oben.",
        cta_h="Mit dem Glücksspiel aufhören. Das Geld behalten.",
        cta_p="Silex sperrt Glücksspiel auf deinem ganzen Handy und begleitet dich 90 Tage lang, Tag für Tag.",
        cta_btn="Silex fürs iPhone laden",
        cta_btn_android="Silex für Android laden",
        nav=[("/de/mit-dem-gluecksspiel-aufhoeren/", "Aufhören"),
             ("/de/spielsucht-test/", "Selbsttest"),
             ("/de/gluecksspiel-sperren-iphone/", "iPhone sperren")],
        footer=[("/de/mit-dem-gluecksspiel-aufhoeren/", "Start"), ("/about/", "Über Silex (EN)"),
                ("/methodology/", "Methodik (EN)"), ("/privacy/", "Datenschutz (EN)")],
        built_by="Entwickelt von", in_city="in Kyjiw, Ukraine",
        also_by="Auch vom Entwickler", vr_desc="Beckenbodentraining für Männer",
        helplines=[
            # bioeg.de/service/infotelefone/gluecksspielsucht — free; Mo–Do 10–22, Fr–So 10–18
            ("Deutschland", "0800 1 37 27 00", "tel:08001372700",
             "BIÖG-Telefonberatung zur Glücksspielsucht — kostenlos, Mo–Do 10–22, Fr–So 10–18 Uhr"),
            # TelefonSeelsorge — free, 24/7
            ("Deutschland", "0800 111 0 111", "tel:08001110111",
             "TelefonSeelsorge — kostenlos, anonym, rund um die Uhr"),
            ("Online", "gamblingtherapy.org", "https://www.gamblingtherapy.org",
             "Gambling Therapy — kostenlose Chat-Hilfe, auch auf Deutsch"),
            ("Andere Länder", "findahelpline.com", "https://findahelpline.com",
             "Krisentelefone in deinem Land"),
        ],
    ),

    "fr": dict(
        html="fr", hreflang="fr", og="fr_FR", label="Français",
        skip="Aller au contenu", short="En bref :", faq="Questions fréquentes",
        by="Par", updated="Mis à jour le", home="Accueil",
        help_title="Si vous avez besoin de parler à quelqu'un maintenant",
        disclaimer="Silex vous aide à construire des habitudes plus saines face aux jeux "
                   "d'argent. Ce n'est pas un soin médical et il ne pose aucun diagnostic. Si "
                   "vous êtes en crise, utilisez les numéros ci-dessus.",
        cta_h="Arrêter de jouer. Garder l'argent.",
        cta_p="Silex bloque les jeux d'argent sur tout votre téléphone et vous accompagne pendant 90 jours, un à la fois.",
        cta_btn="Télécharger Silex pour iPhone",
        cta_btn_android="Télécharger Silex pour Android",
        nav=[("/fr/arreter-de-jouer-aux-jeux-d-argent/", "Arrêter"),
             ("/fr/test-addiction-jeux-argent/", "Test"),
             ("/fr/bloquer-sites-paris-iphone/", "Bloquer sur iPhone")],
        footer=[("/fr/arreter-de-jouer-aux-jeux-d-argent/", "Accueil"), ("/about/", "À propos (EN)"),
                ("/methodology/", "Méthodologie (EN)"), ("/privacy/", "Confidentialité (EN)")],
        built_by="Conçu par", in_city="à Kyiv, Ukraine",
        also_by="Aussi du développeur", vr_desc="rééducation du périnée masculin",
        helplines=[
            # joueurs-info-service.fr — Santé publique France, 8h–2h, 7j/7, no surcharge
            ("France", "09 74 75 13 13", "tel:0974751313",
             "Joueurs Info Service — anonyme, non surtaxé, de 8 h à 2 h, 7 j/7"),
            # info.gouv.fr — national suicide prevention line, free, 24/7
            ("France", "3114", "tel:3114",
             "Numéro national de prévention du suicide — gratuit, 24 h/24"),
            ("En ligne", "gamblingtherapy.org", "https://www.gamblingtherapy.org",
             "Gambling Therapy — soutien gratuit par chat, en français"),
            ("Autres pays", "findahelpline.com", "https://findahelpline.com",
             "Lignes d'écoute de votre pays"),
        ],
    ),

    "ru": dict(
        html="ru", hreflang="ru", og="ru_RU", label="Русский",
        skip="Перейти к содержанию", short="Коротко:", faq="Частые вопросы",
        by="Автор:", updated="Обновлено", home="Главная",
        help_title="Если вам нужно поговорить с кем-то прямо сейчас",
        disclaimer="Silex помогает выстроить более здоровые привычки в отношении азартных игр. "
                   "Это не медицинская помощь: приложение не ставит диагнозов и не лечит. "
                   "Если вы в кризисе, воспользуйтесь контактами выше.",
        cta_h="Бросить играть. Сохранить деньги.",
        cta_p="Silex блокирует азартные игры на всём телефоне и ведёт вас 90 дней, шаг за шагом.",
        cta_btn="Скачать Silex для iPhone",
        cta_btn_android="Скачать Silex для Android",
        nav=[("/ru/kak-brosit-igrat/", "Как бросить"),
             ("/ru/test-na-igrovuyu-zavisimost/", "Тест"),
             ("/ru/zablokirovat-kazino-iphone/", "Блокировка на iPhone")],
        footer=[("/ru/kak-brosit-igrat/", "Главная"), ("/about/", "О Silex (EN)"),
                ("/methodology/", "Методология (EN)"), ("/privacy/", "Конфиденциальность (EN)")],
        built_by="Разработчик —", in_city="Киев, Украина",
        also_by="Ещё от разработчика", vr_desc="тренировка мышц тазового дна для мужчин",
        helplines=[
            # gamblingtherapy.org — text support, native Russian among its languages
            ("Онлайн", "gamblingtherapy.org", "https://www.gamblingtherapy.org",
             "Gambling Therapy — бесплатная поддержка в чате, на русском"),
            ("Экстренно", "112", "tel:112",
             "Единый номер экстренных служб — Россия, Украина, Казахстан, ЕС"),
            ("Другие страны", "findahelpline.com", "https://findahelpline.com",
             "Телефоны доверия вашей страны"),
        ],
    ),

    "zh": dict(
        html="zh-Hans", hreflang="zh-Hans", og="zh_CN", label="中文",
        skip="跳到正文", short="简短回答：", faq="常见问题",
        by="作者：", updated="更新于", home="首页",
        help_title="如果你现在需要找人倾诉",
        disclaimer="Silex 帮助你建立更健康的赌博相关习惯。它不是医疗服务，不做诊断，也不提供治疗。"
                   "如果你正处于危机中，请拨打上方的电话。",
        cta_h="戒掉赌博，把钱留住。",
        cta_p="Silex 在整部手机上屏蔽赌博，并陪你走过 90 天，一天一天来。",
        cta_btn="下载 iPhone 版 Silex",
        cta_btn_android="下载 Android 版 Silex",
        nav=[("/zh/ru-he-jie-du/", "如何戒赌"),
             ("/zh/du-bo-cheng-yin-ce-shi/", "自测"),
             ("/zh/iphone-ping-bi-du-bo/", "iPhone 屏蔽")],
        footer=[("/zh/ru-he-jie-du/", "首页"), ("/about/", "关于 Silex (EN)"),
                ("/methodology/", "方法论 (EN)"), ("/privacy/", "隐私 (EN)")],
        built_by="开发者", in_city="乌克兰基辅",
        also_by="同一开发者的另一款应用", vr_desc="男性盆底肌训练",
        helplines=[
            # donotgamble.org.hk / hkjc.com — Ping Wo Fund hotline
            ("香港", "1834 633", "tel:1834633",
             "平和基金 戒赌热线"),
            # mohw.gov.tw — 1925 安心專線, free, 24 h
            ("台湾", "1925", "tel:1925",
             "卫福部安心专线 — 免费，24 小时"),
            # MSF (ask.gov.sg) — daily 8am–11pm
            ("新加坡", "1800-6-668-668", "tel:18006668668",
             "全国问题赌博援助热线 — 每天 8:00–23:00"),
            ("其他地区", "findahelpline.com", "https://findahelpline.com",
             "你所在地区的危机热线"),
        ],
    ),
    "sv": dict(
        html="sv", hreflang="sv", og="sv_SE", label="Svenska",
        skip="Hoppa till innehållet", short="Kort svar:", faq="Vanliga frågor",
        by="Av", updated="Uppdaterad", home="Hem", reviewed_by="Granskad av",
        help_title="Om du behöver prata med någon nu",
        disclaimer="Silex hjälper dig att bygga sundare vanor kring spel om pengar. Det är inte "
                   "vård, ställer inga diagnoser och behandlar inga tillstånd. Är du i kris, "
                   "ring numren ovan.",
        cta_h="Sluta spela. Behåll pengarna.",
        cta_p="Silex blockerar spel om pengar i hela telefonen och följer dig genom 90 dagar, en i taget.",
        cta_btn="Hämta Silex till iPhone",
        cta_btn_android="Hämta Silex till Android",
        price_country="SE",
        price_head=("Land", "Per vecka", "Per år", "App Store-priser, kontrollerade"),
        ext=["Lägg till i Chrome", "Lägg till i Edge"],
        docs_h="Silex dokumentation", about="/sv/om-silex/",
        aria_main="Huvudmeny", aria_footer="Sidfot", aria_lang="Språk",
        nav=[("/sv/sluta-spela/", "Så slutar du"),
             ("/sv/basta-apparna-blockera-spel/", "Blockerare"),
             ("/sv/test-spelberoende/", "Självtest"),
             ("/sv/om-silex/", "Om Silex")],
        footer=[("/sv/", "Hem"), ("/sv/om-silex/", "Om Silex"), ("/sv/metod/", "Metod"),
                ("/sv/docs/", "Dokumentation"), ("/sv/support/", "Support"),
                ("/sv/integritet/", "Integritet"), ("/sv/villkor/", "Villkor")],
        built_by="Byggt av", in_city="i Kyiv, Ukraina",
        also_by="Från samma utvecklare", vr_desc="bäckenbottenträning för män",
        helplines=[
            # stodlinjen.se/om-oss/oppettider, read 2026-11-25: Mon 9-19, Tue-Wed 9-17, Thu 11-19, Fri 9-15
            ("Sverige", "020-81 91 00", "tel:020819100",
             "Stödlinjen, spel om pengar: gratis och anonymt, vardagar (mån 9–19, tis–ons 9–17, tors 11–19, fre 9–15)"),
            # foreningenspelfriheten.se/for-spelare: peer charity, not clinicians, 24/7
            ("Sverige", "08-37 43 00", "tel:08374300",
             "Föreningen Spelfriheten, kamratstöd för spelare och anhöriga, dygnet runt"),
            # mind.se (archived copy 31 Oct 2026), 1177.se/stodlinjer
            ("Sverige", "90101", "tel:90101",
             "Självmordslinjen (Mind), dygnet runt, anonymt"),
            # hjalplinjen.se
            ("Sverige", "90390", "tel:90390",
             "Hjälplinjen, dygnet runt, gratis och anonymt"),
            ("Nödläge", "112", "tel:112", "Vid direkt livsfara"),
            ("Andra länder", "findahelpline.com", "https://findahelpline.com",
             "Krislinjer där du är"),
        ],
    ),

    "no": dict(
        html="nb", hreflang="no", og="nb_NO", label="Norsk",
        skip="Hopp til innholdet", short="Kort svar:", faq="Vanlige spørsmål",
        by="Av", updated="Oppdatert", home="Hjem", reviewed_by="Gjennomgått av",
        help_title="Hvis du trenger å snakke med noen nå",
        disclaimer="Silex hjelper deg med å bygge sunnere vaner rundt pengespill. Det er ikke "
                   "helsehjelp, stiller ingen diagnoser og behandler ingen tilstander. Er du i "
                   "krise, bruk numrene over.",
        cta_h="Slutt å spille. Behold pengene.",
        cta_p="Silex blokkerer pengespill på hele telefonen og følger deg gjennom 90 dager, én om gangen.",
        cta_btn="Last ned Silex til iPhone",
        cta_btn_android="Last ned Silex til Android",
        price_country="NO",
        price_head=("Land", "Per uke", "Per år", "App Store-priser, sjekket"),
        ext=["Legg til i Chrome", "Legg til i Edge"],
        docs_h="Silex-dokumentasjon", about="/no/om-silex/",
        aria_main="Hovedmeny", aria_footer="Bunntekst", aria_lang="Språk",
        nav=[("/no/slutte-a-spille/", "Slik slutter du"),
             ("/no/beste-apper-blokkere-pengespill/", "Blokkering"),
             ("/no/test-spilleavhengighet/", "Selvtest"),
             ("/no/om-silex/", "Om")],
        footer=[("/no/", "Hjem"), ("/no/om-silex/", "Om Silex"), ("/no/metode/", "Metode"),
                ("/no/docs/", "Dokumentasjon"), ("/no/support/", "Brukerstøtte"),
                ("/no/personvern/", "Personvern"), ("/no/vilkar/", "Vilkår")],
        built_by="Laget av", in_city="i Kyiv, Ukraina",
        also_by="Fra samme utvikler", vr_desc="bekkenbunnstrening for menn",
        helplines=[
            # hjelpelinjen.no, read 2026-11-25: weekdays 09-18; free and anonymous per blakors.no
            ("Norge", "800 800 40", "tel:80080040",
             "Hjelpelinjen for pengespill: gratis og anonym, hverdager 09–18"),
            # mentalhelse.no/fa-hjelp/hjelpetelefonen
            ("Norge", "116 123", "tel:116123",
             "Mental Helse: gratis og døgnåpen, for alle som trenger noen å snakke med"),
            ("Nødsituasjon", "113", "tel:113", "Fare for liv og helse"),
            ("Andre land", "findahelpline.com", "https://findahelpline.com",
             "Krisetelefoner der du er"),
        ],
    ),

    "da": dict(
        html="da", hreflang="da", og="da_DK", label="Dansk",
        skip="Gå til indhold", short="Kort svar:", faq="Ofte stillede spørgsmål",
        by="Af", updated="Opdateret", home="Hjem", reviewed_by="Gennemgået af",
        help_title="Hvis du har brug for at tale med nogen nu",
        disclaimer="Silex hjælper dig med at opbygge sundere vaner omkring pengespil. Det er ikke "
                   "sundhedsbehandling, stiller ingen diagnoser og behandler ingen tilstande. Er "
                   "du i krise, så brug numrene ovenfor.",
        cta_h="Stop med at spille. Behold pengene.",
        cta_p="Silex blokerer pengespil på hele din telefon og følger dig gennem 90 dage, én ad gangen.",
        cta_btn="Hent Silex til iPhone",
        cta_btn_android="Hent Silex til Android",
        price_country="DK",
        price_head=("Land", "Pr. uge", "Pr. år", "App Store-priser, tjekket"),
        ext=["Føj til Chrome", "Føj til Edge"],
        docs_h="Silex-dokumentation", about="/da/om-silex/",
        aria_main="Hovedmenu", aria_footer="Sidefod", aria_lang="Sprog",
        nav=[("/da/stop-med-at-spille/", "Sådan stopper du"),
             ("/da/bedste-apps-blokere-pengespil/", "Blokering"),
             ("/da/test-ludomani/", "Selvtest"),
             ("/da/om-silex/", "Om")],
        footer=[("/da/", "Hjem"), ("/da/om-silex/", "Om Silex"), ("/da/metode/", "Metode"),
                ("/da/docs/", "Dokumentation"), ("/da/support/", "Support"),
                ("/da/privatliv/", "Privatliv"), ("/da/vilkar/", "Vilkår")],
        built_by="Udviklet af", in_city="i Kyiv, Ukraine",
        also_by="Fra samme udvikler", vr_desc="bækkenbundstræning for mænd",
        helplines=[
            # stopspillet.dk, read 2026-11-25: phone Mon-Thu 9-21, Fri 9-17; confidential, closed at weekends
            ("Danmark", "70 22 28 25", "tel:70222825",
             "StopSpillet: gratis og fortroligt, man–tor 9–21, fre 9–17 (lukket i weekenden)"),
            # livslinien.dk: every day 09-05, ordinary phone rate
            ("Danmark", "70 201 201", "tel:70201201",
             "Livslinien: hver dag kl. 9–5, anonymt, almindelig telefontakst"),
            ("Nødsituation", "112", "tel:112", "Akut livsfare"),
            ("Andre lande", "findahelpline.com", "https://findahelpline.com",
             "Krisetelefoner, hvor du er"),
        ],
    ),

    "fi": dict(
        html="fi", hreflang="fi", og="fi_FI", label="Suomi",
        skip="Siirry sisältöön", short="Lyhyesti:", faq="Usein kysyttyä",
        by="Kirjoittanut", updated="Päivitetty", home="Etusivu", reviewed_by="Tarkistanut",
        help_title="Jos tarvitset jonkun juuri nyt",
        disclaimer="Silex auttaa rakentamaan terveempiä tapoja rahapelaamisen suhteen. Se ei ole "
                   "terveydenhoitoa, ei diagnosoi eikä hoida mitään sairautta. Jos olet kriisissä, "
                   "käytä yllä olevia numeroita.",
        cta_h="Lopeta rahapelaaminen. Pidä rahasi.",
        cta_p="Silex estää rahapelit koko puhelimessa ja kulkee kanssasi 90 päivää, yhden kerrallaan.",
        cta_btn="Lataa Silex iPhoneen",
        cta_btn_android="Lataa Silex Androidiin",
        price_country="FI",
        price_head=("Maa", "Viikko", "Vuosi", "App Store -hinnat, tarkistettu"),
        ext=["Lisää Chromeen", "Lisää Edgeen"],
        docs_h="Silexin ohjeet", about="/fi/tietoa-silexista/",
        aria_main="Päävalikko", aria_footer="Alatunniste", aria_lang="Kieli",
        nav=[("/fi/lopeta-rahapelaaminen/", "Näin lopetat"),
             ("/fi/parhaat-rahapelien-estosovellukset/", "Estot"),
             ("/fi/peliriippuvuustesti/", "Testi"),
             ("/fi/tietoa-silexista/", "Tietoa")],
        footer=[("/fi/", "Etusivu"), ("/fi/tietoa-silexista/", "Tietoa Silexistä"),
                ("/fi/menetelma/", "Menetelmä"), ("/fi/docs/", "Ohjeet"), ("/fi/tuki/", "Tuki"),
                ("/fi/tietosuoja/", "Tietosuoja"), ("/fi/kayttoehdot/", "Käyttöehdot")],
        built_by="Tekijä", in_city="Kiova, Ukraina",
        also_by="Samalta tekijältä", vr_desc="lantionpohjan harjoittelua miehille",
        helplines=[
            # peluuri.fi, read 2026-11-25: weekdays 12-18, free
            ("Suomi", "0800 100 101", "tel:0800100101",
             "Peluuri, rahapelaaminen: ilmainen ja nimetön, arkisin klo 12–18"),
            # mieli.fi/tukea-ja-apua/kriisipuhelin: 24/7, not free of charge
            ("Suomi", "09 2525 0111", "tel:0925250111",
             "MIELI Kriisipuhelin, ympäri vuorokauden (oman operaattorin hinta)"),
            ("Hätätilanne", "112", "tel:112", "Välitön hengenvaara"),
            ("Muut maat", "findahelpline.com", "https://findahelpline.com",
             "Kriisilinjat siellä missä olet"),
        ],
    ),
}
