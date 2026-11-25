> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/es/bloquear-apuestas-iphone/

# Cómo bloquear apuestas y casinos en el iPhone

Por [Kyrylo Lozovyi](https://trysilex.com/about/) · 26 de octubre de 2026 · Actualizado 25 de noviembre de 2026

**Respuesta corta:** Tiempo de uso solo no basta. La combinación que aguanta es: un **perfil DNS para todo el dispositivo** (cubre todas las apps y navegadores), **Tiempo de uso con el código en manos de otra persona** (impide reinstalar) y las dos barreras que no se deshacen en un impulso: la **autoprohibición** y el **bloqueo de pagos en el banco**. Todo junto lleva unos 30 minutos.

Hay cinco formas distintas de bloquear el juego en un iPhone y cada una cubre cosas distintas. La mayoría de guías explican solo una, esa tiene un agujero, y por ese agujero se cuela la recaída. Aquí están todas, con sus límites reales.

## Primero: qué cubre cada método

| Método | Qué cubre | ¿Cuánto cuesta deshacerlo? |
|---|---|---|
| Tiempo de uso | Instalación de apps y webs concretas en Safari | Segundos, salvo que otra persona tenga el código |
| Perfil DNS del dispositivo | **Todas las apps y navegadores**, con wifi y datos | Un minuto, en Ajustes |
| Bloqueador de Safari | Solo Safari | Segundos |
| Bloqueo en el banco | Pagos a operadores de juego | Depende del banco; a veces días |
| Autoprohibición | Tus cuentas, en origen | **No se puede** en el momento: meses o años |

Léelo como capas, no como un menú. Las tres primeras hacen el juego incómodo; las dos últimas lo hacen difícil de verdad.

## 1. Tiempo de uso: impide reinstalar

Tiempo de uso es gratis, viene en el iPhone y es más útil por lo que *impide* que por lo que filtra.

**Que no aparezcan apps nuevas.** Borra antes todas las apps de apuestas. Apple cambió los menús en iOS 27 (estos son los nombres en español de España; en Latinoamérica, Tiempo de uso se llama Tiempo en pantalla y alguno más cambia):

- **iOS 27:** Ajustes → Tiempo de uso → **Apps y sitios web** → **Restricciones** → desactiva **Instalar apps**. Si debajo aparecen App Store, Web y Tiendas de apps, ese interruptor pone las tres en **Bloqueado**.
- **iOS 26 y anteriores:** Ajustes → Tiempo de uso → **Restricciones** → actívalas → **Compras en iTunes y App Store** → **Instalar apps** → **No permitir**.
- **iOS 26 en la UE, Brasil o Japón:** también se pueden instalar apps fuera de la App Store, así que cerrarla no basta. El menú se llama **Instalación y compra de apps**: pon también **Tiendas de apps** y **Sitios web** en **No permitir**. [Apple avisa](https://support.apple.com/es-es/118128) de que las dos siguen permitidas tras una actualización aunque ya tuvieras restricciones.

A partir de ahí, reinstalar exige el código de Tiempo de uso.

**Bloquear webs en Safari:**

- **iOS 27:** Tiempo de uso → Apps y sitios web → **Bloqueado** → **+**, y escribe cada casa de apuestas o pega una lista entera. En **Restricciones** → **Filtrado**, elige además **Limitar el acceso a webs para adultos**: según iOS, también bloquea los proxies web. Con un código de Tiempo de uso puesto, iOS restringe además la navegación privada.
- **iOS 26 y anteriores:** Restricciones → **App Store, contenido, internet y juegos** → **Contenido web** → **Limitar webs para adultos**, y en **No permitir nunca**, **Añadir sitio web** para cada casa de apuestas. Además desactiva la navegación privada de Safari.

Comprobamos los menús de iOS 27 en iOS 27.1, en el simulador de Apple, el 25 de noviembre de 2026. La [ayuda de Apple](https://support.apple.com/es-es/105121) solo describe el bloqueo de instalaciones y webs en el dispositivo de un menor (Ajustes → Familia → nombre del menor), así que algún nombre puede cambiar en el tuyo.

**El detalle que nadie cuenta:** iOS no tiene una categoría de juego. «Limitar webs para adultos» es un filtro de contenido adulto: pilla alguna web de apuestas por casualidad y se deja la mayoría.

**Hazlo bien:** pon un código de Tiempo de uso que tú no sepas (iOS 27: Tiempo de uso → **Gestionar el tiempo de uso** → **Bloquear ajustes de tiempo de uso**). Que lo escriba tu pareja, un amigo o un familiar y que lo guarde. En **Recuperación del código de tiempo de uso** no pongas tu propia cuenta de Apple: la cuenta que se indique ahí puede restablecer el código. Y no lo tomes por un muro: las páginas de Apple no coinciden sobre cómo se cambia en iOS 27 ([una](https://support.apple.com/es-es/102677) pide Face ID o el código del teléfono; [la otra](https://support.apple.com/es-es/guide/iphone/iph272b4c4bd/ios), el código actual de Tiempo de uso).

## 2. Un perfil DNS: el que lo cubre todo

Es el método que casi todas las guías se saltan, y el más fuerte de los que viven en el propio teléfono. Toda app y navegador necesita resolver un nombre de dominio antes de conectarse; si la resolución falla, la web de apuestas no carga. Sin extensiones, sin configurar cada navegador, y con datos móviles también.

El iPhone permite que una app o un perfil de configuración instale un DNS cifrado para todo el dispositivo. Si lo apuntas a un servicio que filtra el juego, dejan de cargar todas las casas de apuestas, casinos y tragaperras online. Opciones: los resolvedores públicos de Mullvad (uno «family» gratuito que filtra juego), NextDNS (con lista de juego activable) o una app que lo instale por ti, como [Silex](https://trysilex.com/es/como-dejar-de-apostar/).

Compruébalo: en Ajustes → General → VPN, DNS y gestión de dispositivos debe aparecer tu configuración de DNS seleccionada, y una web de apuestas no debería cargar.

**Su límite:** se puede desactivar en Ajustes en menos de un minuto. Es un badén, no un muro; un badén muy bueno, porque la mayoría de recaídas son impulsivas y un minuto de fricción a menudo basta.

## 3. Bloqueadores de Safari

Una extensión de bloqueo de contenido puede impedir que Safari cargue una lista de dominios. Se activa en Ajustes → Apps → Safari → Extensiones. Útil y limitado: solo cubre Safari. Chrome, el navegador dentro de las redes sociales o la propia app de la casa de apuestas quedan fuera.

## 4 y 5. Lo que no está en el teléfono

Las dos barreras más fuertes no viven en el iPhone: **que tu banco rechace los pagos de juego** y **autoprohibirte** con los operadores (en España, a través del RGIAJ). No se deshacen en los noventa segundos en que importa. [Cómo hacer ambas →](https://trysilex.com/es/como-dejar-de-apostar/)

## Lo que no funciona

- **Solo borrar las apps.** Reinstalar lleva quince segundos y la web móvil funciona igual.
- **Solo bloquear en el router.** Se acaba en la puerta de casa; con datos móviles no hay bloqueo.
- **Una VPN normal.** Cambia por dónde sale tu tráfico, no lo filtra.
- **Cualquier cosa que prometa ser imposible de quitar en iOS.** El sistema no lo permite.

## Bloquear es el suelo, no el plan

Cada capa te da tiempo en los noventa segundos en que el impulso está en su punto más alto. Lo que haces con ese tiempo decide si funciona. [Los impulsos suben y bajan de forma bastante predecible](https://trysilex.com/es/cuanto-duran-las-ganas-de-apostar/), y aprender a esperar uno es una habilidad que mejora con la práctica.

## Deja de apostar. Quédate con el dinero.

Silex bloquea el juego en todo tu teléfono y te acompaña durante 90 días, uno a uno.

[Descargar Silex para iPhone](https://apps.apple.com/app/id6798826038?mt=8) [Descargar Silex para Android](https://play.google.com/store/apps/details?id=com.klozovyi.stopgamble&referrer=utm_source%3Dtrysilex%26utm_campaign%3Des_iphone)

## Preguntas frecuentes

### ¿Se pueden bloquear las apps de apuestas sin instalar nada?

Sí. Tiempo de uso puede impedir instalar apps y bloquear webs concretas, y el iPhone admite una configuración de DNS que hace que los dominios de juego no carguen en ninguna app. Lo que el iPhone no hace solo es mantener una lista de cientos de miles de dominios de juego: eso lo aporta un bloqueador o un DNS con filtro.

### ¿Tiempo de uso bloquea las apps de apuestas?

En parte. Puede impedir instalaciones nuevas y bloquear webs en Safari, pero no tiene una categoría de juego: «Limitar webs para adultos» no es un filtro de apuestas. Tienes que añadir los dominios a mano o usar un DNS que mantenga la lista por ti.

### ¿Funciona con datos móviles además de con wifi?

Un perfil DNS instalado en el iPhone sí, porque pertenece al dispositivo. Un bloqueo en el router de casa no: en cuanto el móvil pasa a 4G o 5G, deja de aplicarse. Es el motivo más habitual por el que falla el bloqueo en casa.

### ¿Algún bloqueador es imposible de quitar en iPhone?

No, y quien diga lo contrario exagera. En iOS siempre puedes quitar un perfil o borrar una app. Lo permanente tiene que venir de fuera del teléfono: la autoprohibición con los operadores y el bloqueo en el banco.

## Si necesitas hablar con alguien ahora

- España: [024](tel:024) — Línea de atención a la conducta suicida — gratuita, confidencial, 24 h
- México: [800 911 2000](tel:8009112000) — Línea de la Vida — salud mental y adicciones, gratuita, 24 h
- Online: [gamblingtherapy.org](https://www.gamblingtherapy.org) — Gambling Therapy — apoyo gratuito por chat, en español
- Otros países: [findahelpline.com](https://findahelpline.com) — Líneas de crisis de tu país
