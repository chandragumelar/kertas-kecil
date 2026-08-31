#!/usr/bin/env python3
"""Kertas Kecil - generator worksheet printable usia 3 tahun.

Jalankan dari root repo:  python3 gen.py
Lalu periksa luapan:      python3 check.py
"""

import os
import re
import random
from pathlib import Path

ROOT = Path(__file__).parent
SVG_DIR = ROOT / "svg"
ASSET_DIR = ROOT / "assets"
random.seed(11)

# ============================================================ aset SVG
# Alias pendek untuk berkas yang sering dipakai. Berkas lain terdaftar
# otomatis memakai nama filenya, jadi menambah SVG baru cukup menaruhnya
# di folder svg/ tanpa menyentuh berkas ini.
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
    "banana": "banana-svgrepo-com.svg",
    "cherry": "cherry-svgrepo-com.svg",
    "broccoli": "broccoli-svgrepo-com.svg",
    "chilli": "chilli-svgrepo-com.svg",
    "eggplant": "eggplant-svgrepo-com.svg",
    "lettuce": "lettuce-svgrepo-com.svg",
    "cake": "cake-svgrepo-com.svg",
    "pizza": "pizza-svgrepo-com.svg",
    "fries": "fries-svgrepo-com.svg",
    "hotdog": "hot-dog-svgrepo-com.svg",
    "sushi": "sushi-svgrepo-com.svg",
    "juice": "juice-svgrepo-com.svg",
    "car": "car-svgrepo-com.svg",
    "truck": "big-truck-svgrepo-com.svg",
    "rocket": "rocket-svgrepo-com.svg",
    "train": "railway-railway-station-svgrepo-com.svg",
    "skates": "roller-skates-svgrepo-com.svg",
    "stroller": "stroller-svgrepo-com.svg",
    "suitcase": "suitcase-svgrepo-com.svg",
    "monkey": "monkey-svgrepo-com.svg",
    "pig": "pig-svgrepo-com.svg",
    "mouse": "mouse-svgrepo-com.svg",
    "rabbit": "rabbit-svgrepo-com.svg",
    "snake": "snake-svgrepo-com.svg",
    "dinosaur": "dinosaur-svgrepo-com.svg",
    "rooster": "rooster-svgrepo-com.svg",
    "goat": "mianyang-svgrepo-com.svg",
    "boar": "wild-boar-svgrepo-com.svg",
    "chameleon": "chameleon-svgrepo-com.svg",
    "macaw": "macaw-svgrepo-com.svg",
    "crab": "crab-svgrepo-com.svg",
    "octopus": "octopus-svgrepo-com.svg",
    "shrimp": "shrimp-svgrepo-com.svg",
    "whale": "whale-svgrepo-com.svg",
    "sun": "sun-nature-sunny-svgrepo-com.svg",
    "rain": "rain-svgrepo-com.svg",
    "rainbow": "nature-rainbow-svgrepo-com.svg",
    "sunrise": "sunrise-over-mountains-svgrepo-com.svg",
    "forest": "forest-svgrepo-com.svg",
    "leaf": "botanical-nature-plant-leaf-garden-13-svgrepo-com.svg",
    "park": "ecology-green-park-svgrepo-com.svg",
    "fire": "fire-svgrepo-com.svg",
    "hat": "hat-svgrepo-com.svg",
    "glasses": "glasses-svgrepo-com.svg",
    "cup": "water-cup-svgrepo-com.svg",
    "pot": "pot-svgrepo-com.svg",
    "knife": "kitchen-knife-svgrepo-com.svg",
    "comb": "comb-svgrepo-com.svg",
    "toothbrush": "toothbrush-svgrepo-com.svg",
    "camera": "camera-svgrepo-com.svg",
    "headphone": "headphone-svgrepo-com.svg",
    "bulb": "light-bulb-svgrepo-com.svg",
    "pencil2": "pencil-svgrepo-com.svg",
    "ruler": "straight-ruler-svgrepo-com.svg",
    "hammer": "hammer-svgrepo-com.svg",
    "spanner": "spanner-svgrepo-com.svg",
    "key": "key-part-2-svgrepo-com.svg",
    "scissors2": "scissors-part-2-svgrepo-com.svg",
    "umbrella2": "umbrella-part-3-svgrepo-com.svg",
    "shuttlecock": "badminton-shuttlecock-svgrepo-com.svg",
    "drumkit": "drum-kit-svgrepo-com.svg",
    "bottle": "feeding-bottle-svgrepo-com.svg",
    "child": "child-svgrepo-com.svg",
}

# Pengelompokan untuk svg/INDEX.md. Kunci yang belum terdaftar masuk ke
# "lainnya", jadi dict ini tidak wajib diperbarui setiap menambah berkas.
KATEGORI = {
    "hewan darat": ["cat", "cat2", "dog", "dog2", "bunny", "deer", "squirrel", "squirrel-1",
                    "squirrel-animal", "chipmunk", "elephant", "elephant2", "giraffe", "tiger",
                    "crocodile", "crocodile-animal", "camel", "kangaroo", "kangaroo-animal",
                    "animal-bishop-cartoon", "animal-cartoon-fauna", "animal-domestic-pet-7",
                    "animal-domestic-pet-11", "animal-domestic-pet-15", "monkey", "pig",
                    "mouse", "rabbit", "snake", "dinosaur", "goat", "boar", "chameleon"],
    "burung": ["bird", "bird-1", "owl", "duck", "flamingo", "pelican", "rooster", "macaw",
               "bird-hand-drawn-toy-animal"],
    "serangga": ["butterfly", "ladybug", "animal-bug-domestic", "animal-butterflies-domestic"],
    "laut": ["fish", "fish2", "dolphin", "shark", "frog", "crab", "octopus", "shrimp",
             "whale"],
    "buah dan sayur": ["apple", "apple2", "grape", "strawberry", "watermelon", "melon",
                       "avocado", "pineapple", "corn", "carrot", "banana", "cherry",
                       "broccoli", "chilli", "eggplant", "lettuce"],
    "makanan": ["donut", "egg", "burger", "icecream", "drumstick", "cake", "pizza",
                "fries", "hotdog", "sushi", "juice"],
    "kendaraan": ["airplane", "airplane-1", "bike", "helicopter", "sailboat", "car",
                  "truck", "rocket", "train", "skates", "stroller", "suitcase"],
    "orang": ["boy", "girl", "avatar-boy-1", "avatar-girl", "avatar-girl-1",
              "cartoon-child-girl", "boy-brother-cartoon", "child"],
    "wajah": ["happy", "unhappy", "crying", "grinning", "emotion-happy-1", "emotion-unhappy-1"],
    "alam dan cuaca": ["tree", "flower", "cactus", "umbrella", "umbrella2", "sun", "rain",
                       "rainbow", "sunrise", "forest", "leaf", "park", "fire"],
    "benda": ["guitar", "drum", "drumkit", "small", "small-1", "camouflage", "hat",
              "glasses", "cup", "pot", "knife", "comb", "toothbrush", "camera",
              "headphone", "bulb", "pencil2", "ruler", "hammer", "spanner", "key",
              "scissors2", "shuttlecock", "bottle"],
}


def _autoregister():
    dipakai = set(FILES.values())
    for f in sorted(os.listdir(SVG_DIR)):
        if not f.endswith(".svg") or f in dipakai:
            continue
        key = f[:-4].replace("-svgrepo-com", "").strip()
        key = re.sub(r"[()]", "", key).replace(" ", "-").strip("-")
        FILES.setdefault(key, f)


_autoregister()
_sym = {}
PAKAI = {}


def _catat(key):
    PAKAI[key] = PAKAI.get(key, 0) + 1


def _load(key):
    raw = (SVG_DIR / FILES[key]).read_text()
    vb = re.search(r'viewBox="([^"]+)"', raw).group(1)
    inner = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")]
    return vb, re.sub(r"<!--.*?-->", "", inner, flags=re.S).strip()


def reg(*keys):
    for k in keys:
        if k not in _sym:
            _sym[k] = _load(k)


def ic(key, mm, style=""):
    reg(key)
    _catat(key)
    return (f'<svg class="kk-ic" viewBox="0 0 100 100" '
            f'style="width:{mm}mm;height:{mm}mm;flex:none;{style}">'
            f'<use href="#a-{key}" width="100" height="100"/></svg>')


def use(key, x, y, sz):
    reg(key)
    _catat(key)
    return (f'<g transform="translate({x - sz / 2} {y - sz / 2})">'
            f'<use href="#a-{key}" width="{sz}" height="{sz}"/></g>')


def _kaya_warna(key):
    """Jumlah warna berbeda di sebuah aset. Dipakai untuk menjaga agar semua
    gambar di dalam bundel bergaya sama, yaitu berwarna penuh, bukan line art."""
    t = (SVG_DIR / FILES[key]).read_text()
    c = set(x.lower() for x in re.findall(r"#[0-9a-fA-F]{6}", t))
    c |= set(x.lower() for x in re.findall(r"#[0-9a-fA-F]{3}\b", t))
    return len(c - {"#fff", "#ffffff", "#000", "#000000", "#231f20", "#010101"})


def tulis_index():
    milik = {v: k for k, vs in KATEGORI.items() for v in vs}
    grup = {k: [] for k in KATEGORI}
    grup["lainnya"] = []
    for key in sorted(FILES):
        grup[milik.get(key, "lainnya")].append(key)
    out = ["# Daftar aset SVG", "",
           "Berkas ini ditulis ulang otomatis oleh `gen.py`. Jangan diedit manual.", "",
           f"Total {len(FILES)} berkas, {len(_sym)} terpakai di bundel saat ini.",
           'Pakai kuncinya di generator, misalnya `ic("apple", 24)`.', ""]
    for kat, keys in grup.items():
        if not keys:
            continue
        out += [f"## {kat} ({len(keys)})", ""]
        out += [f"- `{k}`" + ("" if k in _sym else "  — belum terpakai") for k in keys]
        out.append("")
    (SVG_DIR / "INDEX.md").write_text("\n".join(out))


# ============================================================ warna
C = {
    "blueberry": "#3D5A98",
    "leaf": "#4E9E52",
    "sunny": "#EFB63C",
    "berry": "#E05580",
    "grape": "#7C6BC4",
    "sky": "#3FA9D4",
    "orange": "#EA8535",
}


def crayon_pattern(name, hexv):
    sapuan = [(0.6, 2.1, .72), (3.4, .7, .30), (5.0, 1.3, .55), (7.8, 2.6, .80),
              (11.2, .6, .22), (12.8, 1.7, .60), (15.4, .9, .38), (17.0, .5, .20)]
    garis = "".join(f'<rect x="{x}" y="-2" width="{w}" height="24" fill="#fff" opacity="{o}"/>'
                    for x, w, o in sapuan)
    return (f'<pattern id="cr-{name}" width="18" height="18" patternUnits="userSpaceOnUse" '
            f'patternTransform="rotate(38)"><rect width="18" height="18" fill="{hexv}"/>'
            f'{garis}</pattern>')


def cr(name):
    return f"url(#cr-{name})"


def sprite():
    out = ['<svg class="kk-sprite" aria-hidden="true"><defs>']
    out += [crayon_pattern(k, v) for k, v in C.items()]
    out.append("</defs>")
    out += [f'<symbol id="a-{k}" viewBox="{vb}" overflow="hidden" '
            f'preserveAspectRatio="xMidYMid meet">{inner}</symbol>'
            for k, (vb, inner) in sorted(_sym.items())]
    out.append("</svg>")
    return "\n".join(out)


# ============================================================ ikon inline
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
    "book": '<path d="M4 6 H12 A2 2 0 0 1 14 8 V23 A2 2 0 0 0 12 21 H4 Z M24 6 H16 A2 2 0 0 0 14 8 V23 A2 2 0 0 1 16 21 H24 Z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
}
_ALIAS = {"scribble-loop": "squiggle", "path": "squiggle", "flow-arrow": "arrows",
          "pencil-simple": "pencil", "puzzle-piece": "shapes", "magnifying-glass": "shapes",
          "x-circle": "shapes", "resize": "shapes", "number-circle-three": "num",
          "scales": "num", "palette": "brush", "paint-brush": "brush", "scissors": "scissors",
          "cards": "cards", "smiley": "smiley", "smiley-wink": "smiley", "users-three": "people",
          "lightbulb": "bulb", "warning-circle": "bulb", "book": "book"}


def pico(name):
    return f'<svg class="kk-pico" viewBox="0 0 28 28">{_ICON[_ALIAS.get(name, "shapes")]}</svg>'


# ============================================================ rangka halaman
PAGES = []
TOC = []
NUM = [0]

BADGE_CLS = {"Lanjut": "kk-badge--lanjut", "Tantangan": "kk-badge--tantangan"}


def page(title, instruction, body, note, skill, icon, badge="Mulai", icon_cls=""):
    NUM[0] += 1
    PAGES.append(f"""<section class="kk-page">
  <header class="kk-header">
    <div class="kk-skill-icon {icon_cls}">{pico(icon)}</div>
    <div class="kk-header__top"><h1 class="kk-title">{title}</h1>
      <span class="kk-badge {BADGE_CLS.get(badge, '')}">{badge}</span></div>
  </header>
  <div class="kk-content">
    <p class="kk-instruction">{instruction}</p>
    <div class="kk-activity">{body}</div>
    <div class="kk-parent-note">
      <span class="kk-parent-note__icon">{pico("lightbulb")}</span><span>{note}</span>
    </div>
  </div>
  <footer class="kk-footer">
    <span class="kk-logo"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></span>
    <span>{skill}</span><span>{NUM[0]}</span>
  </footer>
</section>""")


