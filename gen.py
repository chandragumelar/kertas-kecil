#!/usr/bin/env python3
# Kertas Kecil - generator worksheet printable usia 3 tahun
# Output: worksheet.html (A4, 210x297mm)

import re, os, random
from pathlib import Path

SVG_DIR = Path(__file__).parent / "svg"
random.seed(7)

# ---------------------------------------------------------------- assets
FILES = {
    "avocado": "abacate-avocado-avocados-svgrepo-com.svg",
    "pineapple": "abacaxi-fruit-pineapple-svgrepo-com.svg",
    "airplane": "airplane-svgrepo-com.svg",
    "butterfly": "animal-bug-butterfly-svgrepo-com.svg",
    "bunny": "animal-bunny-cartoon-svgrepo-com.svg",
    "dog2": "animal-cachorro-dog-svgrepo-com.svg",
    "deer": "animal-cartoon-deer-svgrepo-com.svg",
    "cat2": "animal-cat-domestic-svgrepo-com.svg",
    "duck": "animal-duck-ducks-svgrepo-com.svg",
    "elephant2": "animal-elefante-elephant-svgrepo-com.svg",
    "apple": "apple-apples-fruit-svgrepo-com.svg",
    "apple2": "apple-svgrepo-com.svg",
    "boy": "avatar-boy-svgrepo-com.svg",
    "girl": "avatar-girl-svgrepo-com (2).svg",
    "bike": "bike-svgrepo-com.svg",
    "bird": "bird-svgrepo-com (2).svg",
    "cactus": "cactus-2-svgrepo-com.svg",
    "camel": "camel-animal-svgrepo-com.svg",
    "carrot": "carrot-svgrepo-com.svg",
    "cat": "cat-svgrepo-com.svg",
    "corn": "corn-svgrepo-com.svg",
    "crocodile": "crocodile-svgrepo-com (1).svg",
    "crying": "crying-face-svgrepo-com.svg",
    "dog": "dog-svgrepo-com.svg",
    "dolphin": "dolphin-svgrepo-com.svg",
    "donut": "donut-1-svgrepo-com.svg",
    "egg": "egg-1-svgrepo-com.svg",
    "guitar": "electric-guitar-svgrepo-com.svg",
    "elephant": "elephant-svgrepo-com.svg",
    "happy": "emotion-happy-svgrepo-com.svg",
    "unhappy": "emotion-unhappy-svgrepo-com.svg",
    "fish": "fish-animal-svgrepo-com.svg",
    "fish2": "fish-fishing-seafood-animal-meal-svgrepo-com.svg",
    "flamingo": "flamingo-svgrepo-com.svg",
    "flower": "flower-svgrepo-com.svg",
    "frog": "frog-svgrepo-com.svg",
    "grape": "fruit-fruits-grape-svgrepo-com.svg",
    "strawberry": "fruit-fruits-strawberry-svgrepo-com.svg",
    "watermelon": "fruit-melancia-watermelon-svgrepo-com.svg",
    "giraffe": "giraffe-svgrepo-com.svg",
    "grinning": "grinning-face-with-smiling-eyes-svgrepo-com.svg",
    "burger": "hamburger-svgrepo-com.svg",
    "helicopter": "helicopter-svgrepo-com.svg",
    "icecream": "ice-cream-svgrepo-com.svg",
    "kangaroo": "kangaroo-svgrepo-com.svg",
    "ladybug": "ladybug-animal-svgrepo-com.svg",
    "owl": "owl-svgrepo-com.svg",
    "pelican": "pelican-animal-svgrepo-com.svg",
    "sailboat": "sailboat-svgrepo-com.svg",
    "shark": "shark-animal-svgrepo-com.svg",
    "drum": "snare-drum-svgrepo-com.svg",
    "squirrel": "squirrel-svgrepo-com.svg",
    "tiger": "tiger-svgrepo-com.svg",
    "tree": "tree-2-svgrepo-com.svg",
    "umbrella": "umbrella-svgrepo-com.svg",
    "melon": "watermelon-1-svgrepo-com.svg",
}

# Kunci di atas adalah alias manual. Semua file lain di folder svg/ otomatis
# terdaftar memakai nama filenya (tanpa "-svgrepo-com" dan tanpa ekstensi),
# jadi menambah file baru cukup taruh di folder svg/ lalu pakai kuncinya.

def _autoregister():
    known = set(FILES.values())
    for f in sorted(os.listdir(SVG_DIR)):
        if not f.endswith(".svg") or f in known:
            continue
        key = f[:-4].replace("-svgrepo-com", "").strip().replace(" ", "-")
        key = re.sub(r"[()]", "", key).strip("-")
        FILES.setdefault(key, f)


_autoregister()

_sym = {}


def _load(key):
    raw = (SVG_DIR / FILES[key]).read_text()
    vb = re.search(r'viewBox="([^"]+)"', raw).group(1)
    inner = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")]
    inner = re.sub(r"<!--.*?-->", "", inner, flags=re.S)
    return vb, inner.strip()


def ic(key, mm, cls="", style=""):
    """Pakai aset sebagai <use>, ukuran kotak mm x mm."""
    if key not in _sym:
        _sym[key] = _load(key)
    st = f"width:{mm}mm;height:{mm}mm;flex:none;" + style
    return (f'<svg class="kk-ic {cls}" viewBox="0 0 100 100" style="{st}">'
            f'<use href="#a-{key}" width="100" height="100"/></svg>')


def sprite():
    out = ['<svg class="kk-sprite" aria-hidden="true"><defs>']
    for c, hexv in CRAYON.items():
        out.append(crayon_pattern(c, hexv))
    out.append("</defs>")
    for key, (vb, inner) in sorted(_sym.items()):
        out.append(f'<symbol id="a-{key}" viewBox="{vb}">{inner}</symbol>')
    out.append("</svg>")
    return "\n".join(out)


# ---------------------------------------------------------------- warna
C = {
    "blueberry": "#3D5A98",
    "leaf": "#5BA84F",
    "sunny": "#F5C242",
    "berry": "#E8547C",
    "grape": "#7C6BC4",
    "sky": "#4FB3D9",
    "orange": "#EE8B3C",
}
CRAYON = dict(C)

CRAYON_LABEL = {
    "blueberry": "biru", "leaf": "hijau", "sunny": "kuning",
    "berry": "merah muda", "grape": "ungu", "sky": "biru muda",
    "orange": "oranye",
}


def crayon_pattern(name, hexv):
    """Pattern isi crayon: warna dengan sapuan putih tak rata."""
    lines = []
    for i, (x, w, o) in enumerate([(0.6, 2.1, .72), (3.4, .7, .3), (5.0, 1.3, .55),
                                   (7.8, 2.6, .8), (11.2, .6, .22), (12.8, 1.7, .6),
                                   (15.4, .9, .38), (17.0, .5, .2)]):
        lines.append(f'<rect x="{x}" y="-2" width="{w}" height="24" fill="#fff" opacity="{o}"/>')
    return (f'<pattern id="cr-{name}" width="18" height="18" '
            f'patternUnits="userSpaceOnUse" patternTransform="rotate(38)">'
            f'<rect width="18" height="18" fill="{hexv}"/>{"".join(lines)}</pattern>')


def cr(name):
    return f"url(#cr-{name})"




# ---------------------------------------------------------------- ikon inline
_ICON = {
 "squiggle": '<path d="M3 16 Q7 6 11 16 Q15 26 19 16 Q22 9 26 14" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
 "pencil": '<path d="M6 22 L8 16 L19 5 L23 9 L12 20 Z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M6 22 L12 20" fill="none" stroke="currentColor" stroke-width="2.2"/>',
 "shapes": '<circle cx="10" cy="10" r="6.5" fill="none" stroke="currentColor" stroke-width="2.2"/><rect x="12" y="12" width="12" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/>',
 "num": '<text x="14" y="21" text-anchor="middle" font-family="Fredoka,sans-serif" font-size="17" font-weight="600" fill="currentColor">3</text>',
 "brush": '<path d="M20 5 L24 9 L13 20 L8 21 L9 16 Z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M8 21 Q4 22 4 25 Q8 25 9 21" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
 "scissors": '<circle cx="8" cy="21" r="3.4" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="20" cy="21" r="3.4" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M19 4 L10 18 M9 4 L18 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
 "cards": '<rect x="4" y="7" width="13" height="17" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M11 4 H22 A2 2 0 0 1 24 6 V20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
 "smiley": '<circle cx="14" cy="14" r="10.5" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="10.5" cy="11.5" r="1.5" fill="currentColor"/><circle cx="17.5" cy="11.5" r="1.5" fill="currentColor"/><path d="M9 17 Q14 21 19 17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
 "people": '<circle cx="14" cy="10" r="4.4" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M5 23 Q7 16 14 16 Q21 16 23 23" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
 "bulb": '<path d="M14 4 A7 7 0 0 1 18 17 V19 H10 V17 A7 7 0 0 1 14 4 Z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M11 22 H17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
 "arrows": '<path d="M4 14 H18 M13 9 L18 14 L13 19" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 8 V20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
}
_ALIAS = {"scribble-loop": "squiggle", "path": "squiggle", "flow-arrow": "arrows",
          "pencil-simple": "pencil", "puzzle-piece": "shapes", "magnifying-glass": "shapes",
          "x-circle": "shapes", "resize": "shapes", "number-circle-three": "num",
          "scales": "num", "palette": "brush", "paint-brush": "brush",
          "scissors": "scissors", "cards": "cards", "smiley": "smiley",
          "smiley-wink": "smiley", "users-three": "people", "lightbulb": "bulb",
          "warning-circle": "bulb"}


def pico(name, cls="kk-pico"):
    d = _ICON[_ALIAS.get(name, "shapes")]
    return f'<svg class="{cls}" viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg">{d}</svg>'


# ---------------------------------------------------------------- halaman
PAGES = []
NUM = [0]


