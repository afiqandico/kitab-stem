#!/usr/bin/env python3
"""Ad-hoc verification of the wave-3 fixes (Chapters 16-20): 18.8, 18.10, 19.10, 20.4, 20.7.

Ad-hoc, not a project suite. Each check demands (a) the defective text is gone, (b) the
replacement text is present, (c) the replacement numbers are correct per exact/numeric computation.
"""
import os
import re
import sys

import numpy as np
import sympy as sp
from scipy.stats import binom, norm

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ID = os.path.join(ROOT, "_buku-ed2", "lampiran-kunci", "kunci-16-23.tex")
EN = os.path.join(ROOT, "_buku-en", "belakang", "kunci-16-23-en.tex")
gagal, jumlah = [], [0]


def cek(nama, syarat, detail=""):
    jumlah[0] += 1
    print(("PASS " if syarat else "FAIL ") + nama + ("  " + detail if detail else ""))
    if not syarat:
        gagal.append(nama)


def blok(path, bab):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"\\section\*\{(?:Bab|Chapter) %d:.*?(?=\\section\*\{(?:Bab|Chapter) %d:)" % (bab, bab + 1),
                  s, re.S)
    if not m and bab == 23:                      # last chapter in the file: up to the end
        m = re.search(r"\\section\*\{(?:Bab|Chapter) 23:.*", s, re.S)
    assert m, f"blok {bab} tidak ditemukan di {path}"
    return m.group(0)


i18, e18 = blok(ID, 18), blok(EN, 18)
i19, e19 = blok(ID, 19), blok(EN, 19)
i20, e20 = blok(ID, 20), blok(EN, 20)

# --- 18.10 ---------------------------------------------------------------
cek("ID 18.10: 5.447,9 hilang", "5\\,447{,}9" not in i18)
cek("ID 18.10: 5.448,03 dan R=5.449", "5\\,448{,}03" in i18 and "5\\,449" in i18)
cek("ID 18.10: 'sembilan belas kali'", "sembilan belas kali" in i18)
cek("ID 18.10: 'dua puluh kali' hilang", "dua puluh kali" not in i18)
cek("EN 18.10: 5,447.9 hilang", "5\\,447.9" not in e18)
cek("EN 18.10: 'nineteen times'", "nineteen times" in e18)

s2, n = 4.55 ** 2, 20
batas = 2 * s2 / ((n - 1) * 0.02 ** 2)
cek("18.10: batas = 5448,03 -> ceil 5449", abs(batas - 5448.0263) < 1e-3 and int(np.ceil(batas)) == 5449,
    f"batas={batas:.4f}")
cek("18.10: R=5448 gagal, R=5449 lolos",
    not (4.55 * np.sqrt(2 / ((n - 1) * 5448)) <= 0.02) and (4.55 * np.sqrt(2 / ((n - 1) * 5449)) <= 0.02))
cek("18.10: tanpa (n-1) -> 19x, bukan 20x",
    abs((2 * s2 / 0.02 ** 2) / batas - 19) < 1e-9, f"rasio={(2*s2/0.02**2)/batas:.6f}")

# --- 18.8 ----------------------------------------------------------------
cek("ID 18.8: jalur f_Y ditambahkan", "lewat $f_{Y}$" in i18)
cek("EN 18.8: jalur f_Y ditambahkan", "via $f_{Y}$" in e18)
y = sp.Symbol("y", positive=True)
i1 = sp.integrate(y / (4 * sp.sqrt(y)), (y, 0, 1))
i2 = sp.integrate(y / (8 * sp.sqrt(y)), (y, 1, 9))
cek("18.8: integral f_Y = 1/6 + 13/6 = 7/3", i1 == sp.Rational(1, 6) and i2 == sp.Rational(13, 6)
    and i1 + i2 == sp.Rational(7, 3), f"{i1}+{i2}={i1+i2}")

# --- 19.10 ---------------------------------------------------------------
cek("ID 19.10: contoh (-1)^n X", "X_{n}=(-1)^{n}X" in i19)
cek("ID 19.10: contoh salah '(-1)^n' tunggal hilang", "$X_{n}=(-1)^{n}$" not in i19)
cek("EN 19.10: contoh (-1)^n X", "X_{n}=(-1)^{n}X" in e19)
# marginal stays Rademacher, but |X_n - X| = 2 for odd n
X = (-1, 1)
for n_ in (1, 2):
    marg = sorted((-1) ** n_ * x for x in X)
    assert marg == [-1, 1], marg
# push-forward: P(X_n = v) is computed, then compared with the Rademacher pmf
from fractions import Fraction as F