def raw_page(html, hitung=True):
    if hitung:
        NUM[0] += 1
    PAGES.append(html)


def gambar_penuh(nama, kelas=""):
    raw_page(f'<section class="kk-page kk-fullpage {kelas}">'
             f'<img src="assets/{nama}" class="kk-fullpage__img" alt=""></section>',
             hitung=False)


def divider(no, judul):
    TOC.append((judul, NUM[0] + 1, no))
    gambar_penuh(f"bagian_{no}.jpeg")


LABEL_CONTOH = '<span class="kk-contoh">contoh</span>'


def tag_side(pertama):
    """Label contoh dengan lebar tetap supaya baris lain tidak bergeser."""
    isi = LABEL_CONTOH if pertama else ""
    return f'<span class="kk-contoh-tag--side">{isi}</span>'


# ============================================================ menelusuri garis
def stroke_row(d, start, w, h, reps, color, contoh=True):
    """Satu baris jejak. Pengulangan pertama ditampilkan sudah ditelusuri."""
    bag = []
    for i in range(reps):
        dx = i * w
        bag.append(f'<g transform="translate({dx} 0)">')
        bag.append(f'<path d="{d}" fill="none" stroke="{C[color]}2E" stroke-width="13" '
                   f'stroke-linecap="round" stroke-linejoin="round"/>')
        if i == 0 and contoh:
            bag.append(f'<path d="{d}" fill="none" stroke="{C[color]}" stroke-width="3.4" '
                       f'stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            bag.append(f'<path d="{d}" fill="none" stroke="#fff" stroke-width="1" '
                       f'stroke-dasharray="3.4 3.4" stroke-linecap="round"/>')
        bag.append(f'<circle cx="{start[0]}" cy="{start[1]}" r="4.4" fill="{C["leaf"]}"/>'
                   f'<circle cx="{start[0]}" cy="{start[1]}" r="1.8" fill="#fff"/>')
        bag.append("</g>")
    return (f'<svg class="kk-svg kk-traceline" viewBox="0 0 {w * reps} {h}">'
            f'{"".join(bag)}</svg>')


def trace_page(title, instr, d, note, deco, start, w=58, h=44, reps=3, badge="Mulai"):
    baris = []
    for i in range(3):
        ikon = ic(deco[i % len(deco)], 20)
        garis = stroke_row(d, start, w, h, reps, ["grape", "sky", "orange"][i], contoh=(i == 0))
        tanda = f'<span class="kk-contoh-tag">{LABEL_CONTOH}</span>' if i == 0 else ""
        sisi = f"{ikon}{garis}" if i % 2 == 0 else f"{garis}{ikon}"
        baris.append(f'<div class="kk-trow">{tanda}{sisi}</div>')
    page(title, instr, "".join(baris), note, "Motorik halus", "scribble-loop", badge)


# ============================================================ menelusuri angka & huruf
# Jejak satu garis di tengah huruf, bukan garis luar ganda, supaya anak
# menarik satu goresan saja seperti waktu menulis sungguhan.
GLYPH = {
    "1": "M12 18 L20 11 V52",
    "2": "M10 19 Q11 11 20 11 Q29 11 29 20 Q29 28 11 52 H31",
    "3": "M11 16 Q13 11 20 11 Q28 11 28 19 Q28 27 19 28 Q29 29 29 39 Q29 52 19 52 Q12 52 10 46",
    "4": "M24 11 L8 38 H32 M24 11 V52",
    "5": "M29 11 H14 L12 29 Q15 26 21 26 Q30 26 30 39 Q30 52 20 52 Q13 52 11 47",
    "6": "M27 13 Q14 15 12 32 Q11 52 20 52 Q29 52 29 41 Q29 31 20 31 Q13 31 12 37",
    "7": "M9 11 H31 L17 52",
    "8": "M20 11 Q11 11 11 19 Q11 27 20 30 Q30 33 30 42 Q30 52 20 52 Q10 52 10 42 Q10 33 20 30 Q29 27 29 19 Q29 11 20 11",
    "9": "M28 31 Q28 41 19 41 Q10 41 10 30 Q10 19 20 19 Q29 19 29 31 Q29 45 14 51",
    "0": "M20 11 Q29 11 29 31 Q29 52 20 52 Q11 52 11 31 Q11 11 20 11",
    "a": "M29 34 Q25 29 19 29 Q11 29 11 40 Q11 52 19 52 Q26 52 29 47 M29 29 V52",
    "b": "M11 10 V52 M11 41 Q11 29 20 29 Q29 29 29 40 Q29 52 20 52 Q11 52 11 42",
    "c": "M29 34 Q25 29 19 29 Q11 29 11 40 Q11 52 19 52 Q25 52 29 47",
    "d": "M29 10 V52 M29 41 Q29 29 20 29 Q11 29 11 40 Q11 52 20 52 Q29 52 29 42",
    "e": "M11 40 H28 Q28 29 19 29 Q11 29 11 40 Q11 52 20 52 Q26 52 29 48",
    "f": "M28 13 Q19 10 19 20 V52 M12 30 H27",
    "g": "M29 34 Q25 29 19 29 Q11 29 11 40 Q11 51 19 51 Q26 51 29 46 "
         "M29 29 V60 Q29 68 20 68 Q13 68 11 63",
    "h": "M11 10 V52 M11 41 Q11 29 20 29 Q29 29 29 40 V52",
    "i": "M20 29 V52 M20 18 a2.4 2.4 0 1 1 0.01 0",
}
MULAI = {  # titik awal goresan
    "1": (12, 18), "2": (10, 19), "3": (11, 16), "4": (24, 11), "5": (29, 11), "6": (27, 13),
    "7": (9, 11), "8": (20, 11), "9": (28, 31), "0": (20, 11),
    "a": (29, 34), "b": (11, 10), "c": (29, 34), "d": (29, 10), "e": (11, 40), "f": (28, 13),
    "g": (29, 34), "h": (11, 10), "i": (20, 29),
}


def glyph_row(ch, reps, color):
    cw, H = 46, 74
    W = cw * (reps + 1)
    g = [f'<line x1="0" y1="9" x2="{W}" y2="9" stroke="#C9CEDA" stroke-width="0.9"/>',
         f'<line x1="0" y1="30" x2="{W}" y2="30" stroke="#C9CEDA" stroke-width="0.9" stroke-dasharray="6 5"/>',
         f'<line x1="0" y1="52" x2="{W}" y2="52" stroke="{C["berry"]}" stroke-width="1.1"/>']
    d, m = GLYPH[ch], MULAI[ch]
    for i in range(reps + 1):
        dx = cw * i + 3
        g.append(f'<g transform="translate({dx} 0)">')
        if i == 0:
            g.append(f'<path d="{d}" fill="none" stroke="{C[color]}" stroke-width="4.6" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            g.append(f'<path d="{d}" fill="none" stroke="#A7AEBD" stroke-width="2.4" '
                     f'stroke-dasharray="5 4.6" stroke-linecap="round" stroke-linejoin="round"/>')
            g.append(f'<circle cx="{m[0]}" cy="{m[1]}" r="3.2" fill="{C["leaf"]}"/>')
        g.append("</g>")
    return f'<svg class="kk-svg kk-glyphrow" viewBox="0 0 {W} {H}">{"".join(g)}</svg>'


def glyph_page(title, instr, chars, note, skill, deco, badge="Lanjut", reps=4):
    baris = []
    for i, ch in enumerate(chars):
        tanda = f'<span class="kk-contoh-tag">{LABEL_CONTOH}</span>' if i == 0 else ""
        baris.append(f'<div class="kk-trow">{tanda}'
                     f'{glyph_row(ch, reps, ["sky", "berry", "grape"][i % 3])}'
                     f'{ic(deco[i % len(deco)], 17)}</div>')
    page(title, instr, "".join(baris), note, skill, "pencil-simple", badge)



def _acak_selain_pertama(n):
    """Urutan kanan: baris pertama tetap sejajar (contoh), sisanya diacak
    sampai tidak ada yang kebetulan sejajar dengan kirinya."""
    sisa = list(range(1, n))
    for _ in range(200):
        random.shuffle(sisa)
        if all(i != v for i, v in zip(range(1, n), sisa)):
            break
    return [0] + sisa


# ============================================================ mencocokkan
def match_page(title, instr, pairs, note, skill="Cocokkan", badge="Mulai"):
    """Pasangan pertama sudah tersambung sebagai contoh."""
    kiri = [p[0] for p in pairs]
    kanan = [p[1] for p in pairs]
    urut = _acak_selain_pertama(len(kanan))
    rows = []
    for i, k in enumerate(kiri):
        rows.append(f'<div class="kk-mrow"><div class="kk-mcell">{ic(k, 24)}'
                    f'<span class="kk-dot"></span></div>'
                    f'<div class="kk-mgap">'
                    + (f'<svg class="kk-mline" viewBox="0 0 100 20" preserveAspectRatio="none">'
                       f'<path d="M2 10 H98" fill="none" stroke="{C["blueberry"]}" '
                       f'stroke-width="1.6" stroke-dasharray="5 4"/></svg>{LABEL_CONTOH}'
                       if i == 0 else "")
                    + f'</div>'
                    f'<div class="kk-mcell kk-mcell--r"><span class="kk-dot"></span>'
                    f'{ic(kanan[urut[i]], 24)}</div></div>')
    page(title, instr, "".join(rows), note, skill, "puzzle-piece", badge, "kk-skill-icon--shape")


def choose_page(title, instr, rows, note, skill, icon, badge="Lanjut", tandai="lingkari"):
    """Baris pertama sudah dijawab sebagai contoh."""
    out = []
    for i, (target, opts, jawab) in enumerate(rows):
        kepala = (f'<div class="kk-choose__t">{ic(target, 22)}</div>'
                  f'<span class="kk-choose__bar"></span>') if target else ""
        sel = []
        for j, k in enumerate(opts):
            mark = ""
            if i == 0 and j == jawab:
                mark = (f'<svg class="kk-mark" viewBox="0 0 100 100">'
                        f'<ellipse cx="50" cy="50" rx="45" ry="43" fill="none" '
                        f'stroke="{C["berry"]}" stroke-width="4" '
                        f'transform="rotate(-6 50 50)"/></svg>'
                        if tandai == "lingkari" else
                        f'<svg class="kk-mark" viewBox="0 0 100 100">'
                        f'<path d="M18 20 L82 80 M82 20 L18 80" stroke="{C["berry"]}" '
                        f'stroke-width="5" stroke-linecap="round" fill="none"/></svg>')
            sel.append(f'<span class="kk-choose__o">{ic(k, 22)}{mark}</span>')
        tag = tag_side(i == 0)
        out.append(f'<div class="kk-choose">{kepala}'
                   f'<div class="kk-choose__row">{"".join(sel)}</div>{tag}</div>')
    page(title, instr, "".join(out), note, skill, icon, badge, "kk-skill-icon--shape")


def size_page(title, instr, rows, note, cari="kecil"):
    """rows: (kunci, urutan ukuran). Yang dilingkari sebagai contoh adalah
    yang paling kecil atau paling besar sesuai argumen `cari`."""
    out = []
    for i, (key, ukuran) in enumerate(rows):
        target = min(ukuran) if cari == "kecil" else max(ukuran)
        sel = []
        for u in ukuran:
            mark = ""
            if i == 0 and u == target:
                mark = (f'<svg class="kk-mark" viewBox="0 0 100 100"><ellipse cx="50" cy="50" '
                        f'rx="46" ry="44" fill="none" stroke="{C["berry"]}" stroke-width="5" '
                        f'transform="rotate(-5 50 50)"/></svg>')
            sel.append(f'<span class="kk-choose__o">{ic(key, u)}{mark}</span>')
        out.append(f'<div class="kk-choose"><div class="kk-choose__row kk-choose__row--wide">'
                   f'{"".join(sel)}</div>{tag_side(i == 0)}</div>')
    page(title, instr, "".join(out), note, "Bentuk", "resize", "Lanjut", "kk-skill-icon--shape")


# ============================================================ pola
def _pola_halaman(title, instr, baris, note, badge="Lanjut"):
    """baris: list (sel_html, jawaban_html). Kotak kosong di ujung deret,
    jawaban berjajar di kolom kanan dengan urutan diacak, anak menarik garis."""
    jawab = [j for _, j in baris]
    urut = _acak_selain_pertama(len(baris))
    rows = []
    for i, (sel, _) in enumerate(baris):
        if i == 0:
            kotak = f'<span class="kk-pcell kk-pcell--q kk-pcell--isi">{jawab[0]}</span>'
            garis = (f'<svg class="kk-mline" viewBox="0 0 100 20" preserveAspectRatio="none">'
                     f'<path d="M2 10 H98" fill="none" stroke="{C["blueberry"]}" '
                     f'stroke-width="1.6" stroke-dasharray="5 4"/></svg>{LABEL_CONTOH}')
        else:
            kotak = '<span class="kk-pcell kk-pcell--q">?</span>'
            garis = ""
        rows.append(f'<div class="kk-prow">'
                    f'<div class="kk-pseq">{sel}<span class="kk-dot"></span></div>'
                    f'<div class="kk-mgap">{garis}</div>'
                    f'<div class="kk-mcell kk-mcell--r"><span class="kk-dot"></span>'
                    f'<span class="kk-pans">{jawab[urut[i]]}</span></div></div>')
    page(title, instr, "".join(rows), note, "Pola", "flow-arrow", badge, "kk-skill-icon--shape")


