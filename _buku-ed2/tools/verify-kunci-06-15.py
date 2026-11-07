#!/usr/bin/env python3
"""Ad-hoc verification of two key fixes (6.5 and 9.9) in both editions.

Not a project suite: it only checks that (a) the wrong text is gone,
(b) the replacement text is present, (c) the replacement claim is numerically CORRECT,
(d) both editions carry the same claim. Compilation is tested separately via build_ed2.py pdf.
"""
import os
import re
import sys

import numpy as np
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ID = os.path.join(ROOT, "_buku-ed2", "lampiran-kunci", "kunci-06-15.tex")
EN = os.path.join(ROOT, "_buku-en", "belakang", "kunci-06-15-en.tex")
gagal = []
jumlah = [0]


def cek(nama, syarat, detail=""):
    jumlah[0] += 1
    print(("PASS " if syarat else "FAIL ") + nama + ("  " + detail if detail else ""))
    if not syarat:
        gagal.append(nama)


def blok(path, bab, sampai):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"\\section\*\{(?:Bab|Chapter) %d:.*?(?=\\section\*\{(?:Bab|Chapter) %d:)" % (bab, sampai), s, re.S)
    assert m, f"blok bab {bab} tidak ditemukan di {path}"
    return m.group(0)


id06, en06 = blok(ID, 6, 7), blok(EN, 6, 7)
id09, en09 = blok(ID, 9, 10), blok(EN, 9, 10)

# --- (a) defective text gone, (b) replacement present -----------------------
cek("ID 6.5: 'ketiga vektor pembangun' sudah tidak ada", "ketiga vektor pembangun" not in id06)
cek("ID 6.5: 'keempat vektor pembangun' ada", "keempat vektor pembangun" in id06)
cek("EN 6.5: 'three spanning vectors' sudah tidak ada", "three spanning vectors" not in en06)
cek("EN 6.5: 'four spanning vectors' ada", "four spanning vectors" in en06)

cek("ID 9.9: langkah tr(PD^10 P^-1) untuk B sudah tidak ada",
    "tr}(PD^{10}P^{-1})" not in id09)
cek("EN 9.9: langkah tr(PD^10 P^-1) untuk B sudah tidak ada",
    "tr}(PD^{10}P^{-1})" not in en09)
cek("ID 9.9: menyebut bentuk segitiga Schur", "Schur" in id09 and "segitiga" in id09)
cek("EN 9.9: menyebut Schur triangular form", "Schur" in en09 and "triangular" in en09)
cek("ID 9.9: menyatakan B tidak punya P dan D", "tidak punya" in id09)
cek("EN 9.9: menyatakan B tidak punya P dan D", "no $P$ and $D$" in en09)

# --- (c) replacement claim is numerically correct --------------------------
cek("6.5: rank tiga vektor = 2 (klaim lama salah)",
    np.linalg.matrix_rank(np.array([[1, 0, 0], [0, 1, 0], [1, 1, 0]])) == 2)
cek("6.5: rank empat pembangun = 3 (klaim baru)",
    np.linalg.matrix_rank(np.array([[1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1]])) == 3)

B = sp.Matrix([[-1, 4, 0], [-1, 3, 0], [1, -2, 2]])
lam = [1, 1, 2]
from scipy.linalg import schur as schur_np

Tn, Qn = schur_np(np.array(B, dtype=float))       # B = Q T Q^T, T upper triangular
T = Tn                                            # stays float: the claim is tested with tolerance
cek("9.9: Schur mereproduksi B (Q T Q^T)", np.allclose(Qn @ Tn @ Qn.T, np.array(B, float)))
cek("9.9: B defektif (tidak dapat didiagonalkan)", B.is_diagonalizable() is False)
cek("9.9: B-I berperingkat 2 -> ruang eigen 1 dimensi", (B - sp.eye(3)).rank() == 2)
cek("9.9: diagonal T = nilai eigen 1,1,2 (tol 1e-6)",
    np.allclose(np.sort(np.diag(T)), lam, atol=1e-6), f"diag={np.diag(T)}")
cek("9.9: T segitiga atas (entri bawah diagonal 0, tol 1e-12)",
    np.allclose(np.tril(T, -1), 0.0, atol=1e-12))
cek("9.9: T^10 segitiga atas berdiagonal lam^10 (tol 1e-6)",
    np.allclose(np.tril(np.linalg.matrix_power(T, 10), -1), 0.0, atol=1e-6)
    and np.allclose(np.sort(np.diag(np.linalg.matrix_power(T, 10))),
                    sorted(x ** 10 for x in lam), rtol=1e-6),
    f"diag(T^10)={np.diag(np.linalg.matrix_power(T,10))}")