def page(title, instruction, body, note, skill, icon,
         badge="Mulai", badge_cls="", icon_cls=""):
    if not badge_cls:
        badge_cls = {"Lanjut": "kk-badge--lanjut", "Tantangan": "kk-badge--tantangan"}.get(badge, "")
    NUM[0] += 1
    PAGES.append(f"""<section class="kk-page">
  <header class="kk-header">
    <div class="kk-skill-icon {icon_cls}">{pico(icon)}</div>
    <div class="kk-header__top"><h1 class="kk-title">{title}</h1><span class="kk-badge {badge_cls}">{badge}</span></div>
  </header>
  <div class="kk-content">
    <p class="kk-instruction">{instruction}</p>
    <div class="kk-activity">{body}</div>
    <div class="kk-parent-note">
      <span class="kk-parent-note__icon">{pico("lightbulb")}</span>
      <span>{note}</span>
    </div>
  </div>
  <footer class="kk-footer">
    <span class="kk-logo"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></span>
    <span>{skill}</span><span>{NUM[0]}</span>
  </footer>
</section>""")


def raw_page(html):
    PAGES.append(html)


def divider(no, title, sub, color, icons, blobs=""):
    """Halaman pembuka bagian, penuh warna."""
    deco = []
    spots = [(24, 176), (58, 205), (100, 186), (146, 210), (176, 178),
             (40, 245), (86, 252), (132, 244), (172, 250)]
    for (x, y), k in zip(spots, icons):
        s = random.choice([26, 30, 34])
        rot = random.randint(-14, 14)
        deco.append(f'<circle cx="{x}" cy="{y}" r="{s * 0.68}" fill="#fff" opacity=".9"/>'
                    f'<g transform="translate({x - s / 2} {y - s / 2}) rotate({rot} {s / 2} {s / 2})">'
                    f'<use href="#a-{k}" width="{s}" height="{s}"/></g>')
        if k not in _sym:
            _sym[k] = _load(k)
    stars = "".join(
        f'<path d="M{x} {y} l3 6 6.5 1-4.7 4.6 1.1 6.5L{x} {y + 15.7} l-5.9 3.1 1.1-6.5L{x - 8.5} {y + 7} l6.5-1z" '
        f'fill="{C["sunny"]}" opacity="{op}"/>'
        for x, y, op in [(186, 24, 1), (168, 62, .7), (192, 104, .5), (24, 126, .55), (60, 148, .4)])
    raw_page(f"""<section class="kk-page kk-divider">
  <svg class="kk-divider__bg" viewBox="0 0 210 297" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
    <rect width="210" height="297" fill="{color}22"/>
    {stars}
    <path d="M0 150 Q52 128 105 146 Q158 164 210 142 V297 H0 Z" fill="{color}55"/>
    <path d="M0 196 Q60 176 118 194 Q170 210 210 190 V297 H0 Z" fill="{color}"/>
    <path d="M0 232 Q58 214 116 230 Q168 244 210 226 V297 H0 Z" fill="{color}" opacity=".82"/>
    {blobs}
    {"".join(deco)}
  </svg>
  <div class="kk-divider__inner">
    <span class="kk-divider__no">Bagian {no}</span>
    <h1 class="kk-divider__title">{title}</h1>
    <p class="kk-divider__sub">{sub}</p>
  </div>
</section>""")


# ---------------------------------------------------------------- tracing garis
def stroke_row(d, w=44, h=30, reps=4, color="grape"):
    """Satu baris berisi `reps` pengulangan jejak yang sama."""
    parts = []
    for i in range(reps):
        dx = i * w
        parts.append(
            f'<g transform="translate({dx} 0)">'
            f'<path d="{d}" fill="none" stroke="{C[color]}33" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="#fff" stroke-width="0.6" stroke-dasharray="2.6 2.6" stroke-linecap="round"/>'
            f'<circle cx="{START[0]}" cy="{START[1]}" r="3.6" fill="{C["leaf"]}"/>'
            f'<circle cx="{START[0]}" cy="{START[1]}" r="1.5" fill="#fff"/>'
            f'</g>')
    return (f'<svg class="kk-svg kk-traceline" viewBox="0 0 {w * reps} {h}" '
            f'style="height:{h * 0.62}mm" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>')


START = (6, 15)


def trace_page(title, instr, d, note, rows=5, reps=4, w=44, h=30,
               deco=(), badge="Mulai", start=(6, 15)):
    global START
    START = start
    out = []
    for i in range(rows):
        a = deco[i % len(deco)] if deco else None
        icon = ic(a, 15) if a else '<span style="width:15mm;flex:none"></span>'
        row = stroke_row(d, w=w, h=h, reps=reps, color=["grape", "sky", "berry", "leaf", "orange"][i % 5])
        if i % 2:
            out.append(f'<div class="kk-trow">{row}{icon}</div>')
        else:
            out.append(f'<div class="kk-trow">{icon}{row}</div>')
    page(title, instr, "".join(out), note, "Motorik halus", "scribble-loop", badge)


# ---------------------------------------------------------------- tracing glyph
def glyph_row(char, reps=4, color="sky", solid_first=True):
    """Baris huruf/angka bergaris tiga seperti buku latin."""
    cw, H = 40, 60
    W = cw * (reps + 1)
    g = [f'<line x1="0" y1="8" x2="{W}" y2="8" stroke="#C9CEDA" stroke-width="0.8"/>',
         f'<line x1="0" y1="30" x2="{W}" y2="30" stroke="#C9CEDA" stroke-width="0.8" stroke-dasharray="5 4"/>',
         f'<line x1="0" y1="52" x2="{W}" y2="52" stroke="{C["berry"]}" stroke-width="1"/>']
    for i in range(reps + 1):
        x = cw * i + cw / 2
        if i == 0 and solid_first:
            g.append(f'<text x="{x}" y="52" text-anchor="middle" class="kk-gl" fill="{C[color]}">{char}</text>')
        else:
            g.append(f'<text x="{x}" y="52" text-anchor="middle" class="kk-gl" fill="none" '
                     f'stroke="#A7AEBD" stroke-width="1.1" stroke-dasharray="4 3.4">{char}</text>')
    return (f'<svg class="kk-svg kk-glyphrow" viewBox="0 0 {W} {H}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(g)}</svg>')


def glyph_page(title, instr, chars, note, skill, deco=(), badge="Lanjut"):
    rows = []
    for i, ch in enumerate(chars):
        a = deco[i % len(deco)] if deco else None
        icon = ic(a, 14) if a else ""
        rows.append(f'<div class="kk-trow">{glyph_row(ch, color=["sky", "berry", "grape", "leaf"][i % 4])}{icon}</div>')
    page(title, instr, "".join(rows), note, skill, "pencil-simple", badge, "kk-badge--lanjut")


# ---------------------------------------------------------------- cocokkan
def match_page(title, instr, pairs, note, skill, icon="puzzle-piece", badge="Mulai"):
    """pairs: list (kiri, kanan) key aset. Kanan diacak."""
    left = [p[0] for p in pairs]
    right = [p[1] for p in pairs]
    order = list(range(len(right)))
    while any(i == j for i, j in enumerate(order)) and len(order) > 2:
        random.shuffle(order)
    lcol = "".join(f'<div class="kk-cell">{ic(k, 26)}<span class="kk-dot"></span></div>' for k in left)
    rcol = "".join(f'<div class="kk-cell"><span class="kk-dot"></span>{ic(right[i], 26)}</div>' for i in order)
    body = (f'<div class="kk-match"><div class="kk-col kk-col--l">{lcol}</div>'
            f'<div class="kk-col kk-col--r">{rcol}</div></div>')
    page(title, instr, body, note, skill, icon, badge, "", "kk-skill-icon--shape")


# ---------------------------------------------------------------- pola
def pattern_page(title, instr, seqs, note, badge="Lanjut"):
    rows = []
    for keys, choices, in seqs:
        cells = "".join(f'<span class="kk-pcell">{ic(k, 20)}</span>' for k in keys)
        q = '<span class="kk-pcell kk-pcell--q">?</span>'
        ch = "".join(f'<span class="kk-choice">{ic(k, 18)}</span>' for k in choices)
        rows.append(f'<div class="kk-pattern"><div class="kk-pattern__seq">{cells}{q}</div>'
                    f'<div class="kk-pattern__choices">{ch}</div></div>')
    page(title, instr, "".join(rows), note, "Pola", "flow-arrow", badge, "kk-badge--lanjut", "kk-skill-icon--shape")


# ---------------------------------------------------------------- berhitung
def count_page(title, instr, groups, note, badge="Lanjut"):
    """groups: list (key, jumlah, pilihan angka)."""
    rows = []
    for key, n, opts in groups:
        items = "".join(ic(key, 17) for _ in range(n))
        boxes = "".join(f'<span class="kk-numbox">{o}</span>' for o in opts)
        rows.append(f'<div class="kk-count-row"><div class="kk-group"><div class="kk-count-items">{items}</div></div>'
                    f'<div class="kk-boxrow">{boxes}</div></div>')
    page(title, instr, "".join(rows), note, "Berhitung", "number-circle-three", badge,
         "kk-badge--lanjut", "kk-skill-icon--count")


# ---------------------------------------------------------------- warna: cari & warnai
def hunt_page(title, instr, legend, grid, note, shape="box", badge="Mulai"):
    """legend: list (char, warna). grid: list baris berisi (char, warna|None)."""
    def cell(ch, color, big=False):
        s = 46 if big else 40
        fill = cr(color) if color else "none"
        if shape == "drop":
            d = f"M{s / 2} 3 C{s * .92} {s * .42} {s * .84} {s} {s / 2} {s} C{s * .16} {s} {s * .08} {s * .42} {s / 2} 3 Z"
            sh = f'<path d="{d}" fill="{fill}" stroke="{C["blueberry"]}" stroke-width="1"/>'
        else:
            sh = f'<rect x="1.5" y="1.5" width="{s - 3}" height="{s - 3}" rx="3" fill="{fill}" stroke="{C["blueberry"]}" stroke-width="1"/>'
        return (f'<svg viewBox="0 0 {s} {s + 2}" class="kk-hunt__c" xmlns="http://www.w3.org/2000/svg">'
                f'{sh}<text x="{s / 2}" y="{s * .70}" text-anchor="middle" class="kk-gl2">{ch}</text></svg>')

    leg = "".join(cell(ch, col, True) for ch, col in legend)
    rows = "".join('<div class="kk-hunt__row">' + "".join(cell(ch, col) for ch, col in row) + "</div>"
                   for row in grid)
    body = (f'<div class="kk-hunt"><div class="kk-hunt__legend">{leg}</div>'
            f'<div class="kk-hunt__grid">{rows}</div></div>')
    page(title, instr, body, note, "Warna", "palette", badge, "", "kk-skill-icon--color")