def _sel(isi, kosong=False, polos=False):
    kelas = "kk-pcell kk-pcell--q" if kosong else (
        "kk-pcell kk-pcell--polos" if polos else "kk-pcell")
    return f'<span class="{kelas}">{isi}</span>'


def pattern_page(title, instr, seqs, note, badge="Lanjut"):
    """Pola dari gambar, misalnya apel anggur apel anggur."""
    baris = []
    for keys, jawab in seqs:
        sel = "".join(_sel(ic(k, 15)) for k in keys) + _sel("?", kosong=True)
        baris.append((sel, ic(jawab, 15)))
    _pola_halaman(title, instr, baris, note, badge)


def _kotak_warna(nama, mm=17):
    return (f'<svg viewBox="0 0 40 40" style="width:{mm}mm;height:{mm}mm">'
            f'<rect x="2" y="2" width="36" height="36" rx="5" fill="{cr(nama)}" '
            f'stroke="{C["blueberry"]}" stroke-width="1.4"/></svg>')


def pattern_color_page(title, instr, seqs, note, badge="Lanjut"):
    """Pola dari warna saja, tanpa gambar apa pun."""
    baris = []
    for warna, jawab in seqs:
        sel = "".join(_sel(_kotak_warna(w), polos=True) for w in warna) + _sel("?", kosong=True)
        baris.append((sel, _kotak_warna(jawab)))
    _pola_halaman(title, instr, baris, note, badge)


BENTUK = {
    "lingkaran": '<circle cx="20" cy="20" r="17" fill="{f}" stroke="{s}" stroke-width="1.6"/>',
    "kotak": '<rect x="4" y="4" width="32" height="32" rx="3" fill="{f}" stroke="{s}" stroke-width="1.6"/>',
    "segitiga": '<path d="M20 3 L37 35 H3 Z" fill="{f}" stroke="{s}" stroke-width="1.6" stroke-linejoin="round"/>',
    "hati": ('<path d="M20 35 C4 24 3 13 10 8 C15 4 19 8 20 12 C21 8 25 4 30 8 '
             'C37 13 36 24 20 35 Z" fill="{f}" stroke="{s}" stroke-width="1.6" stroke-linejoin="round"/>'),
}


def _kotak_bentuk(nama, warna, mm=17):
    d = BENTUK[nama].format(f=cr(warna), s=C["blueberry"])
    return f'<svg viewBox="0 0 40 40" style="width:{mm}mm;height:{mm}mm">{d}</svg>'


def pattern_shape_page(title, instr, seqs, note, badge="Lanjut"):
    """Pola dari bentuk dasar, warnanya sama semua supaya yang dibaca bentuknya."""
    baris = []
    for bentuk, warna, jawab in seqs:
        sel = "".join(_sel(_kotak_bentuk(b, warna), polos=True) for b in bentuk) + _sel("?", kosong=True)
        baris.append((sel, _kotak_bentuk(jawab, warna)))
    _pola_halaman(title, instr, baris, note, badge)


def pattern_size_page(title, instr, seqs, note, badge="Lanjut"):
    """Pola dari ukuran benda yang sama, besar kecil besar kecil."""
    baris = []
    for key, ukuran, jawab in seqs:
        sel = "".join(_sel(ic(key, u)) for u in ukuran) + _sel("?", kosong=True)
        baris.append((sel, ic(key, jawab)))
    _pola_halaman(title, instr, baris, note, badge)


# ============================================================ berhitung
def count_page(title, instr, groups, note, badge="Lanjut"):
    rows = []
    for i, (key, n, opts) in enumerate(groups):
        items = "".join(ic(key, 16) for _ in range(n))
        kotak = []
        for o in opts:
            mark = ""
            if i == 0 and o == n:
                mark = (f'<svg class="kk-mark" viewBox="0 0 100 100"><ellipse cx="50" cy="50" '
                        f'rx="46" ry="44" fill="none" stroke="{C["berry"]}" stroke-width="5" '
                        f'transform="rotate(-6 50 50)"/></svg>')
            kotak.append(f'<span class="kk-numbox">{o}{mark}</span>')
        tag = tag_side(i == 0)
        rows.append(f'<div class="kk-count-row"><div class="kk-group">'
                    f'<div class="kk-count-items">{items}</div></div>'
                    f'<div class="kk-boxrow">{"".join(kotak)}</div>{tag}</div>')
    page(title, instr, "".join(rows), note, "Berhitung", "number-circle-three", badge,
         "kk-skill-icon--count")


def count_match_page(title, instr, rows, note, badge="Tantangan"):
    urut = _acak_selain_pertama(len(rows))
    out = []
    for i, (key, n) in enumerate(rows):
        items = "".join(ic(key, 15) for _ in range(n))
        angka = rows[urut[i]][1]
        garis = (f'<svg class="kk-mline" viewBox="0 0 100 20" preserveAspectRatio="none">'
                 f'<path d="M2 10 H98" fill="none" stroke="{C["blueberry"]}" stroke-width="1.6" '
                 f'stroke-dasharray="5 4"/></svg>{LABEL_CONTOH}' if i == 0 else "")
        out.append(f'<div class="kk-mrow"><div class="kk-mcell"><div class="kk-group">'
                   f'<div class="kk-count-items">{items}</div></div>'
                   f'<span class="kk-dot"></span></div>'
                   f'<div class="kk-mgap">{garis}</div>'
                   f'<div class="kk-mcell kk-mcell--r"><span class="kk-dot"></span>'
                   f'<span class="kk-cmnum">{angka}</span></div></div>')
    page(title, instr, "".join(out), note, "Berhitung", "number-circle-three", badge,
         "kk-skill-icon--count")


def more_page(title, instr, rows, note, badge="Tantangan", cari="banyak"):
    out = []
    for i, (key, a, b) in enumerate(rows):
        kiri = "".join(ic(key, 14) for _ in range(a))
        kanan = "".join(ic(key, 14) for _ in range(b))
        mark = (f'<svg class="kk-mark kk-mark--wide" viewBox="0 0 200 100"><ellipse cx="100" '
                f'cy="50" rx="96" ry="46" fill="none" stroke="{C["berry"]}" stroke-width="4"/>'
                f'</svg>')
        menang_kiri = a > b if cari == "banyak" else a < b
        m_kiri = mark if (i == 0 and menang_kiri) else ""
        m_kanan = mark if (i == 0 and not menang_kiri) else ""
        tag = tag_side(i == 0)
        out.append(f'<div class="kk-more">'
                   f'<div class="kk-group kk-group--half"><div class="kk-count-items">{kiri}</div>{m_kiri}</div>'
                   f'<span class="kk-more__vs">atau</span>'
                   f'<div class="kk-group kk-group--half"><div class="kk-count-items">{kanan}</div>{m_kanan}</div>'
                   f'{tag}</div>')
    page(title, instr, "".join(out), note, "Berhitung", "scales", badge, "kk-skill-icon--count")


# ============================================================ cari & warnai
def hunt_page(title, instr, legend, grid, note, shape="box", badge="Mulai"):
    def sel(ch, color, besar=False):
        s = 46 if besar else 40
        isi = cr(color) if color else "none"
        if shape == "drop":
            d = (f"M{s / 2} 3 C{s * .92} {s * .42} {s * .84} {s} {s / 2} {s} "
                 f"C{s * .16} {s} {s * .08} {s * .42} {s / 2} 3 Z")
            bentuk = f'<path d="{d}" fill="{isi}" stroke="{C["blueberry"]}" stroke-width="1.2"/>'
        else:
            bentuk = (f'<rect x="1.5" y="1.5" width="{s - 3}" height="{s - 3}" rx="4" '
                      f'fill="{isi}" stroke="{C["blueberry"]}" stroke-width="1.2"/>')
        return (f'<svg viewBox="0 0 {s} {s + 2}" class="kk-hunt__c">{bentuk}'
                f'<text x="{s / 2}" y="{s * .70}" text-anchor="middle" class="kk-gl2">{ch}</text></svg>')

    leg = "".join(sel(ch, col, True) for ch, col in legend)
    baris = "".join('<div class="kk-hunt__row">' + "".join(sel(ch, col) for ch, col in row) + "</div>"
                    for row in grid)
    body = (f'<div class="kk-hunt"><div class="kk-hunt__legend">'
            f'<span class="kk-hunt__legendlbl">warna contoh</span>{leg}</div>'
            f'<div class="kk-hunt__grid">{baris}</div></div>')
    page(title, instr, body, note, "Warna", "palette", badge, "kk-skill-icon--color")


# ============================================================ jalan berliku
def path_page(title, instr, d, awal, akhir, note, start_xy, end_xy, deco=(), badge="Lanjut"):
    contoh_len = 26
    art = (f'<svg class="kk-svg kk-scene" viewBox="0 0 200 240">'
           f'<path d="{d}" fill="none" stroke="{C["sunny"]}4D" stroke-width="16" '
           f'stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="{d}" fill="none" stroke="#fff" stroke-width="1" stroke-dasharray="4 4" '
           f'stroke-linecap="round"/>'
           f'<path d="{d}" fill="none" stroke="{C["grape"]}" stroke-width="3" '
           f'stroke-linecap="round" stroke-dasharray="{contoh_len} 4000"/>'
           + "".join(use(k, x, y, s) for k, x, y, s in deco)
           + use(awal, *start_xy, 24) + use(akhir, *end_xy, 24)
           + f'<text x="{start_xy[0] + 16}" y="{start_xy[1] - 15}" class="kk-svgtag">contoh</text>'
           + "</svg>")
    page(title, instr, f'<div class="kk-center">{art}</div>', note, "Motorik halus", "path", badge)


# ============================================================ perasaan
def face_svg(kind, color, isi=True):
    B = C["blueberry"]
    g = [f'<circle cx="50" cy="50" r="42" fill="{cr(color) if isi else "none"}" '
         f'fill-opacity="{0.6 if isi else 1}" stroke="{B}" stroke-width="2.8"/>']
    if kind == "senang":
        g += [f'<path d="M30 40 Q35 33 40 40" fill="none" stroke="{B}" stroke-width="3.2" stroke-linecap="round"/>',
              f'<path d="M60 40 Q65 33 70 40" fill="none" stroke="{B}" stroke-width="3.2" stroke-linecap="round"/>',
              f'<path d="M32 60 Q50 76 68 60" fill="none" stroke="{B}" stroke-width="3.2" stroke-linecap="round"/>']
    elif kind == "sedih":
        g += [f'<circle cx="36" cy="42" r="3.6" fill="{B}"/><circle cx="64" cy="42" r="3.6" fill="{B}"/>',
              f'<path d="M32 70 Q50 56 68 70" fill="none" stroke="{B}" stroke-width="3.2" stroke-linecap="round"/>',
              f'<path d="M36 49 Q31 58 36 62 Q41 58 36 49 Z" fill="none" stroke="{B}" stroke-width="2.4"/>']
    elif kind == "marah":
        g += [f'<path d="M28 36 L42 42 M72 36 L58 42" fill="none" stroke="{B}" stroke-width="3.2" stroke-linecap="round"/>',
              f'<circle cx="36" cy="48" r="3.6" fill="{B}"/><circle cx="64" cy="48" r="3.6" fill="{B}"/>',
              f'<path d="M34 68 H66" fill="none" stroke="{B}" stroke-width="3.2" stroke-linecap="round"/>']
    else:
        g += [f'<circle cx="36" cy="42" r="5.2" fill="none" stroke="{B}" stroke-width="2.8"/>',
              f'<circle cx="64" cy="42" r="5.2" fill="none" stroke="{B}" stroke-width="2.8"/>',
              f'<ellipse cx="50" cy="66" rx="8" ry="10" fill="none" stroke="{B}" stroke-width="3"/>']
    return f'<svg viewBox="0 0 100 100" class="kk-facesvg">{"".join(g)}</svg>'


# ============================================================ gunting
def _garis_lepas():
    """Garis potong vertikal dekat punggung buku untuk melepas lembar."""
    return ('<div class="kk-tear">'
            f'<span class="kk-tear__ic">{pico("scissors")}</span>'
            '<span class="kk-tear__line"></span>'
            '<span class="kk-tear__txt">Orang tua: potong di garis ini dulu, '
            'lalu berikan lembarnya kepada anak</span></div>')


def cut_page(title, instr, body, note, badge="Tantangan"):
    NUM[0] += 1
    PAGES.append(f"""<section class="kk-page kk-cutpage">
  {_garis_lepas()}
  <div class="kk-cutpage__in">
    <header class="kk-header">
      <div class="kk-skill-icon kk-skill-icon--cut">{pico("scissors")}</div>
      <div class="kk-header__top"><h1 class="kk-title">{title}</h1>
        <span class="kk-badge {BADGE_CLS.get(badge, '')}">{badge}</span></div>
    </header>
    <div class="kk-content">
      <p class="kk-instruction">{instr}</p>
      <div class="kk-activity">{body}</div>
      <div class="kk-parent-note">
        <span class="kk-parent-note__icon">{pico("lightbulb")}</span><span>{note}</span>
      </div>
    </div>
    <footer class="kk-footer">
      <span class="kk-logo"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></span>
      <span>Gunting</span><span>{NUM[0]}</span>
    </footer>
  </div>
</section>""")


