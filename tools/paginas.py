"""Genera portada y Cinemiau en ES/EN/PT y aplica cabecera, selector de idioma y pie a las páginas legales y 404. Uso: python3 tools/paginas.py"""
import re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
LANGS = ['es', 'en', 'pt']
ROUTES = {
    'home': {'es': '/', 'en': '/en/', 'pt': '/pt/'},
    'cinemiau': {'es': '/cinemiau/', 'en': '/cinemiau/en/', 'pt': '/cinemiau/pt/'},
    'privacy': {'es': '/cinemiau/privacidad/', 'en': '/cinemiau/privacy/', 'pt': '/cinemiau/privacidade/'},
    'terms': {'es': '/cinemiau/condiciones/', 'en': '/cinemiau/terms/', 'pt': '/cinemiau/termos/'},
}
UI = {
    'es': dict(home='Inicio', privacy='Privacidad', terms='Condiciones', brand='Nythera Games, inicio', nav='Principal', langnav='Idioma'),
    'en': dict(home='Home', privacy='Privacy', terms='Terms', brand='Nythera Games, home', nav='Main', langnav='Language'),
    'pt': dict(home='Início', privacy='Privacidade', terms='Termos', brand='Nythera Games, início', nav='Principal', langnav='Idioma'),
}
LANGNAME = {'es': 'Español', 'en': 'English', 'pt': 'Português'}


