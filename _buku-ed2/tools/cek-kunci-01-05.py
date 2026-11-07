"""Key-number checker for Appendix D, Chapters 1-5. Every number quoted by
`lampiran-kunci/kunci-01-05.tex` is tested with an assert here; the script stops
with an error if any of them is off.

Run from `_buku-ed2/`:  python3 tools/cek-kunci-01-05.py
(output: one summary line per chapter, then `OK: seluruh angka kunci cocok`)

Honest scope: Chapters 1-5 only. The key numbers for Chapters 6-32 were checked ad hoc with
per-chapter scripts while writing, and those scripts were not archived; see "Batas yang jujur"
in README-ED2.md.
"""
import math
from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 60

# ---------- CHAPTER 1 ----------
assert [sum(k * k for k in range(1, n + 1)) for n in (1, 2, 3)] == [1, 5, 14]
assert all(sum(k * k for k in range(1, n + 1)) == n * (n + 1) * (2 * n + 1) // 6
           for n in range(1, 40))

isprime = lambda m: m > 1 and all(m % d for d in range(2, int(m ** .5) + 1))
f41 = {n: n * n + n + 41 for n in range(101)}
fails = [n for n, v in f41.items() if not isprime(v)]
assert len(fails) == 14 and len(f41) - len(fails) == 87
assert fails == [40, 41, 44, 49, 56, 65, 76, 81, 82, 84, 87, 89, 91, 96]
assert sum(1 for n in fails if isprime(n) or isprime(n + 1)) == 5
assert f41[40] == 41 ** 2 and f41[41] == 41 * 43
assert not any(2 ** n > n * n for n in (2, 3, 4)) and all(2 ** n > n * n for n in range(5, 60))
assert 2 ** 2 - 1 == 3 and isprime(3)           # n=2 breaks the claim of item 9
print(f"BAB 1: 87/101 prima; {len(fails)} gagal; n0=5; n=2 -> 3 prima")