def strip_gunting(kind, key):
    if kind == "pendek":
        garis = ('<svg class="kk-cutsvg kk-cutsvg--short" viewBox="0 0 60 20">'
                 f'<path d="M2 10 H58" fill="none" stroke="{C["berry"]}" stroke-width="3.6" '
                 f'stroke-dasharray="8 6" stroke-linecap="round"/></svg>'
                 '<span class="kk-cutfill"></span>')
    elif kind == "lurus":
        garis = ('<svg class="kk-cutsvg" viewBox="0 0 160 20" preserveAspectRatio="none">'
                 f'<path d="M2 10 H158" fill="none" stroke="{C["berry"]}" stroke-width="3.6" '
                 f'stroke-dasharray="8 6" stroke-linecap="round"/></svg>')
    elif kind == "gelombang":
        garis = ('<svg class="kk-cutsvg" viewBox="0 0 160 22" preserveAspectRatio="none">'
                 f'<path d="M2 11 Q22 1 42 11 Q62 21 82 11 Q102 1 122 11 Q142 21 158 11" '
                 f'fill="none" stroke="{C["berry"]}" stroke-width="3.6" stroke-dasharray="8 6" '
                 f'stroke-linecap="round"/></svg>')
    else:
        garis = ('<svg class="kk-cutsvg" viewBox="0 0 160 22" preserveAspectRatio="none">'
                 f'<path d="M2 18 L22 4 L42 18 L62 4 L82 18 L102 4 L122 18 L142 4 L158 18" '
                 f'fill="none" stroke="{C["berry"]}" stroke-width="3.6" stroke-dasharray="8 6" '
                 f'stroke-linecap="round"/></svg>')
    tangan = f'<span class="kk-cut-ico">{pico("scissors")}</span>'
    return f'<div class="kk-cut-strip">{tangan}{garis}{ic(key, 26)}</div>'


def cut_lines_page(title, instr, strips, note, badge="Tantangan"):
    body = "".join(strip_gunting(k, key) for k, key in strips)
    cut_page(title, instr, body, note, badge)


def cut_shape_page(title, instr, shapes, note, badge="Tantangan"):
    sel = []
    for d, key, color in shapes:
        sel.append(f'<div class="kk-cutcell">'
                   f'<svg viewBox="0 0 100 100" class="kk-cutshape">'
                   f'<path d="{d}" fill="{cr(color)}" fill-opacity=".5" stroke="{C["berry"]}" '
                   f'stroke-width="3" stroke-dasharray="8 6" stroke-linejoin="round"/></svg>'
                   f'<span class="kk-cutcell__ic">{ic(key, 20)}</span></div>')
    cut_page(title, instr, f'<div class="kk-cutgrid2">{"".join(sel)}</div>', note, badge)


def cut_cards_page(title, instr, cards, note, badge="Tantangan"):
    isi = "".join(f'<div class="kk-card">{ic(k, 34)}<span class="kk-card__lbl">{lbl}</span></div>'
                  for k, lbl in cards)
    cut_page(title, instr, f'<div class="kk-cardgrid">{isi}</div>', note, badge)


# ============================================================ halaman khusus
def sampul_depan():
    gambar_penuh("cover_depan.jpeg")


def daftar_isi():
    baris = "".join(
        f'<li class="kk-toc__i">'
        f'<span class="kk-toc__no{"" if no else " kk-toc__no--kosong"}">{no or ""}</span>'
        f'<span class="kk-toc__t">{judul}</span>'
        f'<span class="kk-toc__d"></span><span class="kk-toc__p">{hal}</span></li>'
        for judul, hal, no in TOC)
    PAGES.append(f"""<section class="kk-page kk-toc">
  <header class="kk-header">
    <div class="kk-skill-icon">{pico("book")}</div>
    <div class="kk-header__top"><h1 class="kk-title">Daftar Isi</h1></div>
  </header>
  <div class="kk-content">
    <ol class="kk-toc__list">{baris}</ol>
    <div class="kk-parent-note">
      <span class="kk-parent-note__icon">{pico("lightbulb")}</span>
      <span>Urutannya boleh diacak sesuai minat anak hari itu, kecuali Bagian 1 yang
      sebaiknya dikerjakan lebih dulu karena melatih gerakan dasar tangan. Bagian Gunting
      sengaja ditaruh paling belakang supaya lembarnya bisa dilepas tanpa merusak halaman lain.
      Satu bagian tidak harus selesai dalam satu hari.</span>
    </div>
  </div>
  <footer class="kk-footer">
    <span class="kk-logo"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></span>
    <span>Isi bundel</span><span>2</span>
  </footer>
</section>""")


def panduan_orang_tua():
    NUM[0] += 1
    TOC.append(("Untuk Orang Tua", NUM[0], None))
    P = [("Lembar ini pelengkap, bukan kurikulum.",
          "Anak usia tiga tahun belajar paling banyak lewat bermain bebas, bicara, dan "
          "menyentuh benda nyata. Gunakan halaman ini sebagai selingan singkat, bukan "
          "pengganti waktu bermain. Kalau harus memilih antara mengerjakan satu halaman "
          "atau bermain di luar, pilih bermain di luar."),
         ("Lima sampai sepuluh menit sudah cukup.",
          "Kalau anak berhenti di tengah, hentikan tanpa membujuk. Halaman yang sama boleh "
          "diulang minggu depan, dan mengulang justru tanda anak menikmatinya. Rentang "
          "perhatian usia tiga tahun memang sependek itu, bukan tanda anak tidak fokus."),
         ("Jangan kejar kerapian.",
          "Keluar garis, warna terbalik, dan angka yang dilewati itu normal. Yang dilatih di "
          "sini kontrol tangan dan rasa mampu, bukan hasil akhir yang bagus. Komentari "
          "usahanya, misalnya kamu menariknya pelan-pelan sampai ujung, bukan hasilnya bagus."),
         ("Krayon dulu, pensil belakangan.",
          "Krayon gemuk dan spidol besar tidak memaksa jari menggenggam terlalu kecil. "
          "Genggaman tiga jari biasanya matang di usia empat sampai lima tahun. Kalau anak "
          "memegang dengan seluruh telapak, biarkan saja, itu tahap yang wajar."),
         ("Bagian gunting ada di paling belakang.",
          "Setiap halaman gunting punya garis potong di dekat punggung buku. Potong dulu "
          "lembarnya, baru berikan kepada anak, supaya ia tidak menggunting sambil memegang "
          "buku tebal. Gunakan gunting anak berujung tumpul dan tetap dampingi."),
         ("Kalau anak menolak, simpan dulu.",
          "Menolak berulang kali bukan tanda tertinggal, hanya tanda belum waktunya. Simpan "
          "bundel ini satu atau dua bulan lalu tawarkan lagi. Anak yang dipaksa duduk "
          "mengerjakan lembar kerja lebih sering kehilangan minat belajar daripada yang "
          "dibiarkan menunggu sampai siap.")]
    isi = "".join(f'<p class="kk-body"><b>{a}</b> {b}</p>' for a, b in P)
    PAGES.append(f"""<section class="kk-page">
  <header class="kk-header">
    <div class="kk-skill-icon">{pico("users-three")}</div>
    <div class="kk-header__top"><h1 class="kk-title">Untuk Orang Tua</h1></div>
  </header>
  <div class="kk-content kk-content--text">{isi}</div>
  <footer class="kk-footer">
    <span class="kk-logo"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></span>
    <span>Panduan</span><span>{NUM[0]}</span>
  </footer>
</section>""")


def bundel_lainnya():
    NUM[0] += 1
    TOC.append(("Bundel Lainnya", NUM[0], None))
    seri = [
        ("2 Tahun", "Coretan bebas dan warna",
         "Tangan masih menggenggam penuh, jadi semua aktivitas memakai bidang lebar dan tidak "
         "menuntut ketepatan sama sekali.",
         ["coretan bebas di bidang besar", "mencocokkan bentuk sederhana",
          "mewarnai gambar bergaris tebal", "menempel dan menekan", "mengenali warna dasar"],
         "62 halaman"),
        ("3 Tahun", "Garis, angka awal, dan gunting pertama",
         "Buku yang sedang Anda pegang. Anak mulai bisa menahan krayon di dalam jalur dan "
         "memegang gunting untuk potongan pendek.",
         ["pra-menulis sembilan jenis garis", "menelusuri angka 1 sampai 9 dan huruf a sampai i",
          "berhitung sampai sepuluh", "pola gambar, warna, dan bentuk",
          "menggunting garis lurus dan bergelombang"],
         "60 halaman"),
        ("4 Tahun", "Huruf, pola, dan gunting berlekuk",
         "Genggaman tiga jari mulai matang, jadi bidang latihan mengecil dan tuntutan "
         "ketepatannya naik.",
         ["menulis nama sendiri", "huruf a sampai z", "berhitung sampai dua puluh",
          "pola tiga unsur dan urutan", "menggunting bentuk berlekuk"],
         "68 halaman"),
        ("5 Tahun", "Menulis, membaca awal, dan berhitung",
         "Persiapan masuk sekolah dasar, dengan porsi menulis dan membaca yang jauh lebih "
         "besar daripada bundel sebelumnya.",
         ["menulis kata pendek", "suku kata dan bunyi awal", "penjumlahan dan pengurangan kecil",
          "mengurutkan cerita bergambar", "menggunting dan menempel proyek"],
         "72 halaman"),
    ]
    kartu = "".join(
        f'<div class="kk-seri__card{" kk-seri__card--on" if u.startswith("3") else ""}">'
        f'<div class="kk-seri__head"><span class="kk-seri__u">{u}</span>'
        f'<span class="kk-seri__n">{n}</span></div>'
        f'<span class="kk-seri__d">{d}</span>'
        f'<p class="kk-seri__p">{ket}</p>'
        f'<ul class="kk-seri__l">' + "".join(f"<li>{i}</li>" for i in isi) + '</ul></div>'
        for u, d, ket, isi, n in seri)
    PAGES.append(f"""<section class="kk-page">
  <header class="kk-header">
    <div class="kk-skill-icon">{pico("book")}</div>
    <div class="kk-header__top"><h1 class="kk-title">Bundel Lainnya</h1></div>
  </header>
  <div class="kk-content">
    <p class="kk-instruction">Kertas Kecil tersedia untuk empat kelompok usia. Setiap bundel
      disusun ulang dari nol mengikuti kemampuan tangan dan rentang perhatian di usia itu,
      bukan versi lebih mudah atau lebih sulit dari bundel yang lain.</p>
    <div class="kk-serigrid">{kartu}</div>
    <div class="kk-parent-note">
      <span class="kk-parent-note__icon">{pico("lightbulb")}</span>
      <span>Kalau anak menyelesaikan bundel ini dengan mudah dan masih ingin lagi, lanjutkan
      ke usia berikutnya tanpa menunggu ulang tahunnya. Sebaliknya, kalau terasa berat, bundel
      usia di bawahnya tetap berguna dan bukan tanda tertinggal. Semua bundel dijual dalam
      bentuk cetak dan berkas PDF, dan kabar terbarunya ada di Instagram
      <b>@kertaskecil.project</b>.</span>
    </div>
  </div>
  <footer class="kk-footer">
    <span class="kk-logo"><span class="kk-logo__mark"></span><span class="kk-logo__name">Kertas Kecil</span></span>
    <span>Seri Kertas Kecil</span><span>{NUM[0]}</span>
  </footer>
</section>""")


def sampul_belakang():
    tinggi = {"2": 14, "3": 22, "4": 30, "5": 38}
    seri = "".join(
        f'<span class="kk-seri__i {"kk-seri__i--on" if u == "3" else ""}" '
        f'style="height:{tinggi[u]}mm">{u}</span>' for u in ("2", "3", "4", "5"))
    raw_page(f"""<section class="kk-page kk-back">
  <div class="kk-back__in">
    <div class="kk-logo kk-logo--inv"><span class="kk-logo__mark"></span>
      <span class="kk-logo__name">Kertas Kecil</span></div>
    <p class="kk-back__lead">Buku Aktivitas Anak Usia 3 Tahun</p>
    <p class="kk-back__p">Kertas Kecil adalah buku aktivitas untuk anak usia tiga tahun yang
      dikerjakan cukup dengan krayon dan gunting. Tidak perlu stiker, lem, atau alat
      tambahan apa pun.</p>
    <p class="kk-back__p">Isinya sembilan bagian: menarik garis dan coretan, menelusuri angka
      dan huruf, mencocokkan dan membedakan, pola, berhitung sampai sepuluh, mewarnai,
      mengikuti jalan berliku, mengenali perasaan, dan menggunting. Setiap halaman punya satu
      contoh yang sudah dikerjakan, jadi orang tua tidak perlu menebak maksud perintahnya.</p>
    <p class="kk-back__p">Di setiap halaman ada catatan untuk orang tua tentang keterampilan
      yang sedang dilatih dan apa yang wajar terjadi di usia ini. Lembar menggunting ditaruh
      di bagian belakang dan bisa dilepas satu per satu.</p>
    <div class="kk-seri"><span class="kk-seri__t">tersedia untuk usia 2 sampai 5 tahun</span>
      <div class="kk-seri__row">{seri}</div>
      <p class="kk-back__ig">@kertaskecil.project</p></div>
  </div>
</section>""", hitung=False)


