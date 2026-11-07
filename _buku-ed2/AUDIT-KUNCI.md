# Aturan audit kunci jawaban Bab 6–32 (dibaca SETIAP auditor)

Tugasmu: memeriksa apakah **kunci jawaban benar-benar menjawab soalnya** dan apakah
**setiap angka di dalamnya benar**. Gerbang paritas hanya membuktikan edisi ID dan EN
sama; ia TIDAK membuktikan kebenaran. Kesalahan yang dulu lolos: kunci menjawab
pernyataan yang berbeda dari soalnya, faktor `n-1` hilang, arah ketaksamaan terbalik,
`16 GiB` padahal `16 TiB`.

## Sumber yang dibaca (jangan mengubah apa pun)

- Soal: `chNN.tex`, lingkungan `\begin{latihan} ... \end{latihan}`.
- Kunci: `lampiran-kunci/kunci-*.tex`, blok `\section*{Bab NN: ...}` sampai
  `\section*{` berikutnya atau akhir berkas. Butir ke-k = `\item` ke-k.
- Pemetaan sudah diverifikasi: 304 butir soal ↔ 304 butir kunci, 1:1. **Jangan**
  mengusulkan menambah/menghapus butir.

## Larangan keras

1. **Jangan menyunting berkas apa pun.** Kamu hanya melapor; induk yang menerapkan
   perbaikan ke kedua edisi. (Menyunting sendiri membuat edisi ID/EN menyimpang.)
2. **Jangan mengarang angka.** Setiap angka yang kamu klaim harus punya output
   perhitungan nyata di laporanmu: perintah + hasil. Bila soal berupa "jalankan blok
   lab", tulis `BUTUH-LAB` — jangan menebak.
3. **Jangan menilai gaya, panjang, atau mutu prosa.** Hanya: apakah kunci menjawab
   soal itu, dan apakah angkanya benar.
4. Asimetri yang sah: satu soal boleh punya beberapa jalan; kunci yang berbeda jalan
   tetap BENAR bila hasil dan klaimnya benar.

## Prosedur per butir

1. Baca soal ke-k dan kunci ke-k. Tanyakan: apakah kunci menjawab **persis** yang
   diminta soal (objek, arah, syarat, kuantitas)?
2. Ekstrak setiap klaim yang bisa diuji: angka, matriks, akar, peluang, dimensi,
   nilai eigen, kompleksitas, hasil hitung eksplisit.
3. Hitung ulang dengan Python (`source ~/venv/bin/activate`; numpy/scipy/sympy
   tersedia). Untuk Bab 28 (Lean) jalankan `~/.elan/bin/lean` pada berkas sementara
   di `~/.hermes/cache/scratch/`, jangan di repo. Ingat: `omega` aksiomanya
   `[propext, Quot.sound]` dan tidak menutup tujuan non-linear.
4. Bandingkan. Toleransi numerik: relatif 1e-9 untuk eksak, 1e-6 untuk float,
   kecuali soal menyatakan pembulatan.

## Format laporan (ringkas, wajib)

```
BAB NN — 9 butir: 8 BENAR, 1 SALAH
- NN.4 SALAH
  soal: <ringkas 1 baris>
  kunci lama: <potongan persis yang salah>
  hitung: <perintah> -> <hasil>
  seharusnya: <teks LaTeX pengganti, siap tempel, tetap ASCII dan gaya berkas>
- NN.7 RAGU
  alasan: <1 baris>; butuh: <apa>
```
Butir BENAR cukup satu baris: `NN.2 BENAR (dim W=1; numpy rank=1)`.
Tutup dengan: `RINGKASAN: benar=X salah=Y ragu=Z butuh-lab=W`.

Jangan menyalin ulang isi bab. Laporan harus < 120 baris.