def head(lang, title, desc, page, extra=''):
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="https://www.nythera.games{ROUTES[page][l]}">\n' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="https://www.nythera.games{ROUTES[page]["es"]}">\n'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#0B0812">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/Marcellus.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/Figtree.woff2" as="font" type="font/woff2" crossorigin>
{extra}{alts}<link rel="stylesheet" href="/style.css?v=3">
</head>
'''


def header(lang, page):
    u = UI[lang]
    def nav_link(key, label):
        cur = ' aria-current="page"' if key == page else ''
        return f'<a href="{ROUTES[key][lang]}"{cur}>{label}</a>'
    nav = nav_link('home', u['home']) + nav_link('cinemiau', 'Cinemiau') + nav_link('privacy', u['privacy'])
    CUR = ' aria-current="true"'
    langs = ''.join(
        f'<a href="{ROUTES[page][l]}" hreflang="{l}" lang="{l}" title="{LANGNAME[l]}"{CUR if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS)
    return (f'<header class="site-header"><div class="wrap"><a class="brand" href="{ROUTES["home"][lang]}" aria-label="{u["brand"]}">'
            '<img class="marca" src="/assets/img/nythera-emblem.png" alt="" width="46" height="44">'
            '<img class="marca brand-word" src="/assets/img/nythera-wordmark.png" alt="" width="132" height="30"></a>'
            f'<div class="header-end"><nav class="site-nav" aria-label="{u["nav"]}">{nav}</nav>'
            f'<nav class="lang" aria-label="{u["langnav"]}">{langs}</nav></div></div></header>')


def footer(lang):
    u = UI[lang]
    return ('<footer class="site-footer"><div class="wrap"><img class="marca" src="/assets/img/nythera-wordmark.png" alt="Nythera Games" width="150" height="34" loading="lazy">'
            f'<p>© 2026 Nythera Games · <a href="{ROUTES["privacy"][lang]}">{u["privacy"]}</a> · <a href="{ROUTES["terms"][lang]}">{u["terms"]}</a> · '
            '<a href="mailto:contacto@nythera.games">contacto@nythera.games</a></p></div></footer>')


POSTERS = [  # slug, es, en, pt
    ('el-gato-padrino', 'El Gato Padrino', 'The Catfather', 'O Gato Poderoso Chefão'),
    ('catanic', 'Catánic', 'Catanic', 'Gatanic'),
    ('el-mago-de-miauz', 'El Mago de Miauz', 'The Wizard of Paws', 'O Mágico de Miauz'),
    ('2001-odisea-del-gato', '2001: Odisea del Gato', '2001: A Space Catyssey', '2001: Uma Odisseia no Gatoespaço'),
    ('desayuno-con-sardinas', 'Desayuno con Sardinas', "Breakfast at Sardine's", 'Bonequinha de Sardinha'),
    ('el-resplandor-miau', 'El Resplandor Miau', 'The Shining Meow', 'O Iluminado Miau'),
]
def poster_src(lang, slug):
    return f'/assets/img/posters/{"" if lang == "es" else lang + "/"}{slug}.jpg'

T = {
 'es': dict(
  home_title='Nythera Games · Juegos independientes',
  home_desc='Nythera Games: estudio independiente de juegos móviles. Cinemiau: puzle de gatos y cine.',
  eyebrow='Estudio independiente', h1='Juegos pequeños para noches tranquilas',
  lead='Hacemos juegos móviles con cariño: fáciles de empezar, sin cuentas y sin letra pequeña.',
  cta1='Conocer Cinemiau', cta2='Escríbenos',
  nyx_alt='Ilustración: Nyx, diosa de la noche, juega con su móvil en su cama bajo una luna creciente',
  games_eyebrow='Nuestros juegos', games_h2='El primer estreno',
  game_name='Cinemiau: Puzzle de Gatos', soon='Próximamente',
  game_text='Ordena piedras de colores, completa el pixel art y descubre el póster de una película… ¡protagonizada por gatos!',
  game_cta='Ver Cinemiau',
  contact_eyebrow='Contacto', contact_h2='¿Una duda, una idea o un problema?',
  contact_lead='Si es sobre un juego, cuéntanos tu dispositivo y la versión de la app.',
  c_title='Cinemiau: Puzzle de Gatos · Nythera Games',
  c_desc='Cinemiau es un puzle relajado de ordenar colores y pixel art con pósters de cine protagonizados por gatos. Gratis, sin cuentas y sin conexión.',
  c_lead='Ordena piedras de colores, completa el pixel art y gira la carta para descubrir el póster de una película… ¡protagonizada por gatos!',
  how_eyebrow='Cómo se juega', how_h2='Un estreno por cada puzle',
  feats=[('Ordena colores', 'Un juego de ordenar piedras fácil de aprender y difícil de soltar.'),
         ('Completa el pixel art', 'Tableros grandes de pixel art, con pista automática opcional.'),
         ('Llena tu cartelera', 'Cada nivel terminado gira la carta y suma un estreno a tu cartelera.'),
         ('Juega a tu manera', 'Gratis y sin cuentas, y funciona sin conexión. Los anuncios empiezan en el nivel 9 y se quitan con una compra única.')],
  wall_eyebrow='En cartelera', wall_h2='Algunos estrenos que vas a descubrir', poster_alt='Póster de {}',
  sup_eyebrow='Soporte', sup_h2='¿Tienes una duda o encontraste un problema?',
  sup_p='Escríbenos a <a href="mailto:contacto@nythera.games">contacto@nythera.games</a> e indica tu dispositivo y la versión de la app.',
  priv_h2='Privacidad',
  priv_p='Cinemiau es gratis con anuncios de Google AdMob, que puedes quitar con una compra única. Lee la <a href="{privacy}">política de privacidad</a> y las <a href="{terms}">condiciones del servicio</a>.',
  disclaimer='Cinemiau es un juego independiente. Todas las ilustraciones son parodias originales con gatos; no están afiliadas ni respaldadas por ningún estudio, productor ni marca.'),
 'en': dict(
  home_title='Nythera Games · Independent games',
  home_desc='Nythera Games: an independent mobile game studio. Cinemiau: a cat and movie puzzle.',
  eyebrow='Independent studio', h1='Small games for quiet nights',
  lead='We make mobile games with care: easy to start, no accounts and no fine print.',
  cta1='Meet Cinemiau', cta2='Write to us',
  nyx_alt='Illustration: Nyx, goddess of the night, plays on her phone in bed under a crescent moon',
  games_eyebrow='Our games', games_h2='The first premiere',
  game_name='Cinemiau: Cat Puzzle', soon='Coming soon',
  game_text='Sort colored stones, finish the pixel art and reveal a movie poster starring… cats!',
  game_cta='See Cinemiau',
  contact_eyebrow='Contact', contact_h2='A question, an idea or a problem?',
  contact_lead='If it is about a game, tell us your device and the app version.',
  c_title='Cinemiau: Cat Puzzle · Nythera Games',
  c_desc='Cinemiau is a relaxing color sort and pixel art puzzle with movie posters starring cats. Free, no accounts, works offline.',
  c_lead='Sort colored stones, finish the pixel art and flip the card to reveal a movie poster starring… cats!',
  how_eyebrow='How it plays', how_h2='One premiere for every puzzle',
  feats=[('Sort colors', 'A stone sorting puzzle that is easy to learn and hard to put down.'),
         ('Finish the pixel art', 'Big pixel art boards with an optional automatic hint.'),
         ('Fill your poster wall', 'Every finished level flips the card and adds a premiere to your wall.'),
         ('Play your way', 'Free, no accounts, and it works offline. Ads start at level 9 and a one-time purchase removes them.')],
  wall_eyebrow='Now showing', wall_h2='A few premieres you will discover', poster_alt='Poster for {}',
  sup_eyebrow='Support', sup_h2='Questions or found a problem?',
  sup_p='Email <a href="mailto:contacto@nythera.games">contacto@nythera.games</a> and tell us your device and the app version.',
  priv_h2='Privacy',
  priv_p='Cinemiau is free with Google AdMob ads, which you can remove with a one-time purchase. Read the <a href="{privacy}">privacy policy</a> and the <a href="{terms}">terms of service</a>.',
  disclaimer='Cinemiau is an independent game. All artwork is original cat-themed parody and is not affiliated with or endorsed by any studio, producer or brand.'),
 'pt': dict(
  home_title='Nythera Games · Jogos independentes',
  home_desc='Nythera Games: estúdio independente de jogos para celular. Cinemiau: quebra-cabeça de gatos e cinema.',
  eyebrow='Estúdio independente', h1='Jogos pequenos para noites tranquilas',
  lead='Fazemos jogos para celular com carinho: fáceis de começar, sem contas e sem letras miúdas.',
  cta1='Conhecer o Cinemiau', cta2='Fale conosco',
  nyx_alt='Ilustração: Nyx, deusa da noite, joga no celular na cama sob uma lua crescente',
  games_eyebrow='Nossos jogos', games_h2='A primeira estreia',
  game_name='Cinemiau: Puzzle de Gatos', soon='Em breve',
  game_text='Ordene pedras coloridas, complete o pixel art e descubra o pôster de um filme… estrelado por gatos!',
  game_cta='Ver o Cinemiau',
  contact_eyebrow='Contato', contact_h2='Uma dúvida, uma ideia ou um problema?',
  contact_lead='Se for sobre um jogo, conte qual é o seu dispositivo e a versão do app.',
  c_title='Cinemiau: Puzzle de Gatos · Nythera Games',
  c_desc='Cinemiau é um quebra-cabeça relaxante de ordenar cores e pixel art com pôsteres de cinema estrelados por gatos. Grátis, sem contas e offline.',
  c_lead='Ordene pedras coloridas, complete o pixel art e vire a carta para descobrir o pôster de um filme… estrelado por gatos!',
  how_eyebrow='Como se joga', how_h2='Uma estreia a cada quebra-cabeça',
  feats=[('Ordene cores', 'Um jogo de ordenar pedras fácil de aprender e difícil de largar.'),
         ('Complete o pixel art', 'Tabuleiros grandes de pixel art, com dica automática opcional.'),
         ('Encha o seu mural', 'Cada fase concluída vira a carta e soma uma estreia ao seu mural de pôsteres.'),
         ('Jogue do seu jeito', 'Grátis, sem contas e funciona offline. Os anúncios começam no nível 9 e são removidos com uma compra única.')],
  wall_eyebrow='Em cartaz', wall_h2='Algumas estreias que você vai descobrir', poster_alt='Pôster de {}',
  sup_eyebrow='Suporte', sup_h2='Tem uma dúvida ou encontrou um problema?',
  sup_p='Escreva para <a href="mailto:contacto@nythera.games">contacto@nythera.games</a> e informe o seu dispositivo e a versão do app.',
  priv_h2='Privacidade',
  priv_p='O Cinemiau é grátis com anúncios do Google AdMob, que você pode remover com uma compra única. Leia a <a href="{privacy}">política de privacidade</a> e os <a href="{terms}">termos de serviço</a>.',
  disclaimer='O Cinemiau é um jogo independente. Todas as ilustrações são paródias originais com gatos; não são afiliadas nem endossadas por nenhum estúdio, produtor ou marca.'),
}


def chips(t, soon):
    return f'<ul class="chips"><li class="chip chip--estado">{soon}</li><li class="chip">iPhone</li><li class="chip">Android</li></ul>'


def home(lang):
    t = T[lang]; idx = {'es': 0, 'en': 1, 'pt': 2}[lang]
    fan = ''.join(f'<img class="poster" src="{poster_src(lang, s)}" alt="" width="400" height="600" loading="lazy">\n'
                  for s, *_ in [POSTERS[0], POSTERS[1], POSTERS[2]])
    return head(lang, t['home_title'], t['home_desc'], 'home',
                '<link rel="preload" as="image" href="/assets/img/nyx-hero.jpg" media="(min-width:821px)">\n') + f'''<body>
{header(lang, 'home')}
<main>
<section class="hero hero--nyx">
<picture><source media="(max-width:820px)" srcset="/assets/img/nyx-hero-movil.jpg"><img class="hero-bg" src="/assets/img/nyx-hero.jpg" alt="{t['nyx_alt']}" width="1536" height="1024"></picture>
<div class="wrap">
<div class="hero-text">
<p class="eyebrow">{t['eyebrow']}</p>
<h1 class="display">{t['h1']}</h1>
<p class="lead">{t['lead']}</p>
<div class="actions"><a class="btn btn--primary" href="{ROUTES['cinemiau'][lang]}">{t['cta1']}</a><a class="btn btn--ghost" href="#contacto">{t['cta2']}</a></div>
</div>
</div>
</section>