def warnai_page(nama, title, instr, note, badge="Mulai"):
    """Halaman mewarnai: gambar garis dari folder assets/."""
    ada = (ASSET_DIR / nama).exists()
    isi = (f'<img src="assets/{nama}" class="kk-color__img" alt="">' if ada else
           '<div class="kk-color__ph">Gambar mewarnai belum ada.<br>'
           f'Simpan berkasnya sebagai <code>assets/{nama}</code>.</div>')
    page(title, instr, f'<div class="kk-center">{isi}</div>', note, "Warna", "paint-brush",
         badge, "kk-skill-icon--color")


# ============================================================ isi bundel
def bagian_1():
    divider(1, "Garis dan Coretan")
    trace_page("Garis Lurus", "Tarik dari titik hijau sampai ke ujung.",
               "M8 22 H50",
               "Garis lurus melatih tangan berhenti tepat di tempat yang dituju, dan itu "
               "kemampuan yang dipakai nanti saat menulis huruf. Keluar jalur sama sekali "
               "bukan masalah di usia tiga tahun. Kalau anak menarik terlalu cepat, coba "
               "hitung bersama sampai tiga selama krayonnya berjalan.",
               deco=("bike", "car", "truck"), start=(8, 22))
    trace_page("Garis Tegak", "Tarik dari titik hijau ke bawah.",
               "M29 6 V38",
               "Gerakan dari atas ke bawah biasanya dikuasai lebih dulu daripada gerakan "
               "mendatar. Ini dasar huruf l, i, dan t yang akan dipelajari beberapa tahun "
               "lagi. Biarkan anak mengangkat krayon di tengah jalan kalau ia perlu berhenti.",
               deco=("carrot", "corn", "drumstick"), start=(29, 6))
    trace_page("Garis Miring", "Tarik dari titik hijau ke ujung yang lain.",
               "M8 36 L50 8",
               "Garis miring lebih sulit daripada lurus karena tangan harus bergerak ke dua "
               "arah sekaligus. Kalau anak kesulitan, pandu tangannya sekali lalu lepaskan "
               "dan biarkan ia mencoba sendiri. Jangan memegangi tangannya sepanjang halaman.",
               deco=("kangaroo", "monkey", "dinosaur"), start=(8, 36))
    trace_page("Garis Bukit", "Ikuti jalannya naik lalu turun.",
               "M8 36 Q29 4 50 36",
               "Lengkungan melatih pergelangan tangan berputar, bukan cuma jari yang bergeser. "
               "Sebutkan gerakannya sambil anak menarik, misalnya naik lalu turun, karena kata "
               "membantu anak mengingat arah. Bukit dan lembah adalah bahan dasar huruf n dan u.",
               deco=("elephant2", "giraffe", "sunrise"), start=(8, 36))
    trace_page("Garis Lembah", "Ikuti jalannya turun lalu naik.",
               "M8 8 Q29 40 50 8",
               "Ini kebalikan dari halaman sebelumnya dan biasanya terasa lebih sulit. Dua arah "
               "lengkung ini menyiapkan bentuk huruf u dan bagian bawah huruf y. Kalau anak "
               "melewatkan dasar lembahnya, tidak perlu dikoreksi, cukup ulangi lain hari.",
               deco=("whale", "crab", "octopus"), start=(8, 8))
    trace_page("Garis Gelombang", "Ikuti ombaknya sampai ke ujung.",
               "M8 22 Q18 5 29 22 Q40 39 50 22",
               "Ombak menggabungkan naik dan turun tanpa mengangkat tangan, jadi ini latihan "
               "gerakan mengalir yang berkelanjutan. Bersenandung sambil menarik sering membantu "
               "anak menjaga iramanya. Kalau garisnya jadi bergerigi, itu tanda tangannya masih "
               "menegang dan akan melunak dengan latihan.",
               deco=("sailboat", "dolphin", "shrimp"), start=(8, 22))
    trace_page("Garis Zigzag", "Ikuti gigi gergajinya.",
               "M8 38 L18 8 L29 38 L40 8 L50 38",
               "Zigzag menuntut tangan berhenti mendadak lalu berganti arah, gerakan yang jauh "
               "lebih rumit daripada kelihatannya. Sudut yang membulat itu normal di usia ini. "
               "Kalau anak terburu-buru, minta ia berhenti sejenak di setiap puncak.",
               deco=("tiger", "crocodile", "snake"), start=(8, 38))
    trace_page("Lingkaran", "Mulai dari titik hijau, putar sampai bertemu lagi.",
               "M29 8 A15 15 0 1 1 28.4 8",
               "Lingkaran adalah gerakan dasar huruf o, a, c, dan d. Arah putarannya belum perlu "
               "diseragamkan sekarang, yang penting anak berani menutup bentuknya. Banyak anak "
               "berhenti sebelum lingkarannya tersambung, dan itu wajar.",
               deco=("watermelon", "donut", "pizza"), start=(29, 8))
    trace_page("Garis Silang", "Tarik dua garis sampai bersilangan.",
               "M10 8 L48 36 M48 8 L10 36",
               "Menyilang berarti tangan harus melewati garis tengah tubuh, dan itu tahap "
               "penting perkembangan yang berkaitan dengan koordinasi dua sisi otak. Perhatikan "
               "apakah anak memutar badannya atau memindahkan krayon ke tangan lain. Keduanya "
               "wajar sekarang dan akan hilang sendiri.",
               deco=("butterfly", "ladybug", "rainbow"), start=(10, 8))
    trace_page("Garis Melingkar", "Ikuti putarannya tanpa mengangkat tangan.",
               "M8 34 C11 8 27 8 22 27 C18 42 36 42 33 20 C30 6 46 10 50 32",
               "Loop berulang adalah pemanasan untuk tulisan sambung yang akan datang jauh di "
               "kemudian hari. Yang dilatih di sini kelenturan pergelangan, bukan ketepatan. "
               "Kalau anak mengangkat krayonnya di tengah, biarkan dan minta ia melanjutkan.",
               deco=("owl", "chipmunk", "macaw"), start=(8, 34))
    trace_page("Garis Bersudut", "Tarik ke bawah dulu, lalu belok ke kanan.",
               "M12 6 V34 H50",
               "Berbelok tajam menuntut tangan berhenti total sebelum berganti arah, berbeda "
               "dengan lengkungan yang mengalir. Perhatikan apakah anak melambat menjelang "
               "sudutnya, karena itu tanda ia mulai bisa merencanakan gerakan. Sudut yang "
               "membulat tetap dihitung berhasil di usia tiga tahun.",
               deco=("umbrella2", "guitar", "drumkit"), start=(12, 6))


def bagian_2():
    divider(2, "Angka dan Huruf")
    glyph_page("Telusuri Angka 1 2 3", "Telusuri angkanya mulai dari titik hijau.",
               ["1", "2", "3"],
               "Sebut angkanya keras-keras setiap kali ditelusuri karena suara membantu ingatan "
               "lebih daripada gerakan tangan saja. Anak belum perlu tahu bahwa angka 2 berarti "
               "dua benda, itu urusan Bagian 5. Di sini yang dilatih hanya bentuknya.",
               "Angka", ("melon", "butterfly", "rooster"))
    glyph_page("Telusuri Angka 4 5 6", "Telusuri angkanya. Mulai dari titik hijau.",
               ["4", "5", "6"],
               "Angka 4 dan 5 sama-sama punya dua goresan terpisah, jadi anak boleh mengangkat "
               "krayonnya di tengah. Kalau anak menelusuri dari arah yang berbeda, biarkan dulu, "
               "arah baku bisa menyusul di usia lima tahun. Yang penting bentuk akhirnya "
               "terbaca sebagai angka itu.",
               "Angka", ("crab", "rainbow", "cake"))
    glyph_page("Telusuri Angka 7 8 9", "Telusuri angkanya pelan-pelan.",
               ["7", "8", "9"],
               "Angka 8 adalah yang paling sulit di halaman ini karena jalurnya menyilang di "
               "tengah. Boleh dipecah dulu jadi dua lingkaran yang ditumpuk. Kalau anak lelah "
               "setelah dua baris, berhenti saja dan lanjutkan besok.",
               "Angka", ("watermelon", "watermelon", "pizza"))
    glyph_page("Telusuri Huruf a b c", "Telusuri hurufnya. Sebut bunyinya sambil menarik.",
               ["a", "b", "c"],
               "Huruf kecil lebih sering ditemui anak dalam buku cerita daripada huruf besar, "
               "jadi mengenalkannya lebih dulu masuk akal. Bunyikan hurufnya, bukan namanya, "
               "misalnya be untuk b. Anak tiga tahun belum diharapkan hafal, cukup akrab.",
               "Huruf", ("apple2", "bird", "camera"))
    glyph_page("Telusuri Huruf d e f", "Telusuri hurufnya dari titik hijau.",
               ["d", "e", "f"],
               "Huruf b dan d sering tertukar sampai usia enam atau tujuh tahun, jadi jangan "
               "cemas kalau anak membalik arahnya. Halaman ini melatih tangan, bukan menguji "
               "hafalan. Kalau anak mulai menebak-nebak huruf di kemasan makanan, itu tanda "
               "yang jauh lebih bagus daripada telusuran yang rapi.",
               "Huruf", ("dog", "elephant", "fries"))
    glyph_page("Telusuri Huruf g h i", "Telusuri hurufnya dari titik hijau.",
               ["g", "h", "i"],
               "Huruf g punya ekor yang turun sampai di bawah garis merah, dan itu gerakan baru "
               "yang belum muncul di halaman sebelumnya. Huruf i cuma satu garis pendek dengan "
               "satu titik, jadi biasanya jadi huruf yang paling cepat dikuasai. Kerjakan "
               "sebaris saja per hari kalau anak mulai bosan.",
               "Huruf", ("glasses", "hat", "icecream"))


def bagian_3():
    divider(3, "Cocokkan dan Bedakan")
    match_page("Cari Pasangannya", "Tarik garis dari gambar kiri ke pasangannya di kanan.",
               [("monkey", "monkey"), ("pig", "pig"), ("rooster", "rooster"),
                ("snake", "snake"), ("rabbit", "rabbit")],
               "Baris pertama sudah disambungkan sebagai contoh, jadi anak bisa melihat maksud "
               "perintahnya tanpa dijelaskan panjang. Kalau anak ragu, tutup sebagian baris "
               "dengan tangan supaya pilihannya lebih sedikit. Menarik garis panjang melintasi "
               "halaman juga latihan motorik tersendiri.")
    match_page("Cocokkan Buahnya", "Tarik garis ke buah yang sama.",
               [("melon", "melon"), ("carrot", "pizza"), ("corn", "corn"),
                ("drumstick", "drumstick"), ("pizza", "pizza")],
               "Sambil mencocokkan, sebut nama dan warna buahnya supaya satu halaman melatih "
               "dua hal sekaligus. Wortel sengaja diselipkan di antara buah untuk memancing "
               "percakapan tentang mana yang buah dan mana yang sayur. Jawaban anak tidak perlu "
               "benar, obrolannya yang berharga.")
    choose_page("Mana yang Sama", "Lingkari gambar yang sama dengan gambar di kotak kiri.",
                [("cat", ["dog", "cat", "chipmunk", "owl"], 1),
                 ("pizza", ["cake", "fries", "pizza", "hotdog"], 2),
                 ("whale", ["whale", "octopus", "crab", "shrimp"], 0),
                 ("car", ["rocket", "stroller", "truck", "car"], 3)],
                "Lingkaran yang berantakan tetap dihitung benar, yang dinilai pilihannya. "
                "Kalau anak menunjuk dengan jari lebih dulu sebelum melingkari, itu justru "
                "cara berpikir yang bagus. Baris pertama sudah dilingkari sebagai contoh.",
                "Cocokkan", "magnifying-glass")
    choose_page("Mana yang Berbeda", "Coret satu gambar yang berbeda sendiri.",
                [(None, ["rooster", "rooster", "rooster", "macaw"], 3),
                 (None, ["cup", "cup", "pot", "cup"], 2),
                 (None, ["sushi", "juice", "juice", "juice"], 0),
                 (None, ["tree", "tree", "tree", "sunrise"], 3)],
                "Setelah anak memilih, tanyakan kenapa gambar itu berbeda. Jawabannya lebih "
                "berharga daripada coretannya, dan sering memperlihatkan cara anak "
                "mengelompokkan benda. Kalau alasannya masuk akal menurut anak, terima saja "
                "meskipun bukan yang Anda pikirkan.",
                "Bedakan", "x-circle")
    size_page("Besar dan Kecil", "Lingkari yang paling kecil di setiap baris.",
              [("elephant", (30, 15, 22)), ("melon", (16, 28, 23)),
               ("dolphin", (24, 30, 14)), ("cactus", (21, 14, 29))],
              "Mencari yang paling kecil ternyata lebih sulit daripada mencari yang paling "
              "besar, karena mata anak cenderung tertarik ke benda terbesar lebih dulu. "
              "Bandingkan juga dengan benda nyata di rumah, misalnya sendok makan dan sendok "
              "teh. Kata paling kecil sebaiknya sering diucapkan dalam percakapan sehari-hari.",
              cari="kecil")
    match_page("Cocokkan Kendaraannya", "Tarik garis ke kendaraan yang sama.",
               [("truck", "truck"), ("rocket", "rocket"), ("stroller", "stroller"),
                ("skates", "skates")],
               "Halaman ini mengulang keterampilan yang sama dengan gambar berbeda, dan "
               "pengulangan seperti itu memang disengaja. Anak usia tiga tahun butuh bertemu "
               "konsep yang sama berkali-kali dalam wujud berbeda sebelum benar-benar "
               "menguasainya. Tanyakan kendaraan mana yang pernah dinaiki anak.")