def color_scene_page(title, instr, art, note, legend=None, badge="Mulai", skill="Warna"):
    leg = ""
    if legend:
        leg = '<div class="kk-legend">' + "".join(
            f'<span class="kk-legend__i"><svg viewBox="0 0 24 24" class="kk-legend__sw" xmlns="http://www.w3.org/2000/svg">'
            f'<rect x="1" y="1" width="22" height="22" rx="4" fill="{cr(c)}" stroke="{C["blueberry"]}" stroke-width="0.8"/></svg>'
            f'{lbl}</span>' for c, lbl in legend) + "</div>"
    page(title, instr, f'<div class="kk-center">{art}</div>{leg}', note, skill, "paint-brush",
         badge, "", "kk-skill-icon--color")


def OUT(d, w=2.6):
    return f'<path d="{d}" fill="none" stroke="{C["blueberry"]}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def OCIRC(cx, cy, r, w=2.6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["blueberry"]}" stroke-width="{w}"/>'


def scene(vb, inner, h=118):
    return (f'<svg class="kk-svg kk-scene" viewBox="{vb}" '
            f'xmlns="http://www.w3.org/2000/svg">{inner}</svg>')


# ---------------------------------------------------------------- jalan / maze
def path_page(title, instr, d, start_key, end_key, note, badge="Lanjut",
              start_xy=(0, 0), end_xy=(0, 0), deco=()):
    for k in (start_key, end_key) + tuple(x[0] for x in deco):
        if k not in _sym:
            _sym[k] = _load(k)

    def put(k, x, y, sz=24):
        return (f'<g transform="translate({x - sz / 2} {y - sz / 2})">'
                f'<use href="#a-{k}" width="{sz}" height="{sz}"/></g>')

    art = (f'<svg class="kk-svg kk-scene" viewBox="0 0 200 150" xmlns="http://www.w3.org/2000/svg">'
           f'<path d="{d}" fill="none" stroke="{C["sunny"]}55" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="{d}" fill="none" stroke="#fff" stroke-width="1" stroke-dasharray="4 4" stroke-linecap="round"/>'
           + "".join(put(k, x, y, sz) for k, x, y, sz in deco)
           + put(start_key, *start_xy, 26) + put(end_key, *end_xy, 26) + "</svg>")
    page(title, instr, f'<div class="kk-center">{art}</div>', note, "Motorik halus", "path", badge)


# ---------------------------------------------------------------- gunting
def cut_page(title, instr, strips, note, badge="Tantangan"):
    rows = []
    for kind, key in strips:
        if kind == "pendek":
            line = '<div class="kk-cutline-h kk-cutline-h--short"></div><span style="flex:1"></span>'
        elif kind == "lurus":
            line = '<div class="kk-cutline-h"></div>'
        elif kind == "gelombang":
            line = ('<svg class="kk-cutsvg" viewBox="0 0 160 20" xmlns="http://www.w3.org/2000/svg">'
                    f'<path d="M2 10 Q22 0 42 10 Q62 20 82 10 Q102 0 122 10 Q142 20 158 10" fill="none" '
                    f'stroke="{C["berry"]}" stroke-width="3.4" stroke-dasharray="7 5" stroke-linecap="round"/></svg>')
        else:
            line = ('<svg class="kk-cutsvg" viewBox="0 0 160 20" xmlns="http://www.w3.org/2000/svg">'
                    f'<path d="M2 16 L22 4 L42 16 L62 4 L82 16 L102 4 L122 16 L142 4 L158 16" fill="none" '
                    f'stroke="{C["berry"]}" stroke-width="3.4" stroke-dasharray="7 5" stroke-linecap="round"/></svg>')
        rows.append(f'<div class="kk-cut-strip"><span class="kk-cut-ico">{pico("scissors")}</span>'
                    f'{line}{ic(key, 18)}</div>')
    page(title, instr, "".join(rows), note, "Gunting", "scissors", badge, "kk-badge--tantangan", "kk-skill-icon--cut")


def cut_shape_page(title, instr, shapes, note, badge="Tantangan"):
    cells = []
    for d, key, color in shapes:
        cells.append(f'<div class="kk-cutcell">'
                     f'<svg viewBox="0 0 100 100" class="kk-cutshape" xmlns="http://www.w3.org/2000/svg">'
                     f'<path d="{d}" fill="{cr(color)}" fill-opacity=".55" stroke="{C["berry"]}" '
                     f'stroke-width="3" stroke-dasharray="7 5" stroke-linejoin="round"/></svg>'
                     f'<span class="kk-cutcell__ic">{ic(key, 16)}</span></div>')
    page(title, instr, f'<div class="kk-cutgrid2">{"".join(cells)}</div>', note, "Gunting", "scissors",
         badge, "kk-badge--tantangan", "kk-skill-icon--cut")


# ---------------------------------------------------------------- pilih dalam baris
def choose_page(title, instr, rows, note, skill, icon, badge="Lanjut", ring=True):
    """rows: list (target_key|None, [pilihan keys])."""
    out = []
    for target, opts in rows:
        head = (f'<div class="kk-choose__t">{ic(target, 24)}</div>'
                f'<span class="kk-choose__bar"></span>') if target else ""
        cells = "".join(f'<span class="kk-choose__o">{ic(k, 24)}</span>' for k in opts)
        out.append(f'<div class="kk-choose">{head}<div class="kk-choose__row">{cells}</div></div>')
    page(title, instr, "".join(out), note, skill, icon, badge,
         "kk-badge--lanjut" if badge == "Lanjut" else "", "kk-skill-icon--shape")


def size_page(title, instr, rows, note):
    out = []
    for key in rows:
        out.append(f'<div class="kk-choose"><div class="kk-choose__row kk-choose__row--wide">'
                   f'<span class="kk-choose__o">{ic(key, 34)}</span>'
                   f'<span class="kk-choose__o">{ic(key, 16)}</span>'
                   f'<span class="kk-choose__o">{ic(key, 25)}</span></div></div>')
    page(title, instr, "".join(out), note, "Bentuk", "resize", "Lanjut", "kk-badge--lanjut", "kk-skill-icon--shape")


# ================================================================ ISI BUNDEL
# --- Sampul
def cover():
    keys = ("owl", "frog", "cat", "flower", "tree", "butterfly", "ladybug", "duck", "bunny", "bird")
    for k in keys:
        if k not in _sym:
            _sym[k] = _load(k)
    put = lambda k, x, y, s: f'<g transform="translate({x} {y})"><use href="#a-{k}" width="{s}" height="{s}"/></g>'
    raw_page(f"""<section class="kk-page kk-cover">
  <svg class="kk-cover__bg" viewBox="0 0 210 297" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
    <rect width="210" height="297" fill="#EAF1FA"/>
    <circle cx="184" cy="26" r="14" fill="{C['sunny']}"/>
    <ellipse cx="30" cy="124" rx="26" ry="12" fill="#fff"/><ellipse cx="48" cy="118" rx="17" ry="10" fill="#fff"/>
    <ellipse cx="178" cy="138" rx="22" ry="11" fill="#fff"/><ellipse cx="163" cy="133" rx="14" ry="8" fill="#fff"/>
    <path d="M0 188 Q52 166 105 182 Q158 198 210 178 V297 H0 Z" fill="{C['leaf']}"/>
    <path d="M0 228 Q60 210 118 226 Q170 240 210 222 V297 H0 Z" fill="#468B3C"/>
    {put('butterfly', 88, 112, 30)}
    {put('bird', 40, 152, 26)}
    {put('tree', 12, 184, 48)}
    {put('owl', 64, 196, 42)}
    {put('frog', 112, 202, 38)}
    {put('flower', 154, 184, 36)}
    {put('cat', 30, 240, 36)}
    {put('duck', 88, 248, 32)}
    {put('bunny', 130, 246, 32)}
    {put('ladybug', 172, 244, 28)}
  </svg>
  <div class="kk-cover__inner">
    <div class="kk-logo kk-logo--big"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></div>
    <h1 class="kk-cover__title">Siap Belajar<br>Usia 3 Tahun</h1>
    <p class="kk-cover__sub">62 halaman aktivitas<br>cukup krayon dan gunting</p>
  </div>
</section>""")


