#!/usr/bin/env python3
"""Ad-hoc verification of wave 4 (Chapters 21-25): 21.5, 21.9, 22.10, 25.5, 25.9.

Ad-hoc, not a project suite. Checks text (defect gone / replacement present) AND numbers.
Item 25.9 is tested by RERUNNING the lab block extracted from ch25.tex,
not by copying numbers from the auditor's report.
"""
import os
import re
import sys

import numpy as np
import sympy as sp
from scipy.stats import norm

BUKU = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ID = f"{BUKU}/_buku-ed2"
EN = f"{BUKU}/_buku-en"
gagal, jumlah = [], [0]


def cek(nama, syarat, detail=""):
    jumlah[0] += 1
    print(("PASS " if syarat else "FAIL ") + nama + ("  " + detail if detail else ""))
    if not syarat:
        gagal.append(nama)


def blok_kunci(path, bab):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"\\section\*\{(?:Bab|Chapter) %d:.*?(?=\\section\*\{(?:Bab|Chapter))" % bab, s, re.S)
    if not m:
        m = re.search(r"\\section\*\{(?:Bab|Chapter) %d:.*" % bab, s, re.S)
    assert m, f"blok {bab} tak ada di {path}"
    return m.group(0)


def soal(path, n):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"\\begin\{latihan\}(.*?)\\end\{latihan\}", s, re.S).group(1)
    return re.split(r"\n  \\item ", m)[n]


i21 = blok_kunci(f"{ID}/lampiran-kunci/kunci-16-23.tex", 21)
e21 = blok_kunci(f"{EN}/belakang/kunci-16-23-en.tex", 21)
i22 = blok_kunci(f"{ID}/lampiran-kunci/kunci-16-23.tex", 22)
e22 = blok_kunci(f"{EN}/belakang/kunci-16-23-en.tex", 22)
i25 = blok_kunci(f"{ID}/lampiran-kunci/kunci-24-32.tex", 25)
e25 = blok_kunci(f"{EN}/belakang/kunci-24-32-en.tex", 25)
s21i, s21e = soal(f"{ID}/ch21.tex", 5), soal(f"{EN}/ch21.tex", 5)

# --- 21.5 ---------------------------------------------------------------
cek("21.5 soal: titik asimetris (2 dan 9) di ID", "x_0=2$ dan $x_0=9$" in s21i)
cek("21.5 soal: pertanyaan kedua diperbaiki di ID", "menyempit ke nol" in s21i)
cek("21.5 soal EN ikut", "x_0=2$ and $x_0=9$" in s21e and "never" in s21e)
cek("21.5 kunci: pengakuan 'ambigu' dibuang", "ambigu" not in i21 and "ambiguous" not in e21)
cek("21.5 kunci: c(2)=0,261111 dan c(9)=0,377778",
    "0{,}261111" in i21 and "0{,}377778" in i21)
cek("21.5 kunci: batas 1,96 sigma = 0,716", "0{,}716" in i21 and "0.716" in e21)

sig2, Sxx, n, tb = 0.133333, 60.0, 9, 2.364624
c2 = 1 / n + (2 - 5) ** 2 / Sxx
c9 = 1 / n + (9 - 5) ** 2 / Sxx
cek("21.5: c(2)=0,261111", abs(c2 - 0.2611111) < 1e-6, f"{c2:.6f}")
cek("21.5: c(9)=0,377778", abs(c9 - 0.3777778) < 1e-6, f"{c9:.6f}")
cek("21.5: setengah lebar 0,9696 dan 1,0135 (pakai 1+c)",
    abs(tb * np.sqrt(sig2 * (1 + c2)) - 0.969633) < 1e-5
    and abs(tb * np.sqrt(sig2 * (1 + c9)) - 1.013492) < 1e-5,
    f"{tb*np.sqrt(sig2*(1+c2)):.6f} / {tb*np.sqrt(sig2*(1+c9)):.6f}")
cek("21.5: rumus memakai (1+c), bukan c", "133333\\,(1+c)" in i21 and "133333\\,(1+c)" in e21)
cek("21.5: limit 1,96*sigma = 0,716", abs(1.96 * np.sqrt(sig2) - 0.71569) < 1e-4)