def bagian_4():
    divider(4, "Pola")
    pattern_page("Lanjutkan Pola", "Lihat urutannya, lalu tarik garis dari kotak kosong "
                 "ke gambar yang cocok.",
                 [(["apple2", "juice", "apple2", "juice"], "apple2"),
                  (["sunrise", "rain", "sunrise", "rain"], "sunrise"),
                  (["forest", "flower", "forest", "flower"], "forest"),
                  (["hat", "glasses", "hat", "glasses"], "hat")],
                 "Bacakan polanya keras-keras, misalnya apel, jus, apel, jus, lalu? Telinga "
                 "menangkap pola jauh lebih cepat daripada mata di usia ini. Baris pertama "
                 "sudah disambungkan sebagai contoh supaya anak paham yang diminta.")
    pattern_size_page("Pola Besar Kecil",
                      "Lihat urutan ukurannya, lalu tarik garis ke gambar yang cocok.",
                      [("cat", (20, 12, 20, 12), 20),
                       ("truck", (12, 20, 12, 20), 12),
                       ("flower", (20, 12, 20, 12), 20),
                       ("fish", (12, 20, 12, 20), 12)],
                      "Di halaman ini gambarnya sama, yang berganti hanya ukurannya, jadi anak "
                      "harus memperhatikan besar kecil dan bukan bendanya. Sebut sambil "
                      "menunjuk: besar, kecil, besar, kecil, lalu? Kalau anak bingung, tutup "
                      "dua kotak terakhir dengan tangan supaya deretnya terlihat lebih pendek.")
    pattern_color_page("Pola Warna",
                       "Lihat urutan warnanya, lalu tarik garis ke warna yang cocok.",
                       [(["berry", "sky", "berry", "sky"], "berry"),
                        (["sunny", "leaf", "sunny", "leaf"], "sunny"),
                        (["grape", "orange", "grape", "orange"], "grape"),
                        (["sky", "sunny", "sky", "sunny"], "sky")],
                       "Halaman ini sengaja tanpa gambar sama sekali supaya anak membaca "
                       "warnanya saja. Sebutkan nama warnanya sambil menunjuk satu per satu. "
                       "Kalau anak belum hafal nama warna, cukup minta ia mencari kotak yang "
                       "sama persis, karena mencocokkan lebih dulu datang daripada menamai.")
    pattern_shape_page("Pola Bentuk",
                       "Lihat urutan bentuknya, lalu tarik garis ke bentuk yang cocok.",
                       [(["lingkaran", "kotak", "lingkaran", "kotak"], "sky", "lingkaran"),
                        (["segitiga", "lingkaran", "segitiga", "lingkaran"], "leaf", "segitiga"),
                        (["hati", "segitiga", "hati", "segitiga"], "berry", "hati"),
                        (["kotak", "hati", "kotak", "hati"], "grape", "kotak")],
                       "Warna dalam satu baris sengaja dibuat sama supaya yang dibaca anak "
                       "bentuknya, bukan warnanya. Setelah selesai, cari benda berbentuk sama "
                       "di sekitar rumah, misalnya piring bulat dan buku kotak. Bentuk dasar "
                       "ini juga muncul lagi di bagian menggunting.",
                       badge="Tantangan")


def bagian_5():
    divider(5, "Berhitung")
    count_page("Hitung Sampai Tiga", "Hitung benda di dalam kotak, lalu lingkari angkanya.",
               [("cake", 1, [1, 2, 3]), ("rooster", 2, [1, 2, 3]), ("crab", 3, [1, 2, 3]),
                ("forest", 2, [1, 2, 3])],
               "Sentuh tiap benda sambil menyebut angkanya, karena menghitung tanpa menyentuh "
               "hampir selalu meleset di usia ini. Angka terakhir yang disebut adalah "
               "jumlahnya, dan konsep itu butuh berbulan-bulan untuk benar-benar dipahami. "
               "Baris pertama sudah dijawab sebagai contoh.")
    count_page("Hitung Sampai Lima", "Hitung benda di dalam kotak, lalu lingkari angkanya.",
               [("sushi", 4, [3, 4, 5]), ("shuttlecock", 5, [3, 4, 5]),
                ("melon", 3, [3, 4, 5]), ("ladybug", 5, [3, 4, 5])],
               "Kalau anak menghitung ulang benda yang sama atau melewatkan satu, itu hal "
               "paling umum di usia tiga tahun. Menunjuk satu per satu sambil menghitung "
               "membantu, begitu juga menggeser benda nyata ke sisi lain setelah dihitung. "
               "Hitung bersama, jangan langsung membetulkan.")
    count_page("Hitung Sampai Sepuluh", "Hitung benda di dalam kotak, lalu lingkari angkanya.",
               [("key", 7, [6, 7, 8]), ("cake", 6, [6, 7, 8]), ("fries", 8, [6, 7, 8])],
               "Di atas lima, susun benda berbaris dulu supaya lebih mudah dihitung, karena "
               "tumpukan acak membuat anak kehilangan jejak. Banyak anak tiga tahun hafal urutan "
               "sampai sepuluh tapi belum bisa memakainya untuk menghitung, dan itu dua "
               "kemampuan yang berbeda. Halaman ini melatih yang kedua.")
    count_match_page("Cocokkan Jumlah", "Tarik garis dari kelompok benda ke angka yang tepat.",
                     [("shrimp", 2), ("chipmunk", 4), ("apple2", 3), ("butterfly", 5), ("bulb", 1)],
                     "Halaman ini menyambungkan jumlah benda dengan lambang angkanya, "
                     "penghubung yang tidak otomatis bagi anak. Kalau salah, hitung bersama "
                     "sambil menunjuk lalu biarkan anak memperbaiki sendiri. Baris pertama "
                     "sudah disambungkan sebagai contoh.")
    more_page("Mana yang Lebih Banyak", "Lingkari kelompok yang lebih banyak.",
              [("cup", 2, 5), ("fish", 6, 3), ("pig", 4, 2), ("hotdog", 3, 7)],
              "Anak sering memilih kelompok yang memakan tempat lebih luas, bukan yang benar "
              "lebih banyak, dan itu normal. Kalau terjadi, rapatkan benda di satu sisi lalu "
              "tanyakan lagi. Membandingkan jumlah tanpa menghitung adalah kemampuan yang "
              "berkembang perlahan sampai usia lima tahun.")
    more_page("Mana yang Lebih Sedikit", "Lingkari kelompok yang lebih sedikit.",
              [("owl", 5, 2), ("carrot", 3, 6), ("bunny", 7, 4), ("juice", 2, 5)],
              "Mencari yang lebih sedikit lebih sulit daripada mencari yang lebih banyak, "
              "karena anak harus menahan dorongan memilih kelompok yang paling menarik "
              "perhatian. Kalau anak keliru, hitung kedua kelompok bersama lalu bandingkan "
              "angkanya. Halaman ini boleh dikerjakan lain hari kalau terasa berat.",
              cari="sedikit")


def bagian_6():
    divider(6, "Warna")
    hunt_page("Cari Huruf n, b, dan u", "Warnai kotak yang hurufnya sama dengan contoh di atas.",
              [("n", "sky"), ("b", "sunny"), ("u", "berry")],
              [[("n", "sky"), ("b", None), ("l", None)],
               [("u", None), ("g", None), ("u", None)],
               [("s", None), ("b", None), ("n", None)],
               [("b", None), ("n", None), ("d", None)]],
              "Anak tidak perlu tahu nama hurufnya untuk mengerjakan halaman ini, yang dilatih "
              "mata mencocokkan bentuk. Kotak pertama sudah diwarnai sebagai contoh. Warna "
              "yang keluar kotak sama sekali bukan masalah, justru itu tanda anak menekan "
              "krayonnya dengan berani.")
    hunt_page("Tetesan Hujan k, e, v", "Warnai tetesan sesuai warna contoh di baris atas.",
              [("k", "sky"), ("e", "forest"), ("v", "orange")],
              [[("k", None), ("e", None), ("v", None)],
               [("e", None), ("k", None), ("e", None)],
               [("v", None), ("v", None), ("k", None)]],
              "Huruf k, e, dan v dipilih karena bentuknya sangat berbeda satu sama lain, jadi "
              "anak tidak perlu membedakan detail halus. Bentuk tetesan lebih sulit diwarnai "
              "daripada kotak karena ujungnya lancip. Kalau anak hanya mencoret sekali di "
              "tengah, itu tetap dihitung selesai.",
              shape="drop", badge="Lanjut")
    warnai_page("warnai_1.jpeg", "Warnai Langit",
                "Warnai matahari, awan, dan balonnya.",
                "Sebutkan warnanya sambil anak mewarnai, karena kosakata warna tumbuh dari "
                "percakapan bukan dari hafalan. Kalau anak mewarnai matahari jadi biru, "
                "biarkan saja dan tanyakan ceritanya. Memaksa warna yang benar di usia ini "
                "hanya membuat anak berhenti mencoba.")
    warnai_page("warnai_2.jpeg", "Warnai Bawah Laut",
                "Warnai ikan, bintang laut, dan rumput lautnya.",
                "Tanyakan ikan mana yang paling besar dan mana yang paling kecil sebelum mulai "
                "mewarnai, jadi satu halaman dipakai untuk dua hal. Bidang besar diwarnai lebih "
                "dulu, bagian kecil belakangan. Anak tiga tahun biasanya bertahan lima sampai "
                "sepuluh menit di halaman mewarnai.")
    warnai_page("warnai_3.jpeg", "Warnai Kebun",
                "Warnai bunga, daun, dan kupu-kupunya.",
                "Kelopak bunga adalah bentuk kecil berulang, jadi halaman ini melatih tangan "
                "berhenti di tepi. Tidak perlu semua kelopak diwarnai, satu atau dua sudah "
                "cukup untuk sekali duduk. Kalau anak ingin menambah gambar sendiri di ruang "
                "kosongnya, biarkan.")
    warnai_page("warnai_4.jpeg", "Warnai Buah",
                "Warnai buah-buahannya.",
                "Sebelum mewarnai, tanyakan buah apa saja yang pernah dimakan anak minggu ini "
                "supaya gambar di kertas terhubung dengan pengalaman nyatanya. Warna asli buah "
                "boleh jadi bahan obrolan, tapi jangan dijadikan aturan. Halaman ini juga bisa "
                "diulang lain hari dengan warna berbeda kalau dicetak dua kali.")
    warnai_page("warnai_5.jpeg", "Warnai Hewan",
                "Warnai hewan-hewannya.",
                "Bidang tubuh hewan cukup besar untuk anak yang belum bisa mengontrol tepi, "
                "jadi halaman ini biasanya terasa lebih mudah daripada halaman kebun. Tirukan "
                "suara hewannya sambil mewarnai supaya kegiatannya tidak terasa seperti tugas. "
                "Berhenti begitu anak mulai kehilangan minat.")