def bagian_1():
    divider(1, "Garis dan Coretan", "Tangan belajar berhenti, berbelok, dan berputar",
            C["grape"], ["squirrel", "owl", "butterfly", "ladybug", "bird", "frog", "deer", "bunny", "animal-domestic-pet-11"])
    trace_page("Garis Lurus", "Tarik dari titik hijau sampai ujung.",
               "M6 15 H38", "Garis lurus melatih tangan berhenti di tempat. Keluar jalur itu wajar.",
               rows=5, reps=4, deco=("bike", "airplane", "helicopter", "sailboat", "bike"), start=(6, 15))
    trace_page("Garis Tegak", "Tarik dari titik hijau ke bawah.",
               "M13 6 V46", "Gerakan atas ke bawah dikuasai lebih dulu. Ini dasar huruf l, i, dan t.",
               rows=3, reps=6, w=26, h=52, deco=("carrot", "corn", "tree"), start=(13, 6))
    trace_page("Garis Miring", "Tarik dari titik hijau ke ujung yang lain.",
               "M6 25 L38 6", "Garis miring lebih sulit. Kalau anak kesulitan, pandu tangannya sekali lalu lepas.",
               rows=5, deco=("kangaroo", "deer", "bunny", "dolphin", "shark"), start=(6, 25))
    trace_page("Garis Bukit", "Ikuti jalannya naik lalu turun.",
               "M6 25 Q22 3 38 25", "Lengkungan melatih pergelangan berputar. Sebut sambil menarik: naik, turun.",
               rows=5, deco=("camel", "deer", "elephant", "giraffe", "camel"), start=(6, 25))
    trace_page("Garis Lembah", "Ikuti jalannya turun lalu naik.",
               "M6 6 Q22 28 38 6", "Kebalikan halaman sebelumnya. Dua arah ini menyiapkan huruf u dan n.",
               rows=5, deco=("fish", "dolphin", "duck", "fish2", "shark"), start=(6, 6))
    trace_page("Garis Gelombang", "Ikuti ombaknya sampai ujung.",
               "M6 17 Q14 4 22 17 Q30 30 38 17", "Ombak menggabungkan naik dan turun tanpa mengangkat tangan.",
               rows=5, deco=("sailboat", "fish", "dolphin", "duck", "shark"), start=(6, 17))
    trace_page("Garis Zigzag", "Ikuti gigi gergajinya.",
               "M6 26 L14 6 L22 26 L30 6 L38 26", "Zigzag butuh berhenti mendadak lalu ganti arah. Pelan saja.",
               rows=5, deco=("tiger", "crocodile", "cactus", "tree", "giraffe"), start=(6, 26))
    trace_page("Lingkaran", "Mulai dari titik hijau, putar sampai bertemu lagi.",
               "M22 6 A11 11 0 1 1 21.6 6", "Lingkaran searah jarum terbalik. Ini gerakan dasar huruf o, a, dan c.",
               rows=4, reps=4, h=34, deco=("apple", "donut", "egg", "melon"), start=(22, 6))
    trace_page("Garis Silang", "Tarik dua garis sampai bersilangan.",
               "M8 6 L36 26 M36 6 L8 26", "Menyilang berarti tangan melewati garis tengah tubuh. Ini penting.",
               rows=5, deco=("butterfly", "ladybug", "bird", "flower", "cactus"), start=(8, 6))
    trace_page("Garis Melingkar", "Ikuti putarannya tanpa mengangkat tangan.",
               "M6 24 C8 6 20 6 16 20 C13 30 26 30 24 15 C22 5 34 8 38 22",
               "Loop berulang menyiapkan tulisan sambung. Lakukan sambil bersenandung.",
               rows=4, h=34, deco=("owl", "squirrel", "cat", "dog"), start=(6, 24))
    trace_page("Setengah Lingkaran", "Ikuti busurnya dari titik hijau.",
               "M6 24 A16 16 0 0 1 38 24", "Busur ini bagian dari huruf n, m, dan h.",
               rows=5, deco=("umbrella", "burger", "icecream", "watermelon", "umbrella"), start=(6, 24))


def bagian_2():
    divider(2, "Angka dan Huruf", "Bentuknya dulu, hafalannya belakangan",
            C["sky"], ["boy", "girl", "owl", "apple", "flamingo", "chipmunk", "guitar", "drum", "pineapple"])
    glyph_page("Telusuri Angka 1 2 3", "Telusuri angkanya dari kiri ke kanan.", ["1", "2", "3"],
               "Sebut angkanya keras-keras setiap kali ditelusuri. Suara membantu ingatan.",
               "Angka", ("apple", "butterfly", "duck"))
    glyph_page("Telusuri Angka 4 5 6", "Telusuri angkanya. Mulai dari titik paling atas.", ["4", "5", "6"],
               "Kalau anak menelusuri dari bawah, biarkan. Arah baku menyusul nanti.",
               "Angka", ("fish", "flower", "egg"))
    glyph_page("Telusuri Angka 7 8 9", "Telusuri angkanya pelan-pelan.", ["7", "8", "9"],
               "Angka 8 paling sulit. Boleh dipecah jadi dua lingkaran dulu.",
               "Angka", ("grape", "strawberry", "carrot"))
    glyph_page("Telusuri Huruf a b c", "Telusuri hurufnya. Sebut bunyinya sambil menarik.", ["a", "b", "c"],
               "Huruf kecil lebih sering ditemui anak dalam bacaan daripada huruf besar.",
               "Huruf", ("apple", "bird", "cat"))
    glyph_page("Telusuri Huruf d e f", "Telusuri hurufnya dari titik awal.", ["d", "e", "f"],
               "Bunyikan huruf, jangan namanya: d berbunyi de, bukan dé.",
               "Huruf", ("dog", "elephant", "fish"))
    glyph_page("Telusuri Huruf A B C", "Telusuri huruf besarnya.", ["A", "B", "C"],
               "Huruf besar dipakai untuk awal nama. Coba tulis huruf depan nama anak di kertas kosong.",
               "Huruf", ("airplane", "bike", "cactus"))


def bagian_3():
    divider(3, "Cocokkan dan Bedakan", "Mata belajar melihat sama dan tidak sama",
            C["leaf"], ["cat", "dog", "duck", "frog", "owl", "fish", "bunny", "pelican", "kangaroo-animal"])
    match_page("Cari Pasangannya", "Tarik garis dari kiri ke pasangannya di kanan.",
               [("cat", "cat"), ("duck", "duck"), ("frog", "frog"), ("owl", "owl"), ("fish", "fish")],
               "Kalau anak ragu, tutup satu baris dengan tangan agar pilihannya lebih sedikit.", "Cocokkan")
    match_page("Cocokkan Buahnya", "Tarik garis ke buah yang sama.",
               [("apple", "apple"), ("grape", "grape"), ("strawberry", "strawberry"),
                ("watermelon", "watermelon"), ("carrot", "carrot")],
               "Sambil mencocokkan, sebut warnanya. Dua keterampilan sekaligus tanpa halaman tambahan.", "Cocokkan")
    choose_page("Mana yang Sama", "Lingkari gambar yang sama dengan yang di kotak kiri.",
                [("cat", ["dog", "cat", "duck", "owl"]),
                 ("apple", ["grape", "carrot", "apple", "corn"]),
                 ("fish", ["fish", "frog", "bird", "dolphin"]),
                 ("bike", ["airplane", "sailboat", "helicopter", "bike"]),
                 ("flower", ["tree", "flower", "cactus", "corn"])],
                "Lingkari boleh berantakan. Yang dinilai pilihannya, bukan bulatannya.", "Cocokkan", "magnifying-glass")
    choose_page("Mana yang Berbeda", "Coret satu gambar yang berbeda sendiri.",
                [(None, ["duck", "duck", "duck", "owl"]),
                 (None, ["apple", "apple", "grape", "apple"]),
                 (None, ["frog", "fish", "fish", "fish"]),
                 (None, ["tree", "tree", "tree", "flower"]),
                 (None, ["dog", "dog", "cat", "dog"])],
                "Tanya alasannya: kenapa yang itu berbeda. Jawabannya lebih berharga daripada coretannya.",
                "Bedakan", "x-circle")
    size_page("Besar dan Kecil", "Lingkari yang paling besar di setiap baris.",
              ["elephant", "apple", "fish", "tree", "butterfly"],
              "Bandingkan juga dengan benda nyata di rumah: sendok besar dan sendok kecil.")


def bagian_4():
    divider(4, "Pola", "Menebak apa yang datang berikutnya",
            C["orange"], ["butterfly", "flower", "apple", "ladybug", "grape", "avocado", "bird", "squirrel-animal", "cat"])
    pattern_page("Lanjutkan Pola", "Lingkari gambar yang seharusnya ada di kotak tanda tanya.",
                 [(["apple", "grape", "apple", "grape"], ["apple", "corn"]),
                  (["duck", "frog", "duck", "frog"], ["fish", "duck"]),
                  (["flower", "tree", "flower", "tree"], ["flower", "cactus"]),
                  (["cat", "dog", "cat", "dog"], ["cat", "owl"]),
                  (["butterfly", "ladybug", "butterfly", "ladybug"], ["bird", "butterfly"])],
                 "Bacakan polanya keras-keras: apel, anggur, apel, anggur, lalu? Telinga menangkap pola lebih cepat daripada mata.")
    pattern_page("Pola Berulang", "Lanjutkan pola dua-dua.",
                 [(["apple", "apple", "carrot", "carrot"], ["apple", "carrot"]),
                  (["fish", "fish", "dolphin", "dolphin"], ["fish", "shark"]),
                  (["owl", "owl", "bird", "bird"], ["bird", "owl"]),
                  (["tree", "tree", "flower", "flower"], ["tree", "flower"]),
                  (["boy", "boy", "girl", "girl"], ["girl", "boy"])],
                 "Pola dua-dua lebih sulit daripada satu-satu. Kalau macet, kembali ke halaman sebelumnya.")
    pattern_page("Pola Tiga Gambar", "Lanjutkan pola tiga gambar.",
                 [(["apple", "grape", "corn", "apple", "grape"], ["corn", "apple"]),
                  (["cat", "dog", "duck", "cat", "dog"], ["cat", "duck"]),
                  (["fish", "frog", "duck", "fish", "frog"], ["duck", "fish"]),
                  (["flower", "tree", "cactus", "flower", "tree"], ["flower", "cactus"])],
                 "Ini halaman tersulit di bagian pola. Anak tiga tahun boleh melewatinya.",
                 badge="Tantangan")


def count_match_page(title, instr, rows, note):
    out = []
    for key, n in rows:
        items = "".join(ic(key, 16) for _ in range(n))
        out.append(f'<div class="kk-cmrow"><div class="kk-group"><div class="kk-count-items">{items}</div></div>'
                   f'<span class="kk-dot"></span><span class="kk-cmnum">{n}</span></div>')
    random.shuffle(out)
    page(title, instr, "".join(out), note, "Berhitung", "number-circle-three", "Tantangan",
         "kk-badge--tantangan", "kk-skill-icon--count")


