# Kertas Kecil

Buku aktivitas printable untuk anak usia 3 tahun. 76 lembar A4, dikerjakan
cukup dengan krayon dan gunting.

## Alur kerja

    python3 gen.py      # menulis worksheet.html dan svg/INDEX.md
    python3 check.py    # memeriksa luapan, keluar kode 1 kalau ada masalah

Buka `worksheet.html` di Chrome, Cmd+P, save as PDF. Margin None,
background graphics ON.

`check.py` butuh Playwright sekali pasang:

    pip install playwright && playwright install chromium

## Struktur buku

Sampul depan, daftar isi, sembilan bagian, panduan orang tua, lalu blok
gunting, ditutup sampul belakang. Halaman gunting sengaja ditaruh paling
belakang, punya garis potong vertikal di dekat punggung buku, dan setiap
halaman gunting diikuti satu halaman kosong karena lembarnya akan dilepas.

## Menambah SVG

Taruh berkas baru di `svg/`. Otomatis terdaftar memakai nama filenya tanpa
`-svgrepo-com` dan tanpa ekstensi, jadi `panda-svgrepo-com.svg` bisa langsung
dipakai sebagai `ic("panda", 24)`.

Pengelompokan untuk `svg/INDEX.md` ada di dict `KATEGORI` di dalam `gen.py`.
Kunci yang belum terdaftar masuk ke "lainnya", jadi dict itu tidak wajib
diperbarui setiap kali menambah berkas.

## Gambar dari luar

Semua gambar penuh halaman dibaca dari folder `assets/`:

- `cover_depan.jpeg`
- `bagian_1.jpeg` sampai `bagian_9.jpeg`
- `warnai_1.jpeg` sampai `warnai_5.jpeg` untuk Bagian 6

Kalau berkas mewarnai belum ada, halamannya tetap terbentuk dengan kotak
penanda dan generator menyebutkan berkas mana yang kurang.

Ukuran ideal 2480 x 3508 piksel supaya tajam saat dicetak. Rasio A4 adalah
1:1.414; berkas dengan rasio sedikit berbeda akan ter-crop tengah.

## Bikin bundel umur lain

Isi tiap bagian ada di fungsi `bagian_1()` sampai `bagian_9()`. Helper yang
bisa dipakai ulang:

- `trace_page`, `glyph_page`
- `match_page`, `choose_page`, `size_page`
- `pattern_page`
- `count_page`, `count_match_page`, `more_page`
- `hunt_page`, `warnai_page`
- `path_page`
- `cut_lines_page`, `cut_shape_page`, `cut_cards_page`
- `face_svg`

Bentuk huruf dan angka ada di dict `GLYPH` sebagai jejak satu garis di tengah
huruf, bukan garis luar ganda. Titik awal goresan ada di dict `MULAI`.

## Aturan isi

Setiap halaman aktivitas punya satu contoh yang sudah dikerjakan dan catatan
orang tua minimal tiga kalimat. Halaman menelusuri garis maksimal tiga baris
supaya objeknya besar. Semua aktivitas hanya boleh butuh krayon dan gunting.