def bagian_7():
    divider(7, "Jalan Berliku")
    path_page("Naik Turun Bukit", "Ikuti jalannya dari kiri sampai ke ujung kanan.",
              "M18 200 Q46 122 74 200 Q102 122 130 200 Q158 122 182 178",
              "kangaroo", "forest",
              "Jalur naik turun berulang melatih tangan bergerak dengan irama tetap, mirip "
              "gerakan menulis huruf m dan n nanti. Jalannya sengaja dibuat lebar supaya anak "
              "berhasil di percobaan pertama. Awal jalurnya sudah ditarik sebagai contoh.",
              start_xy=(18, 200), end_xy=(182, 178),
              deco=[("sunrise", 100, 60, 26), ("bird", 44, 78, 20), ("tree", 158, 96, 22)])
    path_page("Jalan Berbelok", "Ikuti jalannya sampai bertemu paus.",
              "M20 22 H80 V60 H36 V100 H112 V138 H50 V176 H120 V212 H178",
              "fish", "whale",
              "Sudut siku-siku memaksa tangan berhenti total lalu berbelok, dan itu lebih sulit "
              "daripada lengkungan yang mengalir. Perhatikan apakah anak melambat menjelang "
              "belokan, karena itu tanda ia sudah bisa merencanakan gerakan. Kalau ia memotong "
              "sudutnya, tidak apa-apa.",
              start_xy=(20, 22), end_xy=(178, 212),
              deco=[("dolphin", 150, 40, 20), ("fish2", 158, 112, 18),
                    ("sailboat", 26, 138, 18), ("octopus", 96, 190, 20)])
    path_page("Jalan Bolak-balik", "Ikuti jalannya dari atas, bolak-balik sampai ke bawah.",
              "M22 24 H160 Q180 24 180 44 Q180 62 160 62 H40 Q20 62 20 82 Q20 100 40 100 "
              "H160 Q180 100 180 120 Q180 138 160 138 H40 Q20 138 20 158 Q20 176 40 176 "
              "H160 Q180 176 180 196 Q180 214 160 214 H40",
              "car", "flower",
              "Jalur bolak-balik seperti ini memaksa anak berputar balik berkali-kali tanpa "
              "kehilangan jalur, dan itu latihan ketekunan sekaligus motorik. Boleh dikerjakan "
              "separuh lalu dilanjutkan besok. Tandai sampai mana anak berhasil supaya ia "
              "melihat kemajuannya sendiri.",
              start_xy=(22, 24), end_xy=(40, 214),
              deco=[("cactus", 100, 82, 18), ("cup", 100, 158, 18)],
              badge="Tantangan")
    path_page("Jalan Berputar", "Ikuti jalannya berputar ke dalam sampai bertemu sarang.",
              "M20 30 H176 V204 H44 V64 H150 V178 H72 V92 H124 V152 H98",
              "chipmunk", "owl",
              "Jalur yang berputar ke dalam membuat anak harus terus mengikuti arah tanpa "
              "bisa menebak ke mana ujungnya, berbeda dari jalur lurus atau ombak. Kalau anak "
              "kehilangan jejak, tunjuk saja belokan berikutnya dengan jari. Ini halaman "
              "penutup bagian ini dan boleh dilewati kalau terasa berat.",
              start_xy=(20, 30), end_xy=(98, 152),
              deco=[("butterfly", 30, 230, 20), ("rainbow", 168, 230, 22)])


def gambar_penuh_aktivitas(nama, title, instr, note, skill, icon, badge="Mulai", icon_cls=""):
    """Halaman aktivitas yang isinya satu gambar besar dari folder assets/."""
    ada = (ASSET_DIR / nama).exists()
    isi = (f'<img src="assets/{nama}" class="kk-color__img" alt="">' if ada else
           '<div class="kk-color__ph">Gambar belum ada.<br>'
           f'Simpan berkasnya sebagai <code>assets/{nama}</code>.</div>')
    page(title, instr, f'<div class="kk-center">{isi}</div>', note, skill, icon, badge, icon_cls)


def bagian_8():
    divider(8, "Perasaan")
    gambar_penuh_aktivitas(
        "perasaan_1.jpeg", "Kenali Perasaannya",
        "Lihat wajahnya satu per satu, lalu sebutkan namanya keras-keras.",
        "Perasaan yang belum punya nama jauh lebih sulit dikendalikan, jadi latihan menamai "
        "seperti ini berguna di luar kertas. Jangan buru-buru mengejar sembilan-sembilannya "
        "dalam sekali duduk, tiga sampai empat wajah per hari sudah banyak. Sebutkan juga "
        "perasaan Anda sendiri hari ini supaya anak melihat orang dewasa pun punya perasaan "
        "yang berganti-ganti.",
        "Sosial emosional", "smiley", "Mulai", "kk-skill-icon--shape")
    gambar_penuh_aktivitas(
        "perasaan_2.jpeg", "Gambar Wajahnya",
        "Gambar mata dan mulutnya sesuai perasaan yang tertulis di bawah lingkaran.",
        "Dua titik dan satu garis lengkung sudah cukup untuk menggambar wajah, jadi jangan "
        "menuntut lebih. Tujuannya bercerita, bukan menggambar bagus. Kalau anak bingung mulai "
        "dari mana, buka lagi halaman sebelumnya sebentar lalu tutup kembali supaya ia "
        "menggambar dari ingatan.",
        "Sosial emosional", "smiley-wink", "Lanjut", "kk-skill-icon--shape")
    gambar_penuh_aktivitas(
        "perasaan_3.jpeg", "Kapan Rasanya Begitu",
        "Tarik garis dari gambar di kiri ke wajah yang perasaannya cocok.",
        "Halaman ini menghubungkan kejadian dengan perasaan, penghubung yang tidak otomatis "
        "bagi anak dan justru inti dari kecerdasan emosi. Setelah selesai, tanyakan apakah anak "
        "pernah mengalami salah satu kejadian itu. Jawaban yang berbeda dari dugaan Anda tetap "
        "diterima, karena perasaan setiap orang atas kejadian yang sama memang bisa berbeda.",
        "Sosial emosional", "puzzle-piece", "Lanjut", "kk-skill-icon--shape")
    gambar_penuh_aktivitas(
        "perasaan_4.jpeg", "Cari yang Sedang Senang",
        "Warnai semua wajah yang sedang senang. Wajah lain biarkan putih.",
        "Membedakan satu ekspresi di antara banyak ekspresi lain jauh lebih sulit daripada "
        "menamai wajah satu per satu, jadi halaman ini penutup yang pas untuk bagian ini. "
        "Kalau anak salah mewarnai satu wajah, biarkan saja dan tanyakan menurutnya wajah itu "
        "sedang apa. Wajah contoh di bagian atas boleh dilihat berkali-kali.",
        "Sosial emosional", "palette", "Tantangan", "kk-skill-icon--color")


def bagian_9():
    divider(9, "Gunting")
    cut_lines_page("Gunting Sekali Potong", "Potong sekali di setiap garis merah.",
                   [("pendek", "cake"), ("pendek", "melon"), ("pendek", "donut"),
                    ("pendek", "cake"), ("pendek", "watermelon")],
                   "Sekali buka tutup gunting sudah menyelesaikan satu garis, jadi ini titik "
                   "mulai yang paling mudah. Tunjukkan cara memegang gunting dengan jempol di "
                   "atas sekali saja, lalu biarkan anak mencoba. Dampingi terus selama anak "
                   "memegang gunting.")
    cut_lines_page("Gunting Garis Lurus", "Gunting mengikuti garis sampai ke ujung.",
                   [("lurus", "pig"), ("lurus", "rooster"), ("lurus", "chipmunk"), ("lurus", "rabbit")],
                   "Bagian tersulit bukan tangan yang memegang gunting, melainkan tangan lain "
                   "yang harus memutar kertas. Perlihatkan gerakannya pelan-pelan sekali lalu "
                   "biarkan anak menemukan caranya sendiri. Potongan yang berbelok keluar garis "
                   "tetap dihitung berhasil.")
    cut_lines_page("Gunting Garis Gelombang", "Gunting mengikuti ombaknya.",
                   [("gelombang", "whale"), ("gelombang", "octopus"),
                    ("gelombang", "shrimp"), ("gelombang", "crab")],
                   "Kertasnya yang diputar, bukan guntingnya yang dimiringkan, dan ini biasanya "
                   "baru dikuasai di usia empat tahun. Kalau anak belum bisa, gunting lurus "
                   "melewati ombaknya juga tidak apa-apa. Berhenti sebelum anak frustrasi.")
    cut_lines_page("Gunting Zigzag", "Gunting mengikuti gigi gergajinya.",
                   [("zigzag", "dinosaur"), ("zigzag", "snake"), ("zigzag", "chameleon"),
                    ("zigzag", "boar")],
                   "Berhenti di setiap sudut, putar kertas, lalu potong lagi. Ini halaman "
                   "tersulit di bagian gunting dan banyak anak tiga tahun belum siap. Boleh "
                   "dikerjakan bersama dengan Anda memegang kertasnya dan anak menggunting.")
    cut_shape_page("Gunting Bentuk Dasar", "Gunting mengikuti garis putus-putus.",
                   [("M50 6 L94 50 L50 94 L6 50 Z", "butterfly", "juice"),
                    ("M6 22 H94 V78 H6 Z", "apple2", "sunny"),
                    ("M50 8 A42 42 0 1 1 49.5 8 Z", "donut", "sky"),
                    ("M50 8 L92 90 L8 90 Z", "tree", "forest")],
                   "Bentuk besar dengan sedikit sudut dikerjakan lebih dulu. Lingkaran justru "
                   "yang paling sulit karena tidak punya titik berhenti alami. Hasil guntingan "
                   "bisa ditempel di kertas kosong atau dijadikan hiasan supaya usahanya terasa "
                   "ada gunanya.")
    cut_shape_page("Gunting Bentuk Berlekuk", "Gunting mengikuti garis putus-putus.",
                   [("M50 88 C18 66 8 44 20 30 C32 18 46 24 50 34 C54 24 68 18 80 30 "
                     "C92 44 82 66 50 88 Z", "flower", "berry"),
                    ("M50 6 L62 38 L96 38 L68 58 L79 90 L50 70 L21 90 L32 58 L4 38 L38 38 Z",
                     "owl", "sunny"),
                    ("M20 62 A18 18 0 0 1 24 30 A24 24 0 0 1 64 24 A20 20 0 0 1 92 44 "
                     "A16 16 0 0 1 90 62 Z", "bird", "sky"),
                    ("M50 10 A40 40 0 1 1 49.6 10 Z", "melon", "forest")],
                   "Bentuk berlekuk butuh gunting dibuka setengah saja setiap potongan, bukan "
                   "dibuka penuh. Kalau hasilnya sobek, tempel saja di kertas lain dan lanjutkan. "
                   "Yang dilatih prosesnya, bukan bentuk akhirnya.", badge="Tantangan")
    cut_cards_page("Gunting Jadi Kartu Hewan",
                   "Gunting di garis putus-putus, lalu pakai kartunya untuk main tebak-tebakan.",
                   [("cat", "kucing"), ("dog", "anjing"), ("pig", "babi"),
                    ("monkey", "monyet"), ("rabbit", "kelinci"), ("rooster", "ayam")],
                   "Setelah digunting, sebar kartunya di lantai dan minta anak mencari satu per "
                   "satu sesuai nama yang Anda sebut. Kartu ini bisa dipakai berkali-kali "
                   "sesudah halamannya habis. Simpan di amplop supaya tidak hilang.")
    cut_cards_page("Kartu Buah dan Sayur",
                   "Gunting di garis putus-putus, lalu kelompokkan mana buah dan mana sayur.",
                   [("melon", "pisang"), ("apple2", "ceri"), ("carrot", "wortel"),
                    ("corn", "brokoli"), ("drumstick", "terong"), ("pizza", "cabai")],
                   "Mengelompokkan lebih berguna daripada menghafal nama, jadi terima alasan "
                   "apa pun yang masuk akal bagi anak. Kalau anak mengelompokkan berdasarkan "
                   "warna, itu juga cara berpikir yang sah. Kartunya bisa dipakai lagi saat "
                   "belanja atau menyiapkan makan.")
    cut_cards_page("Kartu Benda di Rumah",
                   "Gunting di garis putus-putus, lalu cari benda aslinya di rumah.",
                   [("cup", "gelas"), ("hat", "topi"), ("glasses", "sisir"),
                    ("pot", "sikat gigi"), ("key", "kunci"), ("camera", "kamera")],
                   "Mencocokkan gambar dengan benda asli di rumah membuat kartu ini terasa "
                   "berguna, bukan sekadar guntingan. Sembunyikan satu kartu lalu minta anak "
                   "menebak benda mana yang hilang kalau ia sudah hafal. Permainan itu melatih "
                   "ingatan sekaligus mengulang nama bendanya.")


