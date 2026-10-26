"""Per-language strings and crisis resources for trysilex.com.

English is the source language; every other locale lives in src/pages/<folder>/
and carries an "en" key in its meta naming the English page it translates, which
is how build.py groups pages for hreflang.

CRISIS RESOURCES ARE SAFETY-CRITICAL. Every number below was verified against an
official or institutional source on 2026-10-26 (see the comment on each). Re-verify
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
    "ru": ("января", "февраля", "марта", "апреля", "мая", "июня", "июля",
           "августа", "сентября", "октября", "ноября", "декабря"),
}


def pretty_date(iso: str, loc: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    if loc == "zh":
        return f"{y}年{m}月{d}日"
    name = MONTHS[loc][m - 1]
    if loc == "en":
        return f"{name} {d}, {y}"
    if loc == "de":
        return f"{d}. {name} {y}"
    if loc in ("es", "pt-br"):
        return f"{d} de {name} de {y}"
    return f"{d} {name} {y}"            # fr, ru


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
        cta_h="Quit for good. Keep the money.",
        cta_p="Silex blocks gambling across your iPhone and walks you through 90 days, one at a time.",
        cta_btn="Get Silex on iPhone",
        nav=[("/how-to-stop-gambling/", "How to stop"),
             ("/best-gambling-blocker-apps/", "Blockers"),
             ("/gambling-self-check/", "Self-check"),
             ("/about/", "About")],
        footer=[("/", "Home"), ("/about/", "About"), ("/methodology/", "Methodology"),
                ("/support/", "Support"), ("/privacy/", "Privacy")],
        built_by="Built by", in_city="in Kyiv, Ukraine",
        also_by="Also by the developer", vr_desc="men's pelvic floor training",
        helplines=[
            ("US", "1-800-GAMBLER", "tel:18004262537",
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
        cta_h="Déjalo para siempre. Quédate con el dinero.",
        cta_p="Silex bloquea el juego en todo tu iPhone y te acompaña durante 90 días, uno a uno.",
        cta_btn="Descargar Silex para iPhone",
        nav=[("/es/como-dejar-de-apostar/", "Cómo dejarlo"),
             ("/es/test-ludopatia/", "Test"),
             ("/es/bloquear-apuestas-iphone/", "Bloquear en iPhone")],
        footer=[("/es/como-dejar-de-apostar/", "Inicio"), ("/about/", "Sobre Silex (EN)"),
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
        cta_h="Pare de vez. Fique com o dinheiro.",
        cta_p="O Silex bloqueia apostas no iPhone inteiro e acompanha você por 90 dias, um de cada vez.",
        cta_btn="Baixar o Silex para iPhone",
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
        cta_h="Endgültig aufhören. Das Geld behalten.",
        cta_p="Silex sperrt Glücksspiel auf deinem ganzen iPhone und begleitet dich 90 Tage lang, Tag für Tag.",
        cta_btn="Silex fürs iPhone laden",
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
        cta_h="Arrêter pour de bon. Garder l'argent.",
        cta_p="Silex bloque les jeux d'argent sur tout votre iPhone et vous accompagne pendant 90 jours, un à la fois.",
        cta_btn="Télécharger Silex pour iPhone",
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
        cta_h="Бросить навсегда. Сохранить деньги.",
        cta_p="Silex блокирует азартные игры на всём iPhone и ведёт вас 90 дней, шаг за шагом.",
        cta_btn="Скачать Silex для iPhone",
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
        cta_h="彻底戒掉，把钱留住。",
        cta_p="Silex 在整部 iPhone 上屏蔽赌博，并陪你走过 90 天，一天一天来。",
        cta_btn="下载 iPhone 版 Silex",
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
}
