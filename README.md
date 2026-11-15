# nythera-games

Sitio web estático de Nythera Games (GitHub Pages, dominio www.nythera.games).

- `/` inicio · `/cinemiau/` y `/cinemiau/en/` página y soporte · `/cinemiau/privacidad/` y `/cinemiau/privacy/` política de privacidad.
- URLs para las tiendas: soporte `https://www.nythera.games/cinemiau/`, privacidad `https://www.nythera.games/cinemiau/privacidad/`.

## Diseño

Sistema «Noche» v1, derivado del logotipo: tokens y componentes en `style.css` (mismos nombres que el sistema de diseño publicado en claude.ai, «Nythera Games»).
- Fuentes OFL alojadas en `assets/fonts/` (Marcellus, Figtree, Josefin Sans) con sus licencias; la web no llama a Google Fonts.
- Logos en `assets/img/` recortados del original `lumen/assets/brand/nythera.png` (fondo negro; se usan con la clase `.marca`).
- Las páginas de un juego ponen `data-product="cinemiau"` en `<body>` para usar sus acentos.