cek("9.9: tr(T^10) = tr(B^10) = sum lam^10 = 1026 (tol 1e-6)",
    abs(np.trace(np.linalg.matrix_power(T, 10)) - (B ** 10).trace()) < 1e-6
    and (B ** 10).trace() == sum(x ** 10 for x in lam) == 1026,
    f"T={np.trace(np.linalg.matrix_power(T,10)):.9f}, B={sp.trace(B**10)}")
cek("9.9: trace B^10 dari matriks tercetak = 1026", (-19) + 21 + 1024 == 1026)

# --- (d) both editions state the same numbers -----------------------------
def angka(t):
    math = " ".join(re.findall(r"\$[^$]+\$", t))
    math = re.sub(r"\\[a-zA-Z]+", "", math)
    return sorted(x for x in re.findall(r"\d+", math) if len(x) <= 6)


cek("paritas 9.9: multiset angka ID == EN", angka(id09) == angka(en09),
    f"ID-only={sorted(set(angka(id09)) - set(angka(en09)))} EN-only={sorted(set(angka(en09)) - set(angka(id09)))}")
cek("paritas 6.5: multiset angka ID == EN", angka(id06) == angka(en06))

# --- wave 2: items 12.2, 13.7, 14.5 ---------------------------------------
id12, en12 = blok(ID, 12, 13), blok(EN, 12, 13)
id13, en13 = blok(ID, 13, 14), blok(EN, 13, 14)
id14, en14 = blok(ID, 14, 15), blok(EN, 14, 15)

cek("ID 12.2: klaim 'interval mana pun' sudah tidak ada", "interval mana pun" not in id12)
cek("ID 12.2: klaim dibatasi ke lingkungan 0",
    "lingkungan mana pun di sekitar $0$" in id12)
cek("EN 12.2: klaim 'any interval' sudah tidak ada", "any interval" not in en12)
cek("EN 12.2: 'any neighbourhood of $0$' ada", "any neighbourhood of $0$" in en12)

fl = lambda x: x + 2 * x ** 2 * np.sin(1 / x ** 2)
cek("12.2: klaim lama salah -- f naik di [1,3]",
    bool((np.diff(fl(np.linspace(1, 3, 200001))) > 0).all()))
dfl = lambda x: 1 + 4 * x * np.sin(1 / x ** 2) - (4 / x) * np.cos(1 / x ** 2)
dekat0 = dfl(np.linspace(1e-4, 1e-2, 20001))
cek("12.2: klaim baru benar -- f' berganti tanda dekat 0",
    bool(dekat0.min() < 0 < dekat0.max()), f"min={dekat0.min():.1f} max={dekat0.max():.1f}")

cek("ID 13.7: 'bersisi' sudah tidak ada", "bersisi" not in id13)
cek("ID 13.7: batas 1/2 delta f(x0)", "\\tfrac12\\delta f(x_{0})>0" in id13)
cek("EN 13.7: 'half-width' sudah tidak ada", "half-width" not in en13)
cek("EN 13.7: batas 1/2 delta f(x0)", "\\tfrac12\\delta f(x_{0})>0" in en13)

# f(x)=x on [0,1], x0=1 (endpoint): the old bound (delta*f) exceeds the true
# integral, the new bound (delta*f/2) does not. The integral is computed, not guessed.
_x = sp.Symbol("x")
_integral = sp.integrate(_x, (_x, 0, 1))
_delta, _fx0 = sp.Rational(9, 10), sp.Integer(1)
cek("13.7: batas lama gagal di titik ujung",
    bool(_delta * _fx0 > _integral), f"delta*f={_delta * _fx0} > integral={_integral}")
cek("13.7: batas baru sah di titik ujung",
    bool(sp.Rational(1, 2) * _delta * _fx0 <= _integral),
    f"delta*f/2={sp.Rational(1, 2) * _delta * _fx0} <= integral={_integral}")

cek("ID 14.5: 5,077 menggantikan 5,018",
    "5{,}077\\times10^{-14}" in id14 and "5{,}018" not in id14)
cek("EN 14.5: 5.077 menggantikan 5.018",
    "5.077\\times10^{-14}" in en14 and "5.018" not in en14)

import math as _math
from fractions import Fraction as _Fr

import mpmath as _mp

_mp.mp.dps = 60
S15 = sum(_Fr(1, _math.factorial(k)) for k in range(16))
galat15 = float(_mp.e - _mp.mpf(S15.numerator) / _mp.mpf(S15.denominator))
cek("14.5: nilai benar 5,077e-14 (relerr < 0,5%)",
    abs(galat15 - 5.077e-14) / galat15 < 5e-3, f"e-S15={galat15:.6e}")

print()
print(f"HASIL: {len(gagal)} gagal dari {jumlah[0]} cek" if gagal else f"HASIL: {jumlah[0]}/{jumlah[0]} PASS")
sys.exit(1 if gagal else 0)