# --- 21.9 ---------------------------------------------------------------
cek("21.9 ID: selang karangan hilang", "(-0{,}05;\\,0{,}61)" not in i21)
cek("21.9 EN: selang karangan hilang", "(-0.05;\\,0.61)" not in e21)
cek("21.9: Bonferroni 12x0,03 tetap", "0{,}36" in i21 and "0.36" in e21)
lo, hi = -0.05, 0.61
mid, se = (lo + hi) / 2, (hi - lo) / 2 / 1.959964
p_ci = 2 * (1 - norm.cdf(abs(mid / se)))
cek("21.9: selang lama -> p=0,096 (bentrok dengan p=0,03)", abs(p_ci - 0.0963) < 5e-4, f"p={p_ci:.4f}")
cek("21.9: p=0,03 menuntut selang lepas dari 0", p_ci > 0.05)
cek("21.9: Bonferroni 12*0,03=0,36", abs(12 * 0.03 - 0.36) < 1e-12)

# --- 22.10 --------------------------------------------------------------
cek("22.10 ID: rentang k dinyatakan", "k=1,\\dots,1000" in i22)
cek("22.10 EN: rentang k dinyatakan", "k=1,\\dots,1000" in e22)
it2210 = [t for t in re.split(r"\n  \\item ", i22) if "999{,}00075" in t][0]
it2210e = [t for t in re.split(r"\n  \\item ", e22) if "999.00075" in t][0]
cek("22.10: butir itu memakai s=0,4997, bukan 0,4999",
    "0{,}4997" in it2210 and "0.4997" in it2210e
    and "0{,}4999" not in it2210 and "0.4999" not in it2210e)
k = np.arange(1, 1001)
x = 999 + ((k % 7) - 3) / 4
cek("22.10: rerata k=1..1000 = 999,00075", abs(x.mean() - 999.00075) < 1e-9, f"{x.mean():.5f}")
cek("22.10: simpangan baku populasi = 0,4997", abs(x.std() - 0.49969) < 5e-5, f"{x.std():.5f}")
k0 = np.arange(0, 1000)
x0 = 999 + ((k0 % 7) - 3) / 4
cek("22.10: k=0..999 memberi 998,99925 (alasan rentang ditulis)",
    abs(x0.mean() - 998.99925) < 1e-9, f"{x0.mean():.5f}")
cek("22.10: kappa = 4,0e6", abs(x.mean() ** 2 / x.var() - 3.997e6) / 3.997e6 < 5e-3,
    f"{x.mean()**2/x.var():.4e}")

# --- 25.5 ---------------------------------------------------------------
cek("25.5 ID: vonis 'Salah'", "Salah. Teorema itu" in i25)
cek("25.5 EN: vonis 'False'", "False. The theorem is about" in e25)

# --- 25.9 (rerun the lab) ----------------------------------------------
cek("25.9 ID: tabel saturasi ada", "rentang $Z_{1}$" in i25 and "\\begin{tabular}" in i25)
cek("25.9 EN: tabel saturasi ada", "range of $Z_{1}$" in e25)
cek("25.9: klaim 'belum dijalankan' hilang",
    "butuh menjalankan blok lab" not in i25 and "require running the lab" not in e25)

src = open(f"{ID}/ch25.tex", encoding="utf-8").read()
labs = re.findall(r"\\begin\{lab\}\s*\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}", src, re.S)
# Blok lab di ch25 bertambah setelah bab disunting: definisi model tidak lagi di blok pertama.
# Jalankan blok berurutan (seperti pembaca menjalankannya) sampai semua nama model terdefinisi.
ns = {"__name__": "lab"}
import contextlib, io
for _blok in labs:
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(_blok, ns)
    except Exception:
        continue
    if all(n in ns for n in ("X", "y", "fwd", "grads", "init", "bce")):
        break
X, y, fwd, grads, init, bce = ns["X"], ns["y"], ns["fwd"], ns["grads"], ns["init"], ns["bce"]