def more_page(title, instr, rows, note):
    out = []
    for key, a, b in rows:
        left = "".join(ic(key, 15) for _ in range(a))
        right = "".join(ic(key, 15) for _ in range(b))
        out.append(f'<div class="kk-more"><div class="kk-group kk-group--half"><div class="kk-count-items">{left}</div></div>'
                   f'<span class="kk-more__vs">atau</span>'
                   f'<div class="kk-group kk-group--half"><div class="kk-count-items">{right}</div></div></div>')
    page(title, instr, "".join(out), note, "Berhitung", "scales", "Tantangan",
         "kk-badge--tantangan", "kk-skill-icon--count")


def bagian_5():
    divider(5, "Berhitung", "Menyentuh satu benda untuk satu angka",
            C["berry"], ["apple", "strawberry", "grape", "egg", "donut", "carrot", "corn", "pineapple", "avocado"])
    count_page("Hitung Sampai Tiga", "Hitung benda di kotak, lalu lingkari angkanya.",
               [("apple", 1, [1, 2, 3]), ("duck", 2, [1, 2, 3]), ("fish", 3, [1, 2, 3]),
                ("flower", 2, [1, 2, 3]), ("egg", 1, [1, 2, 3])],
               "Sentuh tiap benda sambil menyebut angkanya. Menghitung tanpa menyentuh sering meleset.")
    count_page("Hitung Sampai Lima", "Hitung benda di kotak, lalu lingkari angkanya.",
               [("strawberry", 4, [3, 4, 5]), ("butterfly", 5, [3, 4, 5]), ("carrot", 3, [3, 4, 5]),
                ("ladybug", 5, [3, 4, 5]), ("corn", 4, [3, 4, 5])],
               "Angka terakhir yang disebut adalah jumlahnya. Konsep ini butuh waktu berbulan-bulan.")
    count_page("Hitung Sampai Sepuluh", "Hitung benda di kotak, lalu lingkari angkanya.",
               [("grape", 7, [6, 7, 8]), ("egg", 6, [6, 7, 8]), ("donut", 8, [6, 7, 8]),
                ("apple", 9, [8, 9, 10])],
               "Di atas lima, susun benda berbaris dulu. Tumpukan acak membuat anak menghitung ulang.")
    count_match_page("Cocokkan Jumlah", "Tarik garis dari kelompok benda ke angka yang tepat.",
                     [("fish", 2), ("duck", 4), ("apple", 3), ("butterfly", 5), ("egg", 1)],
                     "Kalau anak salah, hitung bersama sambil menunjuk. Jangan langsung dibetulkan.")
    more_page("Mana yang Lebih Banyak", "Lingkari kelompok yang lebih banyak.",
              [("apple", 2, 5), ("fish", 6, 3), ("duck", 4, 2), ("strawberry", 3, 7)],
              "Anak sering memilih yang memakan tempat lebih luas, bukan yang lebih banyak. Itu normal di usia ini.")


# ---------------------------------------------------------------- adegan mewarnai
def art_langit():
    import math
    p = [OCIRC(36, 40, 17)]
    for i in range(8):
        a = math.radians(i * 45 + 22)
        p.append(OUT(f"M{36 + 21 * math.cos(a):.1f} {40 + 21 * math.sin(a):.1f} "
                     f"L{36 + 29 * math.cos(a):.1f} {40 + 29 * math.sin(a):.1f}", 2.6))
    for cx, cy, sc in [(132, 40, 1.05), (64, 96, .8), (166, 104, .66)]:
        p.append(f'<g transform="translate({cx} {cy}) scale({sc})">'
                 + OUT("M-34 12 A13 13 0 0 1 -30 -10 A17 17 0 0 1 2 -16 A14 14 0 0 1 30 -2 "
                       "A11 11 0 0 1 30 12 Z", 2.6 / sc) + "</g>")
    # balon udara
    p.append(OUT("M100 104 C82 104 74 118 78 132 C81 143 92 150 100 156 "
                 "C108 150 119 143 122 132 C126 118 118 104 100 104 Z"))
    p.append(OUT("M92 152 H108 L106 166 H94 Z", 2.4))
    p.append(OUT("M94 156 L96 166 M106 156 L104 166", 2.2))
    for bx, by, sc in [(26, 122, 1), (156, 150, .85), (72, 148, .7)]:
        p.append(OUT(f"M{bx - 11 * sc} {by} Q{bx - 5 * sc} {by - 9 * sc} {bx} {by} "
                     f"Q{bx + 5 * sc} {by - 9 * sc} {bx + 11 * sc} {by}", 2.4))
    p.append(OUT("M6 176 Q52 164 100 174 Q150 184 198 172", 2.8))
    return scene("0 0 200 186", "".join(p), 116)


def art_laut():
    p = [OUT("M4 22 Q26 8 48 22 Q70 36 92 22 Q114 8 136 22 Q158 36 180 22 Q192 14 198 20", 2.4)]
    for x, y, s, flip in [(48, 62, 1.0, 1), (132, 58, .8, -1), (72, 118, .9, -1), (156, 122, .7, 1)]:
        p.append(f'<g transform="translate({x} {y}) scale({s * flip} {s})">'
                 + OUT("M-26 0 C-18 -16 12 -16 24 0 C12 16 -18 16 -26 0 Z")
                 + OUT("M24 0 L38 -12 L38 12 Z") + OCIRC(-14, -4, 2.6, 2.2) + "</g>")
    p.append(OUT("M100 92 L108 108 L126 110 L113 122 L117 140 L100 131 L83 140 L87 122 L74 110 L92 108 Z"))
    for cx, cy, r in [(28, 96, 5), (40, 112, 3.4), (24, 126, 4.2), (176, 88, 4.4), (186, 102, 3)]:
        p.append(OCIRC(cx, cy, r, 2.2))
    p.append(OUT("M4 160 Q16 130 28 160 Q40 132 52 160 Q64 136 76 160", 2.4))
    p.append(OUT("M124 160 Q136 132 148 160 Q160 134 172 160", 2.4))
    p.append(OUT("M2 166 H198", 2.6))
    return scene("0 0 200 176", "".join(p), 116)


def art_kebun():
    import math
    p = []
    for cx, cy, r in [(40, 60, 15), (104, 48, 13), (162, 68, 14)]:
        pr = r * .62
        for i in range(6):
            a = math.radians(i * 60 + 15)
            p.append(OCIRC(cx + r * math.cos(a), cy + r * math.sin(a), pr, 2.4))
        p.append(OCIRC(cx, cy, r * .52, 2.4))
        base = cy + r + pr
        p.append(OUT(f"M{cx} {base} V152", 2.8))
        p.append(OUT(f"M{cx} {base + 20} Q{cx - 20} {base + 12} {cx - 22} {base + 30} "
                     f"Q{cx - 6} {base + 34} {cx} {base + 20}", 2.4))
        p.append(OUT(f"M{cx} {base + 40} Q{cx + 20} {base + 32} {cx + 22} {base + 50} "
                     f"Q{cx + 6} {base + 54} {cx} {base + 40}", 2.4))
    # kupu-kupu
    p.append('<g transform="translate(166 26) scale(0.82)">'
             + OUT("M0 0 C-8 -16 -26 -18 -24 -4 C-23 6 -10 8 0 0 Z", 2.4)
             + OUT("M0 0 C-8 16 -24 18 -23 6 C-22 -2 -10 -6 0 0 Z", 2.4)
             + OUT("M0 0 C8 -16 26 -18 24 -4 C23 6 10 8 0 0 Z", 2.4)
             + OUT("M0 0 C8 16 24 18 23 6 C22 -2 10 -6 0 0 Z", 2.4)
             + OUT("M0 -8 V9 M-2 -9 L-6 -15 M2 -9 L6 -15", 2.2) + "</g>")
    p.append(OUT("M4 152 H196", 2.8))
    for gx in range(14, 194, 20):
        p.append(OUT(f"M{gx} 152 Q{gx + 4} 141 {gx + 9} 152", 2.2))
    return scene("0 0 200 162", "".join(p), 112)


def art_buah():
    p = []
    # apel
    cx, cy = 50, 52
    p.append(OUT(f"M{cx} {cy-22} C{cx-10} {cy-38} {cx-36} {cy-32} {cx-36} {cy-6} "
                 f"C{cx-36} {cy+22} {cx-16} {cy+38} {cx} {cy+28} "
                 f"C{cx+16} {cy+38} {cx+36} {cy+22} {cx+36} {cy-6} "
                 f"C{cx+36} {cy-32} {cx+10} {cy-38} {cx} {cy-22} Z"))
    p.append(OUT(f"M{cx} {cy-26} V{cy-44}", 2.6))
    p.append(OUT(f"M{cx+1} {cy-38} Q{cx+20} {cy-50} {cx+22} {cy-34} Q{cx+8} {cy-30} {cx+1} {cy-38} Z", 2.4))
    # pir
    cx, cy = 150, 52
    p.append(OUT(f"M{cx} {cy-34} C{cx-13} {cy-26} {cx-11} {cy-8} {cx-19} {cy+4} "
                 f"C{cx-30} {cy+20} {cx-15} {cy+38} {cx} {cy+38} "
                 f"C{cx+15} {cy+38} {cx+30} {cy+20} {cx+19} {cy+4} "
                 f"C{cx+11} {cy-8} {cx+13} {cy-26} {cx} {cy-34} Z"))
    p.append(OUT(f"M{cx} {cy-34} V{cy-48}", 2.6))
    p.append(OUT(f"M{cx+1} {cy-44} Q{cx+18} {cy-54} {cx+20} {cy-40} Q{cx+8} {cy-36} {cx+1} {cy-44} Z", 2.4))
    # anggur
    cx, cy = 50, 138
    for row, n in enumerate([4, 3, 2, 1]):
        for i in range(n):
            x = cx - (n - 1) * 9.5 + i * 19
            p.append(OCIRC(x, cy - 12 + row * 16, 9.5, 2.4))
    p.append(OUT(f"M{cx} {cy-22} V{cy-38}", 2.6))
    p.append(OUT(f"M{cx+1} {cy-34} Q{cx+20} {cy-46} {cx+22} {cy-30} Q{cx+8} {cy-26} {cx+1} {cy-34} Z", 2.4))
    # semangka
    cx, cy = 150, 150
    p.append(OUT(f"M{cx-42} {cy+14} A42 42 0 0 1 {cx+42} {cy+14} Z"))
    p.append(OUT(f"M{cx-34} {cy+14} A34 34 0 0 1 {cx+34} {cy+14}", 2.2))
    for sx, sy in [(cx - 16, cy - 4), (cx, cy - 10), (cx + 16, cy - 4), (cx - 8, cy + 6), (cx + 8, cy + 6)]:
        p.append(f'<ellipse cx="{sx}" cy="{sy}" rx="3" ry="4.4" fill="none" '
                 f'stroke="{C["blueberry"]}" stroke-width="2.2"/>')
    return scene("0 0 200 182", "".join(p), 118)


