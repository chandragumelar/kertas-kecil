#!/usr/bin/env python3
"""Periksa worksheet.html: konten yang meluap keluar halaman dan
elemen SVG yang koordinatnya keluar dari viewBox.

Jalankan:  python3 check.py
Keluar dengan kode 1 kalau ada masalah.
"""

import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("playwright belum terpasang. Jalankan:\n"
             "  pip install playwright && playwright install chromium")

ROOT = Path(__file__).parent
FILE = ROOT / "worksheet.html"
TOLERANSI_MM = 0.6          # ambang luapan yang masih dianggap wajar
MM = 96 / 25.4              # 1mm dalam piksel CSS

SKRIP = """
() => {
  const mm = 96 / 25.4;
  const hasil = [];
  document.querySelectorAll('section.kk-page').forEach((sec, i) => {
    const kotak = sec.getBoundingClientRect();
    const masalah = [];

    // 1. tinggi halaman
    if (sec.scrollHeight - sec.clientHeight > 2)
      masalah.push(`konten ${( (sec.scrollHeight - sec.clientHeight) / mm ).toFixed(1)}mm lebih tinggi dari halaman`);
    if (sec.scrollWidth - sec.clientWidth > 2)
      masalah.push(`konten ${( (sec.scrollWidth - sec.clientWidth) / mm ).toFixed(1)}mm lebih lebar dari halaman`);

    // 2. elemen anak yang keluar kotak halaman
    let luarBawah = 0, luarKanan = 0, luarKiri = 0;
    sec.querySelectorAll('*').forEach(el => {
      if (!el.getClientRects().length) return;
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return;
      luarBawah = Math.max(luarBawah, r.bottom - kotak.bottom);
      luarKanan = Math.max(luarKanan, r.right - kotak.right);
      luarKiri  = Math.max(luarKiri,  kotak.left - r.left);
    });
    if (luarBawah > 2) masalah.push(`elemen keluar ${ (luarBawah/mm).toFixed(1) }mm di bawah`);
    if (luarKanan > 2) masalah.push(`elemen keluar ${ (luarKanan/mm).toFixed(1) }mm di kanan`);
    if (luarKiri  > 2) masalah.push(`elemen keluar ${ (luarKiri /mm).toFixed(1) }mm di kiri`);

    // 3. kartu yang isinya terpotong oleh kotaknya sendiri
    sec.querySelectorAll('.kk-seri__card, .kk-card, .kk-group').forEach(el => {
      if (el.scrollHeight - el.clientHeight > 2)
        masalah.push(`isi kartu terpotong ${((el.scrollHeight - el.clientHeight) / mm).toFixed(1)}mm`);
    });

    // 4. isi SVG yang melampaui viewBox
    sec.querySelectorAll('svg[viewBox]').forEach(svg => {
      if (svg.closest('.kk-sprite')) return;
      const vb = svg.viewBox.baseVal;
      let bb;
      try { bb = svg.getBBox(); } catch (e) { return; }
      const t = 0.5;
      const keluar = [];
      if (bb.x < vb.x - t) keluar.push('kiri');
      if (bb.y < vb.y - t) keluar.push('atas');
      if (bb.x + bb.width  > vb.x + vb.width  + t) keluar.push('kanan');
      if (bb.y + bb.height > vb.y + vb.height + t) keluar.push('bawah');
      if (keluar.length)
        masalah.push(`svg .${svg.getAttribute('class') || '(tanpa kelas)'} keluar viewBox di ${keluar.join(', ')}`);
    });

    if (masalah.length) {
      const judul = sec.querySelector('.kk-title');
      const nomor = sec.querySelector('.kk-footer > span:last-child');
      hasil.push({
        lembar: i + 1,
        halaman: nomor ? nomor.textContent.trim() : '-',
        judul: judul ? judul.textContent.trim() : '(tanpa judul)',
        masalah: [...new Set(masalah)]
      });
    }
  });
  return hasil;
}
"""


def main():
    if not FILE.exists():
        sys.exit("worksheet.html belum ada. Jalankan python3 gen.py dulu.")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 900, "height": 1300})
        pg.goto(FILE.as_uri())
        pg.wait_for_timeout(3000)
        jumlah = pg.eval_on_selector_all("section.kk-page", "els => els.length")
        hasil = pg.evaluate(SKRIP)
        b.close()

    print(f"diperiksa {jumlah} lembar")
    if not hasil:
        print("bersih, tidak ada yang meluap")
        return 0
    print(f"\n{len(hasil)} lembar bermasalah:\n")
    for h in hasil:
        print(f"  lembar {h['lembar']} (halaman {h['halaman']}) — {h['judul']}")
        for m in h["masalah"]:
            print(f"      {m}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