<section class="section" aria-labelledby="juegos">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">{t['games_eyebrow']}</p>
<h2 id="juegos">{t['games_h2']}</h2>
</div>
<article class="game" data-product="cinemiau">
<div class="game-text">
<img class="game-logo" src="/assets/img/cinemiau-logo.png" alt="" width="634" height="340" loading="lazy">
<h3>{t['game_name']}</h3>
{chips(t, t['soon'])}
<p>{t['game_text']}</p>
<div class="actions"><a class="btn btn--primary" href="{ROUTES['cinemiau'][lang]}">{t['game_cta']}</a></div>
</div>
<div class="posters" aria-hidden="true">
{fan}</div>
</article>
</div>
</section>

<section class="section" id="contacto" aria-labelledby="contacto-h">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">{t['contact_eyebrow']}</p>
<h2 id="contacto-h">{t['contact_h2']}</h2>
<p class="lead">{t['contact_lead']}</p>
<p class="correo"><a href="mailto:contacto@nythera.games">contacto@nythera.games</a></p>
</div>
</div>
</section>
</main>
{footer(lang)}
</body>
</html>
'''


def cinemiau(lang):
    t = T[lang]; idx = {'es': 1, 'en': 2, 'pt': 3}[lang]
    hero_fan = ''.join(f'<img class="poster" src="{poster_src(lang, POSTERS[i][0])}" alt="" width="400" height="600">\n' for i in (3, 1, 5))
    feats = ''.join(f'<li><h3>{a}</h3><p>{b}</p></li>\n' for a, b in t['feats'])
    wall = ''.join(
        f'<li><figure><img class="poster" src="{poster_src(lang, p[0])}" alt="{t["poster_alt"].format(p[idx])}" width="400" height="600" loading="lazy"><figcaption>{p[idx]}</figcaption></figure></li>\n'
        for p in POSTERS)
    priv = t['priv_p'].format(privacy=ROUTES['privacy'][lang], terms=ROUTES['terms'][lang])
    return head(lang, t['c_title'], t['c_desc'], 'cinemiau') + f'''<body data-product="cinemiau">
{header(lang, 'cinemiau')}
<main>
<section class="hero">
<div class="cielo" aria-hidden="true"></div>
<div class="wrap">
<div class="hero-text">
<img src="/assets/img/cinemiau-logo.png" alt="" width="634" height="340" style="width:min(100%,340px);margin:0 0 var(--s-4) -10px">
<h1>{t['game_name']}</h1>
<p class="lead">{t['c_lead']}</p>
{chips(t, t['soon'])}
</div>
<div class="hero-art posters" aria-hidden="true">
{hero_fan}</div>
</div>
</section>

