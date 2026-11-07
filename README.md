# Kenapa Mesin Bisa Salah? / Why Machines Can Be Wrong

Buku ajar bertingkat — dari aljabar linear sampai keamanan *machine learning* —
dalam **dua edisi paralel**: bahasa Indonesia dan bahasa Inggris. Setiap bab
membawa jalur pembaca bertingkat (anak, mahasiswa, dosen, peneliti), contoh
hitung yang angkanya berasal dari eksekusi nyata, latihan, dan kunci jawaban.

**Penulis:** Afiq Andico Pangimpian
**Edisi:** Pertama, 2026 · **32 bab**, 6 bagian, 304 latihan, 304 kunci
**Lisensi:** teks CC BY 4.0 · kode MIT · **Halaman buku:** 643 (ID) / 638 (EN)

| Berkas | Isi |
|---|---|
| `Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf` | Edisi Indonesia, 643 halaman, 3,54 MB |
| `Kitab-STEM-Why-Machines-Can-Be-Wrong.pdf` | Edisi Inggris, 638 halaman, 3,80 MB |
| `_buku-ed2/` | Sumber LaTeX edisi Indonesia + gerbang mutu + alat verifikasi |
| `_buku-en/` | Sumber LaTeX edisi Inggris + gerbang paritas terjemahan |

## Isi buku

Enam bagian, 32 bab: **(I)** fondasi matematis — aljabar linear, analisis real,
peluang, optimasi; **(II)** pembelajaran mesin — generalisasi, evaluasi yang
jujur; **(III)** metode formal dengan Lean 4; **(IV)** adversarial machine
learning dan pertahanannya; **(V)** batas serangan, NIDS, kriptografi pasca-
kuantum; **(VI)** privasi diferensial dan fondasi matematis QML.

## Merakit ulang

Prasyarat: TeX Live (pdflatex, makeindex), Python 3 dengan `numpy`, `scipy`,
`sympy`; Lean 4 (opsional, hanya untuk pemeriksa Bab 28).

```bash
make check   # gerbang mutu: 32 bab, kata badan, glosarium, pemetaan latihan<->kunci
make test    # uji kerangka (36 cek) + kompilasi sandbox
make pdf     # rakit PDF edisi Indonesia
cd _buku-en && python3 tools/cek-en.py --pdf   # rakit + gerbang PDF edisi Inggris
```

Rakitan bersifat **reproduksibel**: dua rakitan berturut-turut menghasilkan
sha256 identik.

| Artefak | sha256 |
|---|---|
| Edisi ID | `d66d9c2f30704c30df98d0e666acc2f14f8be00988fcb102cc966fca6de614e9` |
| Edisi EN | `64e0e90f06a8aa6dac840800a619a89d073b60ccb41824821c4d2da272172f9c` |

## Verifikasi yang bisa kamu jalankan sendiri

Semua angka di kunci jawaban diperiksa ulang dengan perhitungan nyata, dan
pemeriksanya ikut di repo — bukan klaim:

```bash
cd _buku-ed2
python3 tools/cek-cacah-kunci.py      # 304 latihan <-> 304 kunci, 1:1 di 32 bab
python3 tools/cek-kunci-01-05.py      # angka kunci Bab 1-5
python3 tools/verify-kunci-06-15.py   # 37 cek (6.5, 9.9, 12.2, 13.7, 14.5)
python3 tools/verify-kunci-16-23.py   # 36 cek (18.8, 18.10, 19.10, 20.4, 20.7)
python3 tools/verify-kunci-21-25.py   # 38 cek (21.5, 21.9, 22.10, 25.5, 25.9)
python3 tools/verify-kunci-26-32.py   # 20 cek, menjalankan Lean di tools/lean-28/
cd ../_buku-en
python3 tools/cek-en.py               # paritas kedua edisi, 32 bab
python3 tools/cek-belakang.py         # 13 bagian belakang
```

Audit kunci dijalankan dalam enam gelombang berpedoman `_buku-ed2/AUDIT-KUNCI.md`
dan menemukan **23 butir kunci cacat** (14 di Bab 6–25, 9 di Bab 26–32), ditambah
satu soal (21.5) dan satu angka teks bab (Bab 29); semuanya sudah diperbaiki di
kedua edisi.

## Batas yang diketahui (jujur, bukan disembunyikan)

- **30.5** menuntut tiga angka pada model dua lapis yang lebarnya tidak disebutkan
  soalnya; kuncinya hanya memberi ramalan kualitatif.
- **29.4**: angka 95,48 persen sah untuk satu tarikan acak (`rng(1)`/`rng(2)`;
  `rng(0)` memberi 95,64).
- Blok `lab` Bab 29 memuat pustaka serangannya saja tanpa driver pelatihan, jadi
  tabel 29.5/29.9 tidak bisa diturunkan ulang dari repo tanpa menulis driver.
- Paritas ID↔EN membuktikan terjemahan setia pada sumbernya, **bukan** bahwa
  sumbernya benar; kebenaran isi dijaga oleh audit kunci di atas.
- Repo ini memuat **karya tulis dan kode**, bukan kitab sumber berhak cipta yang
  dipakai sebagai rujukan penulisan.

## Sitasi

Lihat `CITATION.cff`. Bentuk ringkas:

> Pangimpian, A. A. (2026). *Kenapa Mesin Bisa Salah? Dari Aljabar Linear sampai
> Keamanan Machine Learning* (Edisi Pertama, v1.0.0). CC BY 4.0.

## Lisensi

- **Teks buku** (kedua edisi, termasuk PDF): [CC BY 4.0](LICENSE) — bebas dipakai,
  dibagikan, dan diadaptasi dengan atribusi.
- **Kode** (skrip rakit, gerbang, pemeriksa di `tools/`): [MIT](LICENSE-CODE).