# ============================================================ gaya tambahan
CSS = """
  body { margin: 0; background: #E9EAEE; }
  .kk-sprite { position: absolute; width: 0; height: 0; overflow: hidden; }
  .kk-page { margin: 0 auto 8mm; box-shadow: 0 1mm 4mm rgba(0,0,0,.12); overflow: hidden;
             position: relative; }
  .kk-header { align-items: center; }
  .kk-header__top { display: flex; align-items: center; gap: 5mm; flex-wrap: nowrap; }
  .kk-content { flex: 1; display: flex; flex-direction: column; min-height: 0; }
  .kk-content > .kk-instruction { margin: 0 0 4mm; }
  .kk-activity { flex: 1; display: flex; flex-direction: column;
                 justify-content: space-evenly; min-height: 0; }
  .kk-content > .kk-parent-note { margin-top: 5mm; }
  .kk-content--text { gap: 2mm; padding-top: 2mm; }
  .kk-svg { display: block; }
  .kk-center { display: flex; align-items: center; justify-content: center; flex: 1; min-height: 0; }
  .kk-ic { display: block; }
  .kk-pico { width: 100%; height: 100%; display: block; }
  .kk-skill-icon .kk-pico { width: 8mm; height: 8mm; }
  .kk-parent-note__icon { width: 6mm; height: 6mm; }
  .kk-parent-note__icon .kk-pico { width: 6mm; height: 6mm; }
  .kk-parent-note span:last-child { font-size: 9.5pt; line-height: 1.5; }

  .kk-contoh { font: 600 8pt/1 var(--kk-font-ui); color: var(--kk-berry);
               background: var(--kk-tint-berry); border-radius: 99px; padding: 1.4mm 3mm; }
  .kk-contoh-tag { position: absolute; top: -1mm; left: 0; }
  .kk-contoh-tag--side { flex: 0 0 20mm; display: flex; align-items: center;
                         justify-content: flex-start; margin-left: 2mm; }
  .kk-svgtag { font: 600 5px var(--kk-font-ui); fill: #E05580; }
  .kk-mark { position: absolute; inset: -12%; width: 124%; height: 124%; pointer-events: none; }
  .kk-mark--wide { inset: -6% -2%; width: 104%; height: 112%; }

  /* menelusuri garis */
  .kk-trow { display: flex; align-items: center; gap: 5mm; position: relative;
             padding-top: 3mm; }
  .kk-trow .kk-traceline { flex: 1; width: 100%; height: auto; }
  .kk-glyphrow { flex: 1; width: 100%; height: auto; }
  .kk-gl2 { font-family: var(--kk-font-trace); font-size: 24px; font-weight: 700; fill: var(--kk-ink); }

  /* mencocokkan */
  .kk-mrow { display: flex; align-items: center; gap: 3mm; }
  .kk-mcell { display: flex; align-items: center; gap: 4mm; flex: none; }
  .kk-mcell--r { flex-direction: row; }
  .kk-mgap { flex: 1; display: flex; align-items: center; justify-content: center;
             gap: 3mm; min-width: 0; }
  .kk-mline { flex: 1; height: 6mm; min-width: 0; }
  .kk-dot { width: 3.6mm; height: 3.6mm; border-radius: 50%; background: var(--kk-blueberry); flex: none; }

  /* memilih */
  .kk-choose { display: flex; align-items: center; gap: 4mm; }
  .kk-choose__t { border: 0.6mm solid var(--kk-blueberry); border-radius: 4mm; padding: 2.5mm;
                  background: var(--kk-tint-blueberry); flex: none; }
  .kk-choose__bar { width: 0.5mm; align-self: stretch; background: #E3E6EC; flex: none; }
  .kk-choose__row { flex: 1; display: flex; align-items: center; justify-content: space-evenly;
                    gap: 3mm; min-width: 0; }
  .kk-choose__row--wide { justify-content: space-around; }
  .kk-choose__o { position: relative; display: flex; align-items: center; justify-content: center; }

  /* pola */
  .kk-prow { display: flex; align-items: center; gap: 3mm; }
  .kk-pseq { display: flex; align-items: center; gap: 2mm; flex: none; }
  .kk-pans { border: 0.5mm solid var(--kk-guide-gray); border-radius: 3mm; padding: 2mm;
             display: flex; }
  .kk-pcell { display: flex; align-items: center; justify-content: center;
              width: 20mm; height: 20mm; border-radius: 3mm; background: var(--kk-tint-sunny);
              flex: none; }
  .kk-pseq .kk-pcell:nth-child(even) { background: var(--kk-tint-grape); }
  .kk-pcell--polos, .kk-pseq .kk-pcell--polos:nth-child(even) { background: transparent; }
  .kk-pcell--q { background: #fff; border: 0.6mm dashed var(--kk-berry);
                 font: 600 20pt/1 var(--kk-font-title); color: var(--kk-berry); }
  .kk-pcell--isi { background: var(--kk-tint-berry); }

  /* berhitung */
  .kk-group { border: 0.5mm solid #DCE0E8; border-radius: 5mm; padding: 3.5mm 4mm;
              background: #FBFCFD; display: flex; align-items: center; justify-content: center;
              min-width: 92mm; position: relative; }
  .kk-group--half { min-width: 58mm; flex: 1; }
  .kk-count-items { display: flex; gap: 2.5mm; flex-wrap: wrap; justify-content: center;
                    max-width: 84mm; }
  .kk-count-row { display: flex; align-items: center; justify-content: space-between; gap: 4mm; }
  .kk-boxrow { display: flex; gap: 3mm; flex: none; }
  .kk-numbox { position: relative; width: 16mm; height: 16mm; border: 0.5mm solid var(--kk-ink);
               border-radius: 3mm; display: flex; align-items: center; justify-content: center;
               font: 600 18pt/1 var(--kk-font-title); color: var(--kk-ink); }
  .kk-cmnum { width: 20mm; height: 20mm; flex: none; border: 0.6mm solid var(--kk-leaf);
              border-radius: 50%; display: flex; align-items: center; justify-content: center;
              font: 600 20pt/1 var(--kk-font-title); color: var(--kk-leaf); }
  .kk-more { display: flex; align-items: center; gap: 3mm; }
  .kk-more__vs { font: 600 10pt/1 var(--kk-font-ui); color: var(--kk-text-muted); flex: none; }

  /* cari dan warnai */
  .kk-hunt { flex: 1; display: flex; flex-direction: column; gap: 5mm; min-height: 0; }
  .kk-hunt__legend { display: flex; gap: 6mm; justify-content: center; align-items: center; }
  .kk-hunt__legendlbl { font: 600 9pt/1 var(--kk-font-ui); color: var(--kk-text-muted); }
  .kk-hunt__legend .kk-hunt__c { width: 22mm; }
  .kk-hunt__grid { flex: 1; display: flex; flex-direction: column; justify-content: space-evenly;
                   min-height: 0; }
  .kk-hunt__row { display: flex; justify-content: space-evenly; gap: 4mm; }
  .kk-hunt__c { width: 32mm; display: block; }
  .kk-color__img { max-width: 100%; max-height: 100%; object-fit: contain; display: block; }
  .kk-color__ph { border: 0.6mm dashed var(--kk-guide-gray); border-radius: 5mm; padding: 20mm;
                  text-align: center; font: 600 11pt/1.6 var(--kk-font-ui);
                  color: var(--kk-text-muted); }

  /* jalan berliku */
  .kk-scene { width: 100%; height: 100%; max-height: 100%; object-fit: contain; }

  /* perasaan */
  .kk-facegrid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; place-items: center;
                 gap: 4mm; min-height: 0; }
  .kk-face { display: flex; flex-direction: column; align-items: center; gap: 2mm; }
  .kk-face__label { font: 600 12pt/1 var(--kk-font-ui); color: var(--kk-text); }
  .kk-facesvg { width: 46mm; height: 46mm; }

  /* halaman penuh gambar */
  .kk-fullpage { padding: 0 !important; overflow: hidden; }
  .kk-fullpage__img { width: 100%; height: 100%; object-fit: cover; display: block; }

  /* gunting */
  .kk-cutpage { padding: 0 !important; display: flex; flex-direction: row; }
  .kk-tear { width: 24mm; flex: none; position: relative; display: flex;
             flex-direction: column; align-items: center; justify-content: center; gap: 3mm;
             border-right: 0.6mm dashed var(--kk-berry); }
  .kk-tear__ic { width: 6mm; height: 6mm; color: var(--kk-berry); }
  .kk-tear__ic .kk-pico { width: 6mm; height: 6mm; }
  .kk-tear__line { display: none; }
  .kk-tear__txt { writing-mode: vertical-rl; transform: rotate(180deg);
                  font: 600 8pt/1 var(--kk-font-ui); color: var(--kk-berry);
                  max-height: 150mm; text-align: center; }
  .kk-cutpage__in { flex: 1; height: 100%; box-sizing: border-box; display: flex;
                    flex-direction: column; padding: 14mm 14mm 10mm 10mm;
                    min-width: 0; min-height: 0; overflow: hidden; }
  .kk-cut-strip { display: flex; align-items: center; gap: 4mm; }
  .kk-cut-ico { width: 8mm; height: 8mm; color: var(--kk-berry); flex: none; }
  .kk-cut-ico .kk-pico { width: 8mm; height: 8mm; }
  .kk-cutsvg { flex: 1; height: 13mm; min-width: 0; }
  .kk-cutsvg--short { flex: 0 0 42mm; }
  .kk-cutfill { flex: 1; }
  .kk-cutgrid2 { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 4mm;
                 min-height: 0; }
  .kk-cutcell { position: relative; display: flex; align-items: center; justify-content: center; }
  .kk-cutshape { width: 62mm; height: 62mm; max-height: 100%; }
  .kk-cutcell__ic { position: absolute; right: 2mm; bottom: 2mm; }
  .kk-cardgrid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 0; min-height: 0; }
  .kk-card { border: 1mm dashed var(--kk-berry); border-radius: 3mm; margin: -0.5mm;
             display: flex; flex-direction: column; align-items: center; justify-content: center;
             gap: 2mm; }
  .kk-card__lbl { font: 600 11pt/1 var(--kk-font-ui); color: var(--kk-text); }

  /* daftar isi */
  .kk-toc__list { list-style: none; margin: 0; padding: 0; flex: 1;
                  display: flex; flex-direction: column; justify-content: space-evenly; }
  .kk-toc__i { display: flex; align-items: baseline; gap: 3mm;
               font: 600 14pt/1 var(--kk-font-ui); color: var(--kk-text); }
  .kk-toc__no { width: 9mm; height: 9mm; flex: none; border-radius: 50%;
                background: var(--kk-tint-grape); color: var(--kk-grape);
                display: flex; align-items: center; justify-content: center; font-size: 11pt; }
  .kk-toc__d { flex: 1; border-bottom: 0.4mm dotted #C9CEDA; }
  .kk-toc__p { color: var(--kk-text-muted); font-size: 12pt; }
  .kk-toc__no--kosong { background: transparent; }

  /* sampul belakang */
  .kk-back { padding: 0 !important; background: #4E9E52; color: #fff; }
  .kk-back__in { padding: 26mm 20mm; display: flex; flex-direction: column; height: 100%;
                 box-sizing: border-box; }
  .kk-logo--inv .kk-logo__name { color: #fff; }
  .kk-logo--inv .kk-logo__mark { background: #fff; }
  .kk-back__lead { font: 600 20pt/1.2 var(--kk-font-title); margin: 8mm 0 6mm; }
  .kk-back__p { font: 400 11pt/1.6 var(--kk-font-ui); margin: 0 0 5mm; max-width: 150mm; }
  .kk-seri { margin-top: auto; }
  .kk-seri__t { font: 600 9pt/1 var(--kk-font-ui); opacity: .85; }
  .kk-seri__row { display: flex; align-items: flex-end; gap: 3mm; margin-top: 4mm; }
  .kk-seri__i { width: 16mm; border-radius: 3mm 3mm 0 0; background: rgba(255,255,255,.35);
                color: #fff; display: flex; align-items: flex-end; justify-content: center;
                padding-bottom: 3mm; font: 600 16pt/1 var(--kk-font-title); }
  .kk-seri__i--on { background: #fff; color: #4E9E52; }
  .kk-back__ig { font: 600 11pt/1 var(--kk-font-ui); margin: 6mm 0 0; opacity: .95; }
  .kk-serigrid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 5mm;
                 min-height: 0; }
  .kk-seri__card { border: 0.6mm solid #DCE0E8; border-radius: 5mm; padding: 5mm;
                   display: flex; flex-direction: column; gap: 1.5mm; }
  .kk-seri__head { display: flex; align-items: baseline; justify-content: space-between; }
  .kk-seri__n { font: 600 9pt/1 var(--kk-font-ui); color: var(--kk-text-muted); }
  .kk-seri__p { font: 400 8.5pt/1.5 var(--kk-font-ui); color: var(--kk-text-muted);
                margin: 1mm 0 0; }
  .kk-seri__card--on { border-color: var(--kk-leaf); background: var(--kk-tint-leaf); }
  .kk-seri__u { font: 600 15pt/1 var(--kk-font-title); color: var(--kk-blueberry); }
  .kk-seri__d { font: 600 9.5pt/1.35 var(--kk-font-ui); color: var(--kk-blueberry); }
  .kk-seri__l { margin: 1.5mm 0 0; padding-left: 4.5mm;
                font: 400 8.5pt/1.6 var(--kk-font-ui); color: var(--kk-text); }

  @media print {
    body { background: #fff; }
    .kk-page { margin: 0; box-shadow: none; }
  }
"""


def main():
    sampul_depan()
    panduan_orang_tua()             # halaman 1
    NUM[0] = 2                      # halaman 2 disediakan untuk daftar isi
    for f in (bagian_1, bagian_2, bagian_3, bagian_4, bagian_5,
              bagian_6, bagian_7, bagian_8, bagian_9):
        f()
    bundel_lainnya()
    sampul_belakang()

    daftar_isi()
    PAGES.insert(2, PAGES.pop())    # daftar isi jadi lembar ketiga

    tulis_index()
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Kertas Kecil - Buku Aktivitas Anak Usia 3 Tahun</title>
<link rel="stylesheet" href="style.css">
<style>{CSS}</style>
</head>
<body>
{sprite()}
{chr(10).join(PAGES)}
</body>
</html>"""
    (ROOT / "worksheet.html").write_text(html)
    print(f"total lembar: {len(PAGES)} | halaman bernomor: {NUM[0]}")
    print(f"aset terpakai: {len(_sym)} dari {len(FILES)}")
    minim = sorted(k for k in PAKAI if _kaya_warna(k) < 3)
    if minim:
        print("gaya tidak seragam, aset ini nyaris tanpa warna:", ", ".join(minim))
    sering = sorted(PAKAI.items(), key=lambda x: -x[1])[:12]
    print("paling sering muncul:", ", ".join(f"{k} {n}x" for k, n in sering))
    kurang = [f"warnai_{i}.jpeg" for i in range(1, 6) if not (ASSET_DIR / f"warnai_{i}.jpeg").exists()]
    if kurang:
        print("gambar mewarnai belum ada:", ", ".join(kurang))


if __name__ == "__main__":
    main()