pmf = {v: F(1, 2) for v in (-1, 1)}          # X ~ Rademacher
for n_ in (1, 2, 7, 8):
    push = {}
    for x, px in pmf.items():
        push[(-1) ** n_ * x] = push.get((-1) ** n_ * x, F(0)) + px
    cek(f"19.10: marginal X_n (n={n_}) = Rademacher", push == pmf,
        f"{dict(sorted(push.items()))}")
cek("19.10: |X_n - X| = 2 untuk n ganjil",
    all(abs(((-1) ** 1) * x - x) == 2 for x in X))

# --- 20.4 ---------------------------------------------------------------
cek("ID 20.4: 'semata karena n' hilang", "semata karena" not in i20)
cek("ID 20.4: argumen cakupan ada", "cakupan Wald" in i20 and "0{,}921" in i20 and "0{,}943" in i20)
cek("EN 20.4: 'purely because' hilang", "purely because" not in e20)
cek("EN 20.4: argumen cakupan ada", "coverage" in e20 and "0.921" in e20 and "0.943" in e20)

z = norm.ppf(0.975)


def wilson_w(p, n_):
    d = 1 + z * z / n_
    return 2 * z * np.sqrt(p * (1 - p) / n_ + z * z / (4 * n_ * n_)) / d


def wald_w(p, n_):
    return 2 * z * np.sqrt(p * (1 - p) / n_)


cek("20.4: lebar Wilson n=40 p=0,5 = 0,2960", abs(wilson_w(0.5, 40) - 0.296009) < 1e-6,
    f"{wilson_w(0.5,40):.6f}")
cek("20.4: lebar Wilson 13/20 = 0,3860", abs(wilson_w(0.65, 20) - 0.385954) < 1e-6,
    f"{wilson_w(0.65,20):.6f}")
cek("20.4: lebar 7/20 sama dengan 13/20 (simetri)", abs(wilson_w(0.35, 20) - wilson_w(0.65, 20)) < 1e-12)


def cakupan(p, n_, wilson):
    ks = np.arange(n_ + 1)
    pm = binom.pmf(ks, n_, p)
    d = 1 + z * z / n_
    hit = 0.0
    for k, pk in zip(ks, pm):
        ph = k / n_
        if wilson:
            c = (ph + z * z / (2 * n_)) / d
            h = z * np.sqrt(ph * (1 - ph) / n_ + z * z / (4 * n_ * n_)) / d
            lo, hi = c - h, c + h
        else:
            se = np.sqrt(ph * (1 - ph) / n_) if 0 < ph < 1 else 0.0
            lo, hi = ph - z * se, ph + z * se
        hit += pk * (lo <= p <= hi)
    return hit


cw, cwi = cakupan(0.175, 40, False), cakupan(0.175, 40, True)
cek("20.4: cakupan Wald 0,921 < Wilson 0,943", abs(cw - 0.9211) < 5e-4 and abs(cwi - 0.9429) < 5e-4,
    f"Wald={cw:.4f} Wilson={cwi:.4f}")

# --- 20.7 ---------------------------------------------------------------
cek("ID 20.7: p=0,02 hilang dari blok", "p=0{,}02" not in i20)
cek("ID 20.7: p=0,31 dan IK (-0,82; 2,56)",
    "p=0{,}31" in i20 and "(-0{,}82;\\,2{,}56)" in i20)
cek("ID 20.7: asumsi est/se dinyatakan", "0{,}87" in i20 and "0{,}86" in i20)
cek("EN 20.7: p=0.02 hilang dari blok", "p=0.02" not in e20)
cek("EN 20.7: p=0.31 dan IK (-0.82; 2.56)",
    "p=0.31" in e20 and "(-0.82;\\,2.56)" in e20)

est, se = 0.87, 0.86
p0 = 2 * (1 - norm.cdf(est / se))
lo, hi = est - 1.96 * se, est + 1.96 * se
daya = norm.cdf(-1.96 - 0.5 / se) + 1 - norm.cdf(1.96 - 0.5 / se)
cek("20.7: p(δ=0) = 0,31", abs(p0 - 0.3117) < 5e-4, f"p={p0:.4f}")
cek("20.7: IK95 = (-0,82; 2,56)", abs(lo + 0.816) < 5e-3 and abs(hi - 2.556) < 5e-3,
    f"({lo:.3f};{hi:.3f})")
cek("20.7: daya(δ=0,5) = 0,09", abs(daya - 0.0895) < 5e-4, f"daya={daya:.4f}")

print()
print(f"HASIL: {len(gagal)} gagal dari {jumlah[0]} cek" if gagal else f"HASIL: {jumlah[0]}/{jumlah[0]} PASS")
sys.exit(1 if gagal else 0)