def bagian_6():
    divider(6, "Warna", "Krayon boleh keluar garis, itu bukan kesalahan",
            C["sunny"], ["flower", "butterfly", "apple2", "grape", "strawberry", "watermelon", "icecream", "donut", "drumstick"])
    hunt_page("Cari Huruf n, b, dan u", "Warnai kotak yang hurufnya sama dengan contoh di atas.",
              [("n", "sky"), ("b", "sunny"), ("u", "berry")],
              [[("n", "sky"), ("b", None), ("l", None)],
               [("u", None), ("g", None), ("u", None)],
               [("s", None), ("b", None), ("n", None)],
               [("b", None), ("n", None), ("d", None)]],
              "Anak tidak perlu tahu nama hurufnya. Yang dilatih di sini mata mencocokkan bentuk.")
    hunt_page("Tetesan Hujan k, e, v", "Warnai tetesan sesuai warna contoh di baris atas.",
              [("k", "sky"), ("e", "leaf"), ("v", "orange")],
              [[("k", None), ("e", None), ("v", None)],
               [("e", None), ("k", None), ("e", None)],
               [("v", None), ("v", None), ("k", None)]],
              "Huruf k, e, dan v punya garis lurus dan lengkung. Bagus untuk melihat perbedaan bentuk.",
              shape="drop", badge="Lanjut")
    color_scene_page("Warnai Langit", "Warnai matahari, awan, dan balonnya.", art_langit(),
                     "Sebutkan warnanya sambil anak mewarnai. Kosakata warna tumbuh dari percakapan, bukan hafalan.",
                     legend=[("sunny", "matahari"), ("sky", "langit"), ("berry", "balon")])
    color_scene_page("Warnai Bawah Laut", "Warnai ikan, bintang laut, dan rumput lautnya.", art_laut(),
                     "Tanya ikan mana yang paling besar. Halaman mewarnai bisa jadi bahan ngobrol.",
                     legend=[("sky", "air"), ("orange", "ikan"), ("sunny", "bintang laut")])
    color_scene_page("Warnai Kebun", "Warnai bunga, daun, dan kupu-kupunya.", art_kebun(),
                     "Kelopak bunga adalah lingkaran kecil berulang. Bagus untuk melatih tangan berhenti di tepi.",
                     legend=[("berry", "bunga"), ("leaf", "daun"), ("grape", "kupu-kupu")])
    color_scene_page("Warnai Buah", "Warnai buah-buahannya.", art_buah(),
                     "Sebelum mewarnai, tanya buah apa saja yang pernah dimakan minggu ini.",
                     legend=[("berry", "apel"), ("leaf", "pir"), ("grape", "anggur"), ("orange", "semangka")])
    color_scene_page("Warnai Sesuai Angka", "Warnai sesuai nomor: 1 biru, 2 kuning, 3 hijau.",
                     art_numcolor(),
                     "Halaman ini menggabungkan angka dan warna. Boleh dikerjakan setengah lalu dilanjut besok.",
                     legend=[("sky", "1"), ("sunny", "2"), ("leaf", "3")], badge="Tantangan")


def art_numcolor():
    p = []
    grid = [[1, 2, 3, 1], [3, 1, 2, 2], [2, 3, 1, 3], [1, 2, 3, 1]]
    for r, row in enumerate(grid):
        for c, n in enumerate(row):
            x, y = 8 + c * 47, 6 + r * 41
            cx, cy = x + 20, y + 18
            k = (r + c) % 4
            if k == 0:
                p.append(f'<rect x="{x}" y="{y}" width="40" height="36" rx="5" fill="none" '
                         f'stroke="{C["blueberry"]}" stroke-width="2"/>')
            elif k == 1:
                p.append(OCIRC(cx, cy, 18, 2))
            elif k == 2:
                p.append(OUT(f"M{cx} {y} L{x + 40} {y + 36} L{x} {y + 36} Z", 2))
                cy = y + 25
            else:
                p.append(OUT(f"M{cx} {y} L{x + 40} {cy} L{cx} {y + 36} L{x} {cy} Z", 2))
            p.append(f'<text x="{cx}" y="{cy + 7}" text-anchor="middle" class="kk-gl3">{n}</text>')
    return scene("0 0 200 174", "".join(p), 116)


def bagian_7():
    divider(7, "Jalan Berliku", "Menjaga krayon tetap di dalam jalan",
            C["blueberry"], ["bike", "airplane", "sailboat", "helicopter", "cat2", "dog2", "elephant2", "crocodile-animal", "bird-1"])
    path_page("Antar Kepik ke Bunga", "Ikuti jalannya dari kiri sampai ke ujung.",
              "M20 128 Q62 128 78 92 Q94 56 132 52 Q168 48 180 26",
              "ladybug", "flower",
              "Jalan lebar dulu. Kalau anak sudah rapi, ulangi halaman ini dengan krayon lebih tipis.",
              start_xy=(20, 128), end_xy=(180, 26),
              deco=[("butterfly", 40, 40, 22), ("tree", 150, 118, 26), ("flower", 92, 132, 20)])
    path_page("Jalan Berbelok", "Ikuti jalannya sampai bertemu hiu.",
              "M20 24 H84 V78 H36 V126 H176",
              "fish", "shark",
              "Sudut siku-siku memaksa tangan berhenti total lalu berbelok. Lebih sulit daripada lengkungan.",
              start_xy=(20, 24), end_xy=(176, 126),
              deco=[("dolphin", 150, 40, 24), ("fish2", 110, 96, 22), ("sailboat", 62, 132, 22)])
    path_page("Jalan Berkelok", "Ikuti jalannya sampai ke ujung.",
              "M20 36 Q56 12 88 40 Q120 68 92 96 Q64 124 108 134 Q152 146 180 114",
              "sailboat", "dolphin",
              "Kelokan berlawanan arah berturut-turut. Ini halaman tersulit di bagian ini.", badge="Tantangan",
              start_xy=(20, 36), end_xy=(180, 114),
              deco=[("shark", 170, 34, 24), ("fish", 34, 100, 20), ("duck", 148, 78, 22)])



def face_svg(kind, color, fill=True):
    B = C["blueberry"]
    g = [f'<circle cx="50" cy="50" r="42" fill="{cr(color) if fill else "none"}" '
         f'fill-opacity="{0.65 if fill else 1}" stroke="{B}" stroke-width="2.6"/>']
    if kind == "senang":
        g += [f'<path d="M30 40 Q35 33 40 40" fill="none" stroke="{B}" stroke-width="3" stroke-linecap="round"/>',
              f'<path d="M60 40 Q65 33 70 40" fill="none" stroke="{B}" stroke-width="3" stroke-linecap="round"/>',
              f'<path d="M32 60 Q50 76 68 60" fill="none" stroke="{B}" stroke-width="3" stroke-linecap="round"/>']
    elif kind == "sedih":
        g += [f'<circle cx="36" cy="42" r="3.4" fill="{B}"/><circle cx="64" cy="42" r="3.4" fill="{B}"/>',
              f'<path d="M32 70 Q50 56 68 70" fill="none" stroke="{B}" stroke-width="3" stroke-linecap="round"/>',
              f'<path d="M36 48 Q31 58 36 62 Q41 58 36 48 Z" fill="none" stroke="{B}" stroke-width="2.4"/>']
    elif kind == "marah":
        g += [f'<path d="M28 36 L42 42 M72 36 L58 42" fill="none" stroke="{B}" stroke-width="3" stroke-linecap="round"/>',
              f'<circle cx="36" cy="48" r="3.4" fill="{B}"/><circle cx="64" cy="48" r="3.4" fill="{B}"/>',
              f'<path d="M34 68 H66" fill="none" stroke="{B}" stroke-width="3" stroke-linecap="round"/>']
    else:  # kaget
        g += [f'<circle cx="36" cy="42" r="5" fill="none" stroke="{B}" stroke-width="2.6"/>',
              f'<circle cx="64" cy="42" r="5" fill="none" stroke="{B}" stroke-width="2.6"/>',
              f'<ellipse cx="50" cy="66" rx="8" ry="10" fill="none" stroke="{B}" stroke-width="2.8"/>']
    return ('<svg viewBox="0 0 100 100" class="kk-facesvg" xmlns="http://www.w3.org/2000/svg">'
            + "".join(g) + "</svg>")