# ---------- CHAPTER 2 ----------
def stirling(n, k):
    S = [[0] * (k + 1) for _ in range(n + 1)]
    S[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            S[i][j] = j * S[i - 1][j] + S[i - 1][j - 1]
    return S[n][k]

def parts(n):
    if n == 0:
        yield []
        return
    for p in parts(n - 1):
        for i in range(len(p)):
            yield p[:i] + [p[i] | {n}] + p[i + 1:]
        yield p + [{n}]

allp = list(parts(5))
assert stirling(5, 2) == 15 == sum(len(p) == 2 for p in allp) == 2 ** 4 - 1
assert len(allp) == 52
T = lambda s: s * (s + 1) // 2
assert T(12) + 5 == 83 and T(44) + 10 == 1000 and 990 <= 1000 < 1035
enum = [(p, k - p) for k in range(2, 30) for p in range(1, k)
        if math.gcd(p, k - p) == 1]
assert enum[29] == (7, 3) and enum[40] == (10, 1)
assert sum(1 for p in range(1, 11) if math.gcd(p, 11 - p) == 1) == 10   # phi(11)
print(f"BAB 2: S(5,2)=15 Bell=52 pi(7,5)=83 invers(1000)=(34,10) posisi30=(7,3) posisi41=(10,1)")

# ---------- CHAPTER 3 ----------
assert max(2 - F(1, n) for n in range(1, 99)) < 2 and min(2 - F(1, n) for n in range(1, 99)) == 1
for q, want in ((F(1), F(5, 4)), (F(7, 5), F(169, 120))):
    h = (2 - q * q) / (2 * q + 2)
    assert q + h == want and (q + h) ** 2 < 2
assert F(169, 120) - F(7, 5) == F(1, 120) and F(5, 4) - 1 == F(1, 4)
s3, x, xs = Decimal(3).sqrt(), F(2), [F(2)]
for _ in range(5):
    x = (x + F(3) / x) / 2
    xs.append(x)
assert (str(xs[1]), str(xs[2])) == ('7/4', '97/56')
assert xs[3] == F(18817, 10864)
errs = [abs(Decimal(v.numerator) / v.denominator - s3) / s3 for v in xs]
ratio = [f"{float(errs[i+1]/errs[i]**2):.4f}" for i in range(3)]
assert ratio == ['0.4330', '0.4949', '0.5000']
assert [f"{float(errs[i]):.5g}" for i in (1, 2, 3)] == ['0.010363', '5.3145e-05', '1.4121e-09']
assert [f"{float(errs[i]):.3g}" for i in (4, 5)] == ['9.97e-19', '4.97e-37']
print(f"BAB 3: sup=2 inf=1; 5/4 & 169/120; x2=97/56; galat x4,x5={[f'{float(errs[i]):.3g}' for i in (4,5)]}; "
      f"nisbah {ratio} -> 1/2")

# ---------- CHAPTER 4 ----------
thr = (F(11) / F(1, 1000) - 12) / 9
assert thr == F(10988, 9) and int(thr) == 1220
assert f"{11 / (9 * 1221 + 12):.4e}" == '9.9991e-04'          # error at n=1221
xs_, ys_ = (lambda n: 1 + (-1) ** n + 1 / n), (lambda n: (-1) ** n * (1 + 1 / n))
assert xs_(1000) == 2 + 1 / 1000 and xs_(999) == 1 / 999      # even -> 2, odd -> 0
assert ys_(1000) == 1 + 1 / 1000 and ys_(999) == -(1 + 1 / 999)
x, e, n = 1.0, {1: 1.0}, 1
while n < 60:
    x = math.sqrt(2 + x); n += 1; e[n] = abs(x - 2)
first = lambda t: min(k for k in e if e[k] < t)
assert (first(1e-6), first(1e-12)) == (12, 21)
assert abs(e[13] / e[12] - 0.25) < 1e-3
err = lambda m: abs(F(3 * m + 1, m + 2) - 3)
assert err(4998) == F(1, 1000) and err(4999) < F(1, 1000) and err(4997) > F(1, 1000)
print(f"BAB 4: N=1220 galat(n=1221)=9.9991e-04; galat<1e-6 di n=12, <1e-12 di n=21; "
      f"galat(4998)=1/1000 tepat, galat(4999)={float(err(4999)):.7f}")

# ---------- CHAPTER 5 ----------
r = F(3, 5)
s20 = sum(r ** k for k in range(21))
assert f"{float(s20):.10f}" == '2.4999451576'
assert s20 + r ** 21 / (1 - r) == F(5, 2) == s20 + (F(5, 2) - s20)
assert f"{float(F(5, 2) - s20):.4e}" == '5.4842e-05' == f"{float(r ** 21 / (1 - r)):.4e}"
assert abs((1 + 1e-6) ** (1e6) - math.e) < 1e-3          # ratio test (c): limit 1/e
N = 10 ** 6
import numpy as np
s = float(np.sum(1.0 / np.arange(1, N + 1, dtype=np.float64) ** 2))
assert f"{s:.10f}" == '1.6449330668'
assert f"{math.pi ** 2 / 6:.10f}" == '1.6449340668'
a, b = s, math.pi ** 2 / 6
digits = lambda t: max(i for i in range(17) if round(t, i) == round(b, i))
assert digits(a) == 5 and digits(a + 1 / N - 1 / (2 * N * N)) == 15
alt = sum((1 if k % 2 else -1) / math.sqrt(k) for k in range(1, N + 1))
lim = (1 - math.sqrt(2)) * -1.4603545088095868           # (1-sqrt2) zeta(1/2)
assert 1 / math.sqrt(N + 1) < 1e-3 and N == 10 ** 6
assert f"{abs(lim - alt):.4e}" == '5.0000e-04'
SK = lambda K: sum(1 / (2 * j - 1) for j in range(1, 3 * K + 1)) - sum(1 / (2 * j) for j in range(1, K + 1))
H = lambda m: sum(1 / k for k in range(1, m + 1))
assert abs(SK(1000) - (H(6000) - H(3000) / 2 - H(1000) / 2)) < 1e-12
assert abs(SK(10 ** 6) - math.log(2 * math.sqrt(3))) < 1e-6
assert f"{math.log(2*math.sqrt(3)):.4f}" == '1.2425' and f"{math.log(2*math.sqrt(3))/math.log(2):.4f}" == '1.7925'
print(f"BAB 5: s20=2.4999451576 galat=5.4842e-05; s(1e6)=1.6449330668; "
      f"angka benar 5->15; N=1e6 galat=5.0000e-04; S_K->{math.log(2*math.sqrt(3)):.7f}")
print("OK: seluruh angka kunci cocok")
