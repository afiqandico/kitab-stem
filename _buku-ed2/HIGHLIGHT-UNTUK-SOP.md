# Dua bab unggulan untuk SoP (dan cara menyebutnya)

Dokumen kerja, bukan bagian buku. Dipakai saat menulis Statement of Purpose, ringkasan
program, atau surat pengantar: memilih dua bab yang paling murah dibuktikan dan paling
nyambung dengan riset keamanan ML.

## Pilihan: Bab 25 dan Bab 29

| | Bab 25 — Jaringan Saraf dan Turunan Balik (hlm. 424-445) | Bab 29 — Adversarial Machine Learning (hlm. 499-517) |
|---|---|---|
| Yang dibuktikan | bisa mengajar matematika terapan sampai angka | bisa menghubungkan model ke ancaman nyata |
| Bukti di dalam bab | hitung tangan 6 langkah + kode NumPy yang mencetak angka sama | definisi serangan, resep FGSM, kaitan ke IDS |
| Bukti di luar buku | repo `usb-hid-threat-lab` (pipeline deteksi), `adversarial-ml-ids-validation` | naskah ESWA |
| Risiko jika ditanya | rendah: semua angka bisa dihitung ulang di kertas | sedang: pastikan tidak mengklaim sudah menyerang sistem nyata |

Alasan memilih dua ini, bukan yang lain: keduanya satu jalur. Bab 25 mengajarkan turunan
yang dipakai menyerang; Bab 29 memakai turunan itu untuk menyerang model. Kalau penguji
bertanya "kenapa buku ini ada", jawabannya ada di sambungan dua bab itu.

## Kalimat siap pakai (English, untuk SoP)

> I wrote a 646-page textbook that teaches machine learning from the arithmetic up. In the
> neural-network chapter (Ch. 25, pp. 424-445) every derivative is first computed by hand on
> six worked steps with real numbers, and the accompanying NumPy listing reproduces those
> same numbers to seven decimals; a finite-difference check is printed next to the analytic
> gradient. The adversarial chapter (Ch. 29, pp. 499-517) then uses that gradient to derive
> FGSM, which is the threat model my intrusion-detection work evaluates against.

Kalimat pendek untuk CV (satu baris):

> Author, *Kenapa Mesin Bisa Salah?* — 32-chapter open textbook (CC BY 4.0, 646 pp.),
> hand-computed derivations plus reproducible NumPy labs; Ch. 25 and Ch. 29 cover
> backpropagation and adversarial ML.

## Yang harus disiapkan sebelum menyebutnya

1. **Halaman dan versi.** Sebut edisi (v1.0.0) dan tanggal PDF; nomor halaman di atas dari
   rakitan 2026-11-12.
2. **Tautan.** Repo GitHub publik + DOI Zenodo bila sudah terbit. Tanpa tautan, klaim
   "open textbook" melemah.
3. **Satu angka yang bisa diuji penguji.** Contoh teraman: `-0.4994798` (gradien terhadap
   bobot) dan `0.6209570` (kerugian sesudah serangan). Keduanya keluar dari kode di Bab 25
   apa adanya.
4. **Jangan menyebut** bab lain yang belum punya blok jembatan pemahaman; 31 bab lain masih
   menunggu (lihat `tools/cek-jembatan.py`).

## Catatan jujur

Bab 25 dan 29 dipilih karena buktinya paling murah diperiksa, bukan karena bab lain lemah.
Bab 16 (persamaan diferensial) dan Bab 23 (optimisasi) sama padatnya, tetapi tidak punya
sambungan langsung ke riset keamanan yang sedang dikerjakan.