def bagian_8():
    divider(8, "Perasaan", "Menamai yang dirasakan sebelum meledak",
            C["grape"], ["happy", "unhappy", "crying", "grinning", "boy", "avatar-girl", "cartoon-child-girl", "boy-brother-cartoon", "owl"])
    faces = [("senang", "sunny"), ("sedih", "sky"), ("marah", "berry"), ("kaget", "grape")]
    body = '<div class="kk-facegrid">' + "".join(
        f'<div class="kk-face">{face_svg(k, col)}<span class="kk-face__label">{k}</span></div>'
        for k, col in faces) + "</div>"
    page("Bagaimana Perasaanmu", "Lingkari wajah yang paling mirip perasaanmu hari ini.", body,
         "Tanpa nama, perasaan sulit dikendalikan. Sebutkan juga perasaan Anda sendiri hari ini.",
         "Sosial emosional", "smiley", "Mulai", "", "kk-skill-icon--shape")
    circles = "".join(
        f'<div class="kk-face"><svg viewBox="0 0 100 100" class="kk-facesvg" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="50" cy="50" r="42" fill="{cr(col)}" fill-opacity=".45" stroke="{C["blueberry"]}" stroke-width="2.6"/>'
        f'</svg><span class="kk-face__label">{lbl}</span></div>'
        for col, lbl in [("sunny", "senang"), ("sky", "sedih"), ("berry", "marah"), ("leaf", "kaget")])
    page("Gambar Wajahnya", "Gambar mata dan mulutnya sesuai perasaan di bawah kotak.",
         f'<div class="kk-facegrid">{circles}</div>',
         "Dua titik dan satu garis sudah cukup. Tujuannya bercerita, bukan menggambar bagus.",
         "Sosial emosional", "smiley-wink", "Lanjut", "kk-badge--lanjut", "kk-skill-icon--shape")


def bagian_9():
    divider(9, "Gunting", "Dua tangan bekerja bersama",
            C["berry"], ["butterfly", "flower", "bird", "apple", "egg", "donut", "animal-bishop-cartoon", "animal-cartoon-fauna", "chipmunk"])
    cut_page("Gunting Sekali Potong", "Potong sekali di setiap garis merah.",
             [("pendek", "apple"), ("pendek", "carrot"), ("pendek", "donut"), ("pendek", "egg"), ("pendek", "corn")],
             "Sekali buka tutup gunting sudah selesai. Mulai dari sini sebelum garis panjang.")
    cut_page("Gunting Garis Lurus", "Gunting mengikuti garis sampai ujung.",
             [("lurus", "fish"), ("lurus", "duck"), ("lurus", "bird"), ("lurus", "cat"), ("lurus", "dog")],
             "Tangan yang tidak memegang gunting ikut bekerja memutar kertas. Itu bagian tersulitnya.")
    cut_page("Gunting Garis Gelombang", "Gunting mengikuti ombaknya.",
             [("gelombang", "dolphin"), ("gelombang", "sailboat"), ("gelombang", "shark"), ("gelombang", "fish2")],
             "Kertas yang diputar, bukan guntingnya. Tunjukkan sekali lalu biarkan mencoba.", badge="Tantangan")
    cut_page("Gunting Zigzag", "Gunting mengikuti gigi gergajinya.",
             [("zigzag", "tiger"), ("zigzag", "crocodile"), ("zigzag", "cactus"), ("zigzag", "giraffe")],
             "Berhenti di setiap sudut, putar kertas, lalu potong lagi. Boleh dibantu.", badge="Tantangan")
    cut_shape_page("Gunting Bentuk Besar", "Gunting mengikuti garis putus-putus.",
                   [("M50 6 L94 50 L50 94 L6 50 Z", "butterfly", "grape"),
                    ("M6 22 H94 V78 H6 Z", "apple", "sunny"),
                    ("M50 8 A42 42 0 1 1 49.5 8 Z", "donut", "sky"),
                    ("M50 8 L92 90 L8 90 Z", "tree", "leaf")],
                   "Bentuk besar dan sudut sedikit dulu. Lingkaran justru paling sulit.")
    cut_shape_page("Gunting Bentuk Lucu", "Gunting mengikuti garis putus-putus.",
                   [("M20 62 A18 18 0 0 1 24 30 A24 24 0 0 1 64 24 A20 20 0 0 1 92 44 A16 16 0 0 1 90 62 Z", "bird", "sky"),
                    ("M50 88 C18 66 8 44 20 30 C32 18 46 24 50 34 C54 24 68 18 80 30 C92 44 82 66 50 88 Z", "flower", "berry"),
                    ("M50 6 L62 38 L96 38 L68 58 L79 90 L50 70 L21 90 L32 58 L4 38 L38 38 Z", "owl", "sunny"),
                    ("M50 10 A40 40 0 1 1 49.6 10 Z", "melon", "leaf")],
                   "Kalau hasilnya sobek, tempel saja di kertas lain. Prosesnya yang dilatih.", badge="Tantangan")
    # kartu gunting
    cards = "".join(
        f'<div class="kk-card">{ic(k, 30)}<span class="kk-card__lbl">{lbl}</span></div>'
        for k, lbl in [("cat", "kucing"), ("dog", "anjing"), ("duck", "bebek"),
                       ("fish", "ikan"), ("frog", "katak"), ("owl", "burung hantu")])
    page("Gunting Jadi Kartu", "Gunting di garis putus-putus. Jadikan kartu untuk main tebak-tebakan.",
         f'<div class="kk-cardgrid">{cards}</div>',
         "Setelah digunting, sebar kartunya dan minta anak mencari satu per satu sesuai nama.",
         "Gunting", "cards", "Tantangan", "kk-badge--tantangan", "kk-skill-icon--cut")
    cards2 = "".join(
        f'<div class="kk-card">{ic(k, 30)}<span class="kk-card__lbl">{lbl}</span></div>'
        for k, lbl in [("apple", "apel"), ("grape", "anggur"), ("carrot", "wortel"),
                       ("corn", "jagung"), ("strawberry", "stroberi"), ("watermelon", "semangka")])
    page("Kartu Buah dan Sayur", "Gunting di garis putus-putus, lalu kelompokkan buah dan sayur.",
         f'<div class="kk-cardgrid">{cards2}</div>',
         "Mengelompokkan lebih berguna daripada menghafal nama. Terima alasan apa pun yang masuk akal bagi anak.",
         "Gunting", "cards", "Tantangan", "kk-badge--tantangan", "kk-skill-icon--cut")
    cards3 = "".join(
        f'<div class="kk-card">{ic(k, 30)}<span class="kk-card__lbl">{lbl}</span></div>'
        for k, lbl in [("airplane", "pesawat"), ("bike", "sepeda"), ("sailboat", "perahu"),
                       ("helicopter", "helikopter"), ("boy", "adik"), ("girl", "kakak")])
    page("Kartu Kendaraan", "Gunting di garis putus-putus, lalu urutkan dari yang paling cepat.",
         f'<div class="kk-cardgrid">{cards3}</div>',
         "Tidak ada jawaban benar untuk urutannya. Yang dilatih kemampuan menjelaskan pilihan.",
         "Gunting", "cards", "Tantangan", "kk-badge--tantangan", "kk-skill-icon--cut")
    cut_page("Gunting dan Tempel", "Gunting garisnya, lalu tempel gambarnya di kertas kosong.",
             [("gelombang", "flower"), ("lurus", "butterfly"), ("zigzag", "ladybug"), ("lurus", "tree")],
             "Lem batang lebih mudah dipegang tangan kecil daripada lem cair.", badge="Tantangan")


def penutup():
    raw_page(f"""<section class="kk-page kk-parent">
  <header class="kk-header">
    <div class="kk-skill-icon">{pico("users-three")}</div>
    <div class="kk-header__top"><h1 class="kk-title">Untuk Orang Tua</h1></div>
  </header>
  <div class="kk-content kk-content--text">
    <p class="kk-body"><b>Lembar ini pelengkap, bukan kurikulum.</b> Anak usia tiga tahun belajar paling banyak
    lewat bermain bebas, bicara, dan menyentuh benda nyata. Gunakan halaman ini sebagai selingan singkat,
    bukan pengganti waktu bermain.</p>
    <p class="kk-body"><b>Lima sampai sepuluh menit sudah cukup.</b> Kalau anak berhenti di tengah, hentikan.
    Halaman yang sama boleh diulang minggu depan. Mengulang justru tanda anak menikmatinya.</p>
    <p class="kk-body"><b>Jangan kejar kerapian.</b> Keluar garis, warna terbalik, dan angka yang dilewati itu
    normal. Yang dilatih di sini kontrol tangan dan rasa mampu, bukan hasil akhir yang bagus.</p>
    <p class="kk-body"><b>Krayon dulu, pensil belakangan.</b> Krayon gemuk dan spidol besar tidak memaksa jari
    menggenggam terlalu kecil. Genggaman tiga jari biasanya matang di usia empat sampai lima tahun.</p>
    <p class="kk-body"><b>Cara menghemat kertas:</b> laminasi halaman favorit atau masukkan ke plastik map,
    lalu pakai spidol whiteboard. Satu halaman bisa dipakai puluhan kali.</p>
    <p class="kk-body"><b>Urutan bagian:</b> garis dan coretan lebih dulu, gunting paling akhir.
    Bagian tengah boleh diacak sesuai minat anak hari itu.</p>
    <div class="kk-parent-note" style="margin-top:auto">
      <span class="kk-parent-note__icon">{pico("warning-circle")}</span>
      <span>Kalau anak menolak berulang kali, simpan dulu bundel ini satu atau dua bulan.
      Menolak bukan tanda tertinggal, hanya tanda belum waktunya.</span>
    </div>
  </div>
  <footer class="kk-footer">
    <span class="kk-logo"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></span>
    <span>Panduan</span><span>{NUM[0] + 1}</span>
  </footer>
</section>""")


