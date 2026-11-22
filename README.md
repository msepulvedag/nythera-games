# nythera-games

Sitio web estático de Nythera Games (GitHub Pages, dominio www.nythera.games).

- Tres idiomas con selector ES/EN/PT en la cabecera: `/`, `/en/`, `/pt/` inicio · `/nosotros/`, `/en/about/`, `/pt/sobre/` acerca de · `/cinemiau/`, `/cinemiau/en/`, `/cinemiau/pt/` página y soporte · `/cinemiau/privacidad|privacy|privacidade/` privacidad · `/cinemiau/condiciones|terms|termos/` condiciones.
- Textos de portada, Cinemiau, Luciérnagas, Acerca de, menú y pie en `tools/paginas.py`; tras editarlos, ejecutar `python3 tools/paginas.py`.
- URLs para las tiendas: soporte `https://www.nythera.games/cinemiau/`, privacidad `https://www.nythera.games/cinemiau/privacidad/`.

| Luciérnagas | ES | EN | PT |
| --- | --- | --- | --- |
| Página y soporte | `/luciernagas/` | `/luciernagas/en/` | `/luciernagas/pt/` |
| Privacidad | `/luciernagas/privacidad/` | `/luciernagas/privacy/` | `/luciernagas/privacidade/` |
| Condiciones | `/luciernagas/condiciones/` | `/luciernagas/terms/` | `/luciernagas/termos/` |

- URLs de Luciérnagas para las tiendas: soporte `https://www.nythera.games/luciernagas/`, privacidad `https://www.nythera.games/luciernagas/privacidad/` y condiciones `https://www.nythera.games/luciernagas/condiciones/`.

## Diseño

Sistema «Noche» v1, derivado del logotipo: tokens y componentes en `style.css` (mismos nombres que el sistema de diseño publicado en claude.ai, «Nythera Games»).
- Fuentes OFL alojadas en `assets/fonts/` (Marcellus, Figtree, Josefin Sans) con sus licencias; la web no llama a Google Fonts.
- Logos en `assets/img/` recortados del original `lumen/assets/brand/nythera.png` (fondo negro; se usan con la clase `.marca`).
- Las páginas de un juego ponen `data-product` con el slug del juego en `<body>` para usar sus acentos.
- Ilustración del héroe (Nyx) generada con OpenAI a partir del logo; originales y prompt en `Juegos/_referencias/nythera-hero/`.