<section class="section" aria-labelledby="como">
<div class="wrap">
<div class="section-head"><p class="eyebrow">{t['how_eyebrow']}</p><h2 id="como">{t['how_h2']}</h2></div>
<ul class="rasgos">
{feats}</ul>
</div>
</section>

<section class="section" aria-labelledby="cartelera">
<div class="wrap">
<div class="section-head"><p class="eyebrow">{t['wall_eyebrow']}</p><h2 id="cartelera">{t['wall_h2']}</h2></div>
<ul class="cartelera">
{wall}</ul>
</div>
</section>

<section class="section" aria-labelledby="soporte">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">{t['sup_eyebrow']}</p>
<h2 id="soporte">{t['sup_h2']}</h2>
<p>{t['sup_p']}</p>
<h2>{t['priv_h2']}</h2>
<p>{priv}</p>
<p class="muted">{t['disclaimer']}</p>
</div>
</div>
</section>
</main>
{footer(lang)}
</body>
</html>
'''


def write(route, text):
    p = ROOT / route.strip('/') / 'index.html' if route != '/' else ROOT / 'index.html'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    print('wrote', p.relative_to(ROOT))


for l in LANGS:
    write(ROUTES['home'][l], home(l))
    write(ROUTES['cinemiau'][l], cinemiau(l))

# Páginas legales y 404: cambia cabecera, pie, hreflang y versión de la hoja
for page in ('privacy', 'terms'):
    for l in LANGS:
        p = ROOT / ROUTES[page][l].strip('/') / 'index.html'
        s = p.read_text()
        s, n = re.subn(r'<header class="site-header">.*?</header>', lambda m: header(l, page), s, flags=re.S); assert n == 1, p
        s, n = re.subn(r'<footer class="site-footer">.*?</footer>', lambda m: footer(l), s, flags=re.S); assert n == 1, p
        s = re.sub(r'<link rel="alternate" hreflang[^>]*>\n', '', s)
        alts = ''.join(f'<link rel="alternate" hreflang="{x}" href="https://www.nythera.games{ROUTES[page][x]}">\n' for x in LANGS)
        s = re.sub(r'<link rel="stylesheet" href="/style.css\?v=\d+">', lambda m: alts + '<link rel="stylesheet" href="/style.css?v=3">', s)
        p.write_text(s); print('updated', p.relative_to(ROOT))

p = ROOT / '404.html'; s = p.read_text()
s, n = re.subn(r'<header class="site-header">.*?</header>', lambda m: header('es', 'home').replace(' aria-current="page"', ''), s, flags=re.S); assert n == 1
s, n = re.subn(r'<footer class="site-footer">.*?</footer>', lambda m: footer('es'), s, flags=re.S); assert n == 1
s = s.replace('/style.css?v=2', '/style.css?v=3')
s = s.replace('<p>Esta página no existe. <a href="/">Volver al inicio</a>.</p>',
              '<p>Esta página no existe. <a href="/">Volver al inicio</a>.</p><p lang="en">This page does not exist. <a href="/en/">Go to the home page</a>.</p><p lang="pt">Esta página não existe. <a href="/pt/">Voltar ao início</a>.</p>')
p.write_text(s); print('updated 404.html')