# ================================================================ CSS + rakit
CSS = """
  body { margin: 0; background: #E9EAEE; }
  .kk-sprite { position: absolute; width: 0; height: 0; overflow: hidden; }
  .kk-page { margin: 0 auto 8mm; box-shadow: 0 1mm 4mm rgba(0,0,0,.12); }
  .kk-header { align-items: center; }
  .kk-header__top { display: flex; align-items: center; gap: 5mm; flex-wrap: wrap; }
  .kk-content { flex: 1; display: flex; flex-direction: column; }
  .kk-content > .kk-instruction { margin: 0 0 5mm; }
  .kk-activity { flex: 1; display: flex; flex-direction: column; justify-content: space-evenly; }
  .kk-content > .kk-parent-note { margin-top: 6mm; }
  .kk-content--text { gap: 3mm; padding-top: 3mm; }
  .kk-svg { display: block; }
  .kk-center { display: flex; align-items: center; justify-content: center; flex: 1; }
  .kk-ic { display: block; }

  /* garis tracing */
  .kk-trow { display: flex; align-items: center; gap: 4mm; }
  .kk-trow .kk-traceline { flex: 1; height: auto !important; }
  .kk-glyphrow { flex: 1; width: 100%; height: auto; }
  .kk-scene { width: 100%; height: auto; max-height: 150mm; }
  .kk-pico { width: 100%; height: 100%; display: block; }
  .kk-skill-icon .kk-pico { width: 8mm; height: 8mm; }
  .kk-parent-note__icon .kk-pico, .kk-cut-ico .kk-pico { width: 6mm; height: 6mm; }
  .kk-cut-ico { width: 8mm; height: 8mm; color: var(--kk-berry); }
  .kk-cut-ico .kk-pico { width: 8mm; height: 8mm; }
  .kk-gl  { font-family: var(--kk-font-trace); font-size: 44px; font-weight: 400; }
  .kk-gl2 { font-family: var(--kk-font-trace); font-size: 24px; font-weight: 700; fill: var(--kk-ink); }
  .kk-gl3 { font-family: var(--kk-font-title); font-size: 20px; font-weight: 600; fill: var(--kk-blueberry); }

  /* cocokkan */
  .kk-match { flex: 1; display: flex; justify-content: space-between; gap: 26mm; }
  .kk-col { display: flex; flex-direction: column; justify-content: space-evenly; flex: 1; }
  .kk-cell { display: flex; align-items: center; gap: 5mm; min-height: 26mm; }
  .kk-col--r .kk-cell { flex-direction: row; justify-content: flex-end; }
  .kk-col--r .kk-cell { flex-direction: row; }
  .kk-dot { width: 4mm; height: 4mm; border-radius: 50%; background: var(--kk-blueberry); flex: none; }

  /* pilih */
  .kk-choose { display: flex; align-items: center; gap: 5mm; }
  .kk-choose__t { border: 0.6mm solid var(--kk-blueberry); border-radius: 4mm; padding: 3mm; background: var(--kk-tint-blueberry); }
  .kk-choose__bar { width: 0.5mm; align-self: stretch; background: #E3E6EC; }
  .kk-choose__row { flex: 1; display: flex; align-items: center; justify-content: space-evenly; gap: 4mm; }
  .kk-choose__row--wide { justify-content: space-around; }
  .kk-choose__o { display: flex; align-items: center; justify-content: center; }

  /* pola */
  .kk-pattern { display: flex; align-items: center; justify-content: space-between; gap: 4mm; }
  .kk-pattern__seq { display: flex; align-items: center; gap: 2mm; }
  .kk-pcell { display: flex; align-items: center; justify-content: center; width: 24mm; height: 24mm;
              border-radius: 3mm; background: var(--kk-tint-sunny); }
  .kk-pcell:nth-child(even) { background: var(--kk-tint-grape); }
  .kk-pcell--q { background: #fff !important; border: 0.6mm dashed var(--kk-berry);
                 font: 600 22pt/1 var(--kk-font-title); color: var(--kk-berry); }
  .kk-pattern__choices { display: flex; gap: 3mm; border-left: 0.4mm dashed var(--kk-guide-gray);
                         padding-left: 4mm; flex: none; }
  .kk-choice { border: 0.5mm solid var(--kk-guide-gray); border-radius: 3mm; padding: 2.5mm; }

  /* berhitung */
  .kk-group { border: 0.5mm solid #DCE0E8; border-radius: 5mm; padding: 4mm 5mm; background: #FBFCFD;
              display: flex; align-items: center; justify-content: center; min-width: 96mm; }
  .kk-group--half { min-width: 62mm; flex: 1; }
  .kk-count-items { display: flex; gap: 3mm; flex-wrap: wrap; justify-content: center; max-width: 86mm; }
  .kk-count-row { display: flex; align-items: center; justify-content: space-between; gap: 6mm; }
  .kk-boxrow { display: flex; gap: 3mm; }
  .kk-numbox { width: 17mm; height: 17mm; border: 0.5mm solid var(--kk-ink); border-radius: 3mm;
               display: flex; align-items: center; justify-content: center;
               font: 600 20pt/1 var(--kk-font-title); color: var(--kk-ink); }
  .kk-cmrow { display: flex; align-items: center; gap: 6mm; }
  .kk-cmnum { width: 22mm; height: 22mm; flex: none; border: 0.6mm solid var(--kk-leaf); border-radius: 50%;
              display: flex; align-items: center; justify-content: center;
              font: 600 22pt/1 var(--kk-font-title); color: var(--kk-leaf); }
  .kk-more { display: flex; align-items: center; gap: 4mm; }
  .kk-more__vs { font: 600 11pt/1 var(--kk-font-ui); color: var(--kk-text-muted); flex: none; }

  /* cari & warnai */
  .kk-hunt { flex: 1; display: flex; flex-direction: column; gap: 7mm; }
  .kk-hunt__legend { display: flex; gap: 10mm; justify-content: center; }
  .kk-hunt__legend .kk-hunt__c { width: 26mm; }
  .kk-hunt__grid { flex: 1; display: flex; flex-direction: column; justify-content: space-evenly; }
  .kk-hunt__row { display: flex; justify-content: space-evenly; gap: 4mm; }
  .kk-hunt__c { width: 34mm; display: block; }
  .kk-legend { display: flex; gap: 8mm; justify-content: center; margin-top: 3mm; }
  .kk-legend__i { display: flex; align-items: center; gap: 2mm;
                  font: 600 10pt/1 var(--kk-font-ui); color: var(--kk-text); }
  .kk-legend__sw { width: 7mm; height: 7mm; }

  /* jalan */
  .kk-pathwrap { position: relative; flex: 1; display: flex; align-items: center; justify-content: center; }
  .kk-pathwrap__a { position: absolute; left: 2mm; bottom: 12mm; }
  .kk-pathwrap__b { position: absolute; right: 2mm; top: 8mm; }

  /* gunting */
  .kk-cut-strip { display: flex; align-items: center; gap: 5mm; }
  .kk-cut-ico { font-size: 10mm; color: var(--kk-berry); flex: none; }
  .kk-cutline-h { flex: 1; border-top: 3.4mm dashed var(--kk-berry); }
  .kk-cutline-h--short { flex: 0 0 42mm; }
  .kk-facesvg { width: 54mm; height: 54mm; }
  .kk-header__top { flex-wrap: nowrap; }
  .kk-cutsvg { flex: 1; height: 12mm; }
  .kk-cutgrid2 { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 6mm; }
  .kk-cutcell { position: relative; display: flex; align-items: center; justify-content: center; }
  .kk-cutshape { width: 66mm; height: 66mm; }
  .kk-cutcell__ic { position: absolute; right: 6mm; bottom: 2mm; }
  .kk-cardgrid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
  .kk-card { border: 1mm dashed var(--kk-berry); border-radius: 3mm; margin: -0.5mm;
             display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3mm; }
  .kk-card__lbl { font: 600 12pt/1 var(--kk-font-ui); color: var(--kk-text); }

  /* perasaan */
  .kk-facegrid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; place-items: center; gap: 6mm; }
  .kk-face { display: flex; flex-direction: column; align-items: center; gap: 3mm; }
  .kk-face__label { font: 600 13pt/1 var(--kk-font-ui); color: var(--kk-text); }
  .kk-blankface { width: 52mm; height: 52mm; }

  /* pembatas bagian */
  .kk-divider { padding: 0 !important; position: relative; overflow: hidden; }
  .kk-divider__bg { position: absolute; inset: 0; width: 100%; height: 100%; }
  .kk-divider__inner { position: relative; z-index: 1; padding: 34mm 20mm 0; }
  .kk-divider__no { display: inline-block; background: #fff; border-radius: 99px; padding: 2.5mm 6mm;
                    font: 600 11pt/1 var(--kk-font-ui); color: var(--kk-blueberry); }
  .kk-divider__title { font: 600 40pt/1.06 var(--kk-font-title); color: #253154; margin: 6mm 0 0; }
  .kk-divider__sub { font: 600 14pt/1.5 var(--kk-font-ui); color: #3E4A63; margin: 4mm 0 0; max-width: 130mm; }

  /* sampul */
  .kk-cover { padding: 0 !important; position: relative; overflow: hidden; }
  .kk-cover__bg { position: absolute; inset: 0; width: 100%; height: 100%; }
  .kk-cover__inner { position: relative; z-index: 1; display: flex; flex-direction: column;
                     align-items: center; text-align: center; gap: 6mm; padding: 26mm 18mm 0; }
  .kk-logo--big { transform: scale(1.9); margin-bottom: 10mm; }
  .kk-cover__title { font: 600 42pt/1.08 var(--kk-font-title); color: var(--kk-blueberry); margin: 0; }
  .kk-cover__sub { font: 600 14pt/1.5 var(--kk-font-ui); color: #3E4A63; margin: 0; }

  @media print {
    body { background: #fff; }
    .kk-page { margin: 0; box-shadow: none; }
  }
"""


def main():
    cover()
    bagian_1(); bagian_2(); bagian_3(); bagian_4(); bagian_5()
    bagian_6(); bagian_7(); bagian_8(); bagian_9()
    penutup()
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Kertas Kecil - Bundel Usia 3 Tahun</title>
<link rel="stylesheet" href="style.css">
<style>{CSS}</style>
</head>
<body>
{sprite()}
{chr(10).join(PAGES)}
</body>
</html>"""
    Path(__file__).parent.joinpath("worksheet.html").write_text(html)
    print("halaman aktivitas:", NUM[0], "| total section:", len(PAGES))
    unused = sorted(set(FILES) - set(_sym))
    print("aset terpakai:", len(_sym), "dari", len(FILES))
    if unused:
        print("belum terpakai:", ", ".join(unused))


if __name__ == "__main__":
    main()
