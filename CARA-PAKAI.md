# Kertas Kecil

Buku aktivitas printable untuk anak usia 3 tahun. 71 lembar A4, dikerjakan
cukup dengan krayon dan gunting.

## Alur kerja

    python3 gen.py      # menulis worksheet.html dan svg/INDEX.md
    python3 check.py    # memeriksa luapan, keluar kode 1 kalau ada masalah

Buka `worksheet.html` di Chrome dari dalam folder repo, bukan dari Downloads,
karena berkasnya menunjuk ke `style.css`, `assets/`, dan `svg/` lewat path
relatif. Cetak dengan Cmd+P, margin None, background graphics ON.

`check.py` butuh Playwright sekali pasang:

    pip install playwright && playwright install chromium

Setiap kali generator jalan, ia melaporkan jumlah lembar, jumlah aset yang
terpakai, dan dua belas aset yang paling sering muncul. Angka terakhir itu
dipakai untuk mendeteksi gambar yang terlalu sering diulang.

## Struktur buku

Sampul depan, panduan orang tua, daftar isi, sembilan bagian, halaman bundel
lainnya, lalu sampul belakang. Bagian gunting ada di blok terakhir. Setiap
halaman gunting punya garis potong vertikal jauh dari punggung buku supaya
lembarnya bisa dilepas.

## Menambah SVG

Taruh berkas baru di `svg/`. Otomatis terdaftar memakai nama filenya tanpa
`-svgrepo-com` dan tanpa ekstensi, jadi `panda-svgrepo-com.svg` bisa langsung
dipakai sebagai `ic("panda", 24)`. Alias pendek bisa ditambahkan di dict
`FILES`, pengelompokan untuk `svg/INDEX.md` ada di dict `KATEGORI`.

Beberapa SVG dari svgrepo isinya sedikit melewati viewBox sendiri. Kalau
`check.py` melaporkan svg keluar viewBox, ganti aset itu dengan yang lain.

Gaya gambar di dalam bundel harus seragam, yaitu berwarna penuh, bukan line
art. Generator memeriksa jumlah warna tiap aset yang dipakai dan memperingatkan
kalau ada yang nyaris tanpa warna. Kalau peringatan itu muncul, ganti asetnya.

## Gambar dari luar

Semua gambar penuh halaman dibaca dari folder `assets/`:

- `cover_depan.jpeg`
- `bagian_1.jpeg` sampai `bagian_9.jpeg`
- `warnai_1.jpeg` sampai `warnai_5.jpeg` untuk Bagian 6
- `perasaan_1.jpeg` sampai `perasaan_4.jpeg` untuk Bagian 8

Kalau ada berkas yang belum masuk, halamannya tetap terbentuk dengan kotak
penanda. Ukuran ideal 2480 x 3508 piksel untuk halaman penuh.

## Bikin bundel umur lain

Isi tiap bagian ada di fungsi `bagian_1()` sampai `bagian_9()`. Helper yang
bisa dipakai ulang:

- `trace_page`, `glyph_page`
- `match_page`, `choose_page`, `size_page`
- `pattern_page`
- `count_page`, `count_match_page`, `more_page`
- `hunt_page`, `warnai_page`, `gambar_penuh_aktivitas`
- `path_page`
- `cut_lines_page`, `cut_shape_page`, `cut_cards_page`

Bentuk huruf dan angka ada di dict `GLYPH` sebagai jejak satu garis di tengah
huruf, bukan garis luar ganda. Titik awal goresan ada di dict `MULAI`.

## Aturan isi

Setiap halaman aktivitas punya satu contoh yang sudah dikerjakan dan catatan
orang tua minimal tiga kalimat, kecuali bagian gunting yang tanpa contoh.
Halaman menelusuri garis maksimal tiga baris supaya objeknya besar. Semua
aktivitas hanya boleh butuh krayon dan gunting.