def latih_b1(b1val, langkah=3000, lr=0.5, seed=0, nh=8):
    W1, b1, w2, b2 = init("he", np.random.default_rng(seed), nh)
    b1 = np.full(nh, float(b1val))
    Z1, H, P = fwd(X, W1, b1, w2, b2)
    L0 = bce(P, y)
    z0min, z0max = float(Z1.min()), float(Z1.max())
    jejak = []
    for t in range(langkah + 1):
        gW1, gb1, gw2, gb2 = grads(X, y, W1, b1, w2, b2)
        W1, b1 = W1 - lr * gW1, b1 - lr * gb1
        w2, b2 = w2 - lr * gw2, b2 - lr * gb2
        if t % 500 == 0:
            jejak.append(bce(fwd(X, W1, b1, w2, b2)[2], y))
    Z1, H, P = fwd(X, W1, b1, w2, b2)
    return dict(L0=L0, L=bce(P, y), akur=float(np.mean((P > 0.5) == (y > 0.5))),
                mati=int(np.sum(np.all(H <= 0, axis=0))), zmin=float(Z1.min()), zmax=float(Z1.max()),
                z0min=z0min, z0max=z0max,
                gb1=float(np.linalg.norm(gb1)), jejak=jejak)


d0, dp, dm = latih_b1(0.0), latih_b1(10.0), latih_b1(-10.0)
cek("25.9 lab: b1=0 -> Z1 awal dalam [-2,43;2,40], 0/8 mati",
    abs(d0["z0min"] + 2.43) < 0.01 and abs(d0["z0max"] - 2.40) < 0.01 and d0["mati"] == 0,
    f"[{d0['z0min']:.2f};{d0['z0max']:.2f}]")
cek("25.9 lab: b1=+10 -> Z1 awal dalam [7,57;12,41], 0/8 mati",
    abs(dp["z0min"] - 7.57) < 0.01 and abs(dp["z0max"] - 12.41) < 0.01 and dp["mati"] == 0,
    f"[{dp['z0min']:.2f};{dp['z0max']:.2f}]")
cek("25.9 lab: b1=-10 -> Z1 awal dalam [-12,43;-7,60], 8/8 mati",
    abs(dm["z0min"] + 12.43) < 0.01 and abs(dm["z0max"] + 7.60) < 0.01 and dm["mati"] == 8,
    f"[{dm['z0min']:.2f};{dm['z0max']:.2f}]")
cek("25.9: tabel menyebut rentang sebagai nilai awal",
    "(awal)" in i25 and "(initial)" in e25)
cek("25.9 lab: akurasi 1,0000 / 0,8375 / 0,5333",
    abs(d0["akur"] - 1.0) < 1e-9 and abs(dp["akur"] - 0.8375) < 5e-5 and abs(dm["akur"] - 0.5333) < 5e-5,
    f"{d0['akur']:.4f} / {dp['akur']:.4f} / {dm['akur']:.4f}")
cek("25.9 lab: L akhir 0,0163 / 0,3225 / 0,6909",
    abs(d0["L"] - 0.016349) < 1e-5 and abs(dp["L"] - 0.322527) < 1e-5 and abs(dm["L"] - 0.690923) < 1e-5,
    f"{d0['L']:.6f} / {dp['L']:.6f} / {dm['L']:.6f}")
cek("25.9 lab: L b1=+10 mulai dari 4,04", abs(dp["L0"] - 4.038386) < 1e-5, f"{dp['L0']:.6f}")
cek("25.9 lab: gradien b1 tepat nol saat mati", dm["gb1"] == 0.0, f"{dm['gb1']:.1e}")
cek("25.9 lab: 0,6909 = entropi label, bukan log 2",
    abs(dm["L"] - (-(112 / 240) * np.log(112 / 240) - (128 / 240) * np.log(128 / 240))) < 1e-9
    and abs(dm["L"] - np.log(2)) > 1e-3, f"L={dm['L']:.6f} vs log2={np.log(2):.6f}")

print()
print(f"HASIL: {len(gagal)} gagal dari {jumlah[0]} cek" if gagal else f"HASIL: {jumlah[0]}/{jumlah[0]} PASS")
sys.exit(1 if gagal else 0)
