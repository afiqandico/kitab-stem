# Kitab STEM — English edition

This directory holds the English edition of *Why Machines Can Be Wrong: From Linear Algebra
to Machine-Learning Security*. It is built from the Indonesian manuscript in `../_buku-ed2/`.
**The book is complete: 32/32 chapters plus the whole back matter** (front matter, four
appendices, index, colophon, references), assembled to a single PDF in 2026-10-26.

## Status

| Item | State |
|---|---|
| `preamble-en.tex` | done — English labels, same environment names as the Indonesian edition |
| `tools/cek-en.py` | done — chapter gate + `--pdf` assembly gate |
| `tools/uji-cek-en.py` | done — self-test of the chapter gate (16 checks, needs pdflatex) |
| `tools/cek-belakang.py` | done — parity gate for back matter (13 parts) |
| `tools/uji-cek-belakang.py` | done — self-test: 1 clean control + 5 planted defects, `6/6 PASS` |
| `tools/ambil-sumber.py` | done — regenerates `belakang/_sumber/` from `../_buku-ed2/main.tex`; `--cek` detects a stale copy |
| `TERJEMAH.md` | done — translation rules (what to translate, what to leave verbatim) |
| `main-en.tex` | assembler: title page, 6 parts + part intros, 32 chapters, appendices A–D, index, colophon, references |
| Chapters | ch01–ch32 (32/32) |
| Back matter | `belakang/*-en.tex`, 13 parts, ~20 000 words: preface, how-to-read (4 tracks), dependency map, Appendix A notation, Appendix B glossary (217 entries), Appendix C grading criteria, Appendix D answer keys (304 items), colophon, references (34 entries) |
| Assembled PDF | **638 pages, 3802746 bytes**, sha256 `64e0e90f06a8aa6dac840800a619a89d073b60ccb41824821c4d2da272172f9c`; built by `tools/cek-en.py --pdf`, not committed — a copy sits at `~/Downloads/Kitab-STEM-Why-Machines-Can-Be-Wrong.pdf` |

Gate state on the finished book:

```
python3 tools/cek-en.py            -> 32 bab diperiksa, 0 masalah
python3 tools/cek-en.py --pdf      -> OK rakitan EN: rc=0 error=0 label-ganda=0
                                      overfull>10pt=0 bocor-header=0 '??'=0
                                      entri-indeks=352 header=556
python3 tools/cek-belakang.py      -> 13 bagian diperiksa, 0 bermasalah
python3 tools/uji-cek-belakang.py  -> 6/6 PASS
python3 tools/ambil-sumber.py --cek-> sumber segar: salinan cocok dengan edisi Indonesia
```

The Indonesian edition was rebuilt for the answer-key audit: **643 pages, 3716202 bytes,
sha256 `d66d9c2f30704c30df98d0e666acc2f14f8be00988fcb102cc966fca6de614e9`** (previous
`bdb51a9f…`), two consecutive builds identical. The corrections carried into both editions are
listed under *Corrections carried into both editions*.

## How a chapter is checked

```
python3 tools/cek-en.py ch05        # one chapter
python3 tools/cek-en.py             # every translated chapter
python3 tools/cek-en.py --pdf       # assemble (pdflatex, makeindex, pdflatex x2) and inspect
python3 tools/uji-cek-en.py         # self-test: the gate must accept a faithful
                                    # chapter and must reject four planted defects
```

The gate compares the English chapter with its Indonesian source and fails when:

- the number of `\section`, `\tingkat`, `\kamus`, `\index` or `\label` differs;
- the sequence of environments `\begin{...}` differs (so no box or exercise is dropped);
- the set of `\label` keys differs, or a `\ref` has no matching `\label`;
- the multiset of math spans differs (whitespace ignored, `\text{...}` contents normalised), so a
  changed symbol or digit is caught — this check exists because it found a real defect in ch03;
- percent signs are compared as written: `$95\%$` and `$95$ percent` are *not* the same math,
  because a swallowed `\%` used to hide the rest of the line from the gate;
- in `--pdf` mode, a running head whose words are not in that chapter's own title (`bocor-header`),
  for chapters **and** appendices; headers still count up, so only matching each head against its
  own title catches a leak. Injected on purpose, this check reports 75 bad heads;
- the word count leaves the 0.85–1.35 band (guards against summarising or padding);
- more than 0.5% of words are Indonesian function words (guards against untranslated prose).

## How the back matter is checked

`tools/cek-belakang.py` is a separate gate because the back matter is not made of chapters:

```
python3 tools/cek-belakang.py                 # all 13 parts
python3 tools/cek-belakang.py lampB           # one part
python3 tools/ambil-sumber.py --cek           # source copies still match ../_buku-ed2
```

It compares `belakang/<name>-en.tex` with `belakang/_sumber/<name>.tex` and fails when:

- a part is missing, or the word ratio (EN/ID) leaves 0.85–1.35;
- the multiset of `\item`, `\section`, `\label`, `\ref`, `\toprule`, … counts differs;
- the sequence of `\begin{...}` environments differs;
- the multiset of math spans differs (same normalisation as the chapter gate);
- numbers differ. Numbers inside math are compared there, not here: **scanning math for numbers
  as well split `1{,}5625` into the tokens `1` and `5625`** and reported failures where the maths
  was identical. `\input{...}` lines are ignored the same way (file names are not prose);
- more than 0.1% of words outside parentheses are Indonesian function words. Parentheses are
  skipped because the glossary deliberately keeps the Indonesian term there;
- the glossary is not sorted by its English headword.

A stale `_sumber/` copy is a failure, not a detail: if `../_buku-ed2/main.tex` changes and the copy
does not, the gate compares the translation with the old text. `tools/ambil-sumber.py` cuts the
slabs by *marker*, not by line number (line numbers shift with every edit) and `--cek` reports
`sumber basi: …` when a copy drifts.

## Corrections carried into both editions

- **Answer key 32.7 (Bell state).** The Indonesian key said that when the second qubit is
  measured and the result is `1`, the first qubit is `|0>` and the outcome `01` is certain —
  which contradicts the perfect correlation the next sentence claims. In `|Phi+>` a measured
  `1` on the second qubit forces the first to `|1>`, so the outcome is `11` and `P(01) = 0`,
  exactly as in the `0` case. Fixed in `../_buku-ed2/lampiran-kunci/kunci-24-32.tex` and here,
  and both PDFs were rebuilt; the earlier Indonesian shas `59d576a8…` and `6963b865…` do not
  contain the fix.
  The gate compares the two editions, so it would have kept the error: it proves parity, not
  truth. This one was caught by reading, and it is the reason the README says prose needs a
  human reader.

- **Follow-up audit (4 more points).** The hint for 5.9 used `H_{2K}` (giving `0.8959`); the
  three-positive/one-negative pattern gives `S_K = H_{6K} - (1/2)H_{3K} - (1/2)H_K -> 1.2424521`,
  confirmed by direct summation, so the hint was corrected. The premise of exercise 12.9 ("why is
  that bound much looser?") is false: `p2(0.04) = 1.0198`, error `3.90e-6`, Lagrange remainder
  `4.00e-6` — the bound is tight; exercise and key were reworded. Two audit notes were rejected:
  exercise 1.9 deliberately asks the reader to judge a fallacious inference, and the KKT condition
  in 23 carries the correct sign for a *minimise* problem (`N = {1,2,3,...}` is defined in ch01).

- **Answer-key audit, second pass (20 items).** Every exercise has a keyed answer, so the keys were
  audited against the exercises and recomputed independently (sympy/numpy/scipy, Lean 4.10 for the
  formal chapters). Twenty items were wrong in *both* editions — parity had kept them identical, not
  correct — and all twenty were fixed in the Indonesian source first and mirrored here:
  `1.9` (answered a different claim: `n^2-1` instead of `n^2+n+41`, which fails at `n=40`),
  `10.6` (only one direction proved), `11.6` (`delta=eps/3` was called valid although
  `(1+eps/3)^3-1>eps`), `17.1` (triple-overlap term subtracted *three* times, not two),
  `17.8` (false positives for two positive tests are `999*0.01^2≈0.1`, not `10`),
  `18.10` (`R=5 448`, not `103 514`: the `n-1` factor was dropped), `20.4` (narrower interval comes
  from `n=40`, not from `p` near the edge; Fisher information is *larger*), `20.7` (`p=0.02` and the
  2-hour difference lies outside the interval), `21.5` (the leverage difference vanishes like `1/n`),
  `21.8` (`-0.2+0.6` is not a decomposition; contributions are `-0.028571+0.428571`),
  `24.9` (capacity 7 rules out the pair `(1,3)`, not `(1,2)`), `25.7` and the chapter-25 hint
  (`1+k+k(k-1)/2` regions: `2,4,7`, not `k^2-k+2`: `2,4,8`), `25.9` (the lab block uses ReLU, so
  `b1=+10` saturates nothing), `27.6` (pair counts `5+5+4+3+2=19`), `28.2` (a goal containing `k*k`
  is not linear, so `omega` alone cannot close it), `28.7` (`forall delta` -> `exists delta` in the
  weak statement), `28.8` (`omega` yields `propext, Quot.sound`, not `Classical.choice`), `29.5`
  (the gap *widens* to 54 points before it narrows), `30.3` (the inequality direction: below 0.35 is
  guaranteed to succeed, and at 0.35 the label still flips), `32.9` (`16 TiB`, not `16 GiB`).
  Rejected: a claim that Lean auto-binds a free `x` in 28.9 — Lean 4.10 refuses it here, so the key
  was right. Every follow-up note (1.9, 12.9, 23.2, 25.7/25.10, 27.10, and the hint in 5.9) was
  settled in the follow-up audit above: 5.9 and 12.9 were real defects and are fixed, the rest were
  rejected with a computation.

- **Answer-key audit, waves 5–6 (chapters 26–32).** Nine items were still wrong after the second
  pass, and the reason matters: several earlier fixes diagnosed the defect but left the key's
  conclusion intact. `28.2` said `omega` cannot close a goal containing `k*k`, then still claimed the
  remainder was linear and closed by `omega` — the working proof ends with `exact bantu k`. `30.3`
  corrected the inequality direction but kept `0.35`; `(8*0.25-0.62)/4 = 0.345`. `28.9`'s "correct
  version" still used `exists delta` and stayed vacuous. The others: `26.2` never showed the second
  cross term (it vanishes because `E[fhat-fbar]=0`, no independence needed), `27.9` (8.62 wrong
  alarms rounds to *nine*, not eight), `28.3` (`rw [evenSum, ih]` fails; the key needed a `have h`
  regrouping step, and `evenSum` was never defined in the chapter), `28.5` (`n=0..1000` is *1001*
  cases, not 1000), `31.9` (condition (ii) was "widely used", which is not a correctness condition —
  and its second reason contradicted chapter 31, which says ML-DSA/FIPS 204 already exists), `32.6`
  (`Z` after `H` is `X`, not `S^dagger`). The chapter 29 body also said 89.28 percent where its own
  table gives 89.06. Rejected after recomputation: `29.4` (95.48 reproduces with `rng(1)`/`rng(2)`;
  `rng(0)` gives 95.64, so the number is a draw, not an error) and `31.1` (the verdict stands).
  Still open by choice: `30.5` asks for three numbers on a two-layer model whose width is never
  specified, so the key gives the qualitative prediction only. The chapter 29 `lab` block ships
  only the attack library, no training driver, so the rows of the 29.5/29.9 tables cannot be
  re-derived from the repo without writing one (the audit did: clean accuracy 0.9799 reproduces,
  untargeted success comes out 88.21 percent instead of 89.06 on the same protocol). Checkers: `tools/verify-kunci-06-15.py`
  (37), `tools/verify-kunci-16-23.py` (36), `tools/verify-kunci-21-25.py` (38),
  `tools/verify-kunci-26-32.py` (20, runs Lean 4 on `tools/lean-28/*.lean`), all passing.

## Deliberate choices

- **Environment names stay Indonesian** (`teorema`, `untukdosen`, `bacakeras`, …) so one
  checker can diff the two editions; `preamble-en.tex` prints the English labels.
- **`\kamus{English term}{Indonesian term}{analogy}`** — the printed pair stays
  "English (Indonesian)" in the English edition, mirroring the Indonesian original. The glossary
  follows the same convention: English headword, definition in English, Indonesian term in
  parentheses.
- **Glossary order follows the English alphabet**, not the Indonesian source order, with 217
  entries kept. Four English headwords appear twice (`Covariance`, `Kernel, null space`,
  `Uniform convergence`, `Wilson interval`) because the Indonesian source itself carries two terms
  for each of those concepts; both entries are kept and the Indonesian term tells them apart.
- **Long chapter titles shorten the running head only, never the title.** `\judulpendek{...}`
  (defined in `preamble-en.tex`) supplies a head text for the *next* `\chapter` and is consumed
  immediately, so the shortening cannot leak. The full title stays in the table of contents and
  on the chapter page. Without the one-shot mechanism, chapter 13's override made chapters 14–18
  print "CHAPTER 13. RIEMANN INTEGRALS" in the head.
- **`\@chapapp`, not `\chaptername`, in `\chaptermark`** so appendix heads read
  "APPENDIX A. TABLE OF NOTATION". `\chaptername` stays "Chapter" after `\appendix`, and LaTeX
  raises no warning when an appendix claims to be a chapter.
- **English number conventions in math:** decimal comma `{,}` becomes `.` (949 places), and
  thousands groups use `{,}` (`100{,}000`). The gates normalise both editions before comparing,
  so parity is still proved on the digits, not on the separator.
- **Label keys are identical across editions** (`fig:kisi`, `thm:cauchy-schwarz`, …), which is
  what lets the gate prove nothing was renamed or lost.

## Known limits (honest)

- Translation quality is machine-produced and gated only structurally: counts, labels, word
  band, residue words, sorted glossary. Prose quality still needs a human reader. No native
  speaker has read the English edition.
- Mathematical statements and numeric results are copied verbatim from the Indonesian source;
  the gates do not re-verify their correctness.
- The index (352 entries) is built from the `\index{...}` keys that already existed in the
  Indonesian chapters, so it inherits their choices of terms — no new English index terms were
  invented for the back matter.
- Number normalisation is a heuristic: a bare comma followed by exactly three digits is read as a
  thousands separator, so the rare Indonesian decimal `1,234` would be read as 1234. Both editions
  are treated the same way, which keeps parity but does not make the reading always correct.
- **Three source defects in `_buku-ed2/ch25.tex` were fixed in both editions**, not mirrored:
  `\nabla` and `\neq` had been split into `abla` / `eq` by a line break (the printed Indonesian
  PDF said "ablaW₁L = 0" and "W1 eq0"), the hint said "Item 10" for a chapter with nine
  exercises, and a cross-reference pointed at "Chapters 26 and 25" — chapter 25 itself.
- **Two chapter-gate defects were found by the translators and fixed here:** (`%` escaped as `\%`
  was being treated as a comment start, deleting the rest of every such line from the comparison —
  negative control F1) and `\\[3pt]` inside a TikZ node was being read as an opening display-math
  delimiter, merging a whole node into one bogus span (negative control F2). Both had been quietly
  weakening the math check since batch 1.
- `$95$ percent` versus `$95\%$`: the source decides. Where the source writes `$95\%$` the
  translation uses `$95\%$`; where it writes `$95$ persen` the translation keeps `$95$ percent`.
  88 occurrences were aligned this way and each chapter was re-checked by the gate.
- The Indonesian source itself mixes decimal separators (mostly `{,}`, sometimes a full stop —
  `$0.775$`, `$2.718$`). Those are left as decimals here. The 15 dotted three-digit tokens whose
  value is ≥ 10 were reviewed by hand: eight are thousands separators in the source
  (`65.536`, `100.000`, `99.900`, `98.901`, `98.902`, `999.037`, `10.943.7`, `11.094`) and were
  regrouped as `{,}`; the rest (`19.125`, `24.001`, `24.002`, `26.565`, `15.249`, …) are genuine
  decimals.

## Gate defects found while finishing the back matter

- **`\f` blindness (assembly gate).** `pdftotext` prefixes the first line of every page with a form
  feed, so `^CHAPTER …` matched almost nothing: the gate reported `bocor-header=0` because it was
  blind, not because the book was clean. The PDF text is now normalised (`\f` → newline) and the
  gate prints `header=554`; fewer than 400 readable heads is now itself an error.
- **Appendix heads read "CHAPTER A."** `\chaptermark` used `\chaptername`, which does not change
  after `\appendix`. Fixed to `\@chapapp`; the head check now also covers appendices and reports
  a wrong prefix as `prefix: seharusnya APPENDIX`.
- **The assembly gate never built the index.** `\printindex` printed an empty page with no warning.
  `--pdf` now runs `makeindex` and requires `entri-indeks > 0` (currently 352).
- **Number scan of the back-matter gate read math and `\input` names.** Fixed as described above;
  the self-test's planted defects still fail after the change (`6/6 PASS`).

## Defects found in batch 8 (chapters 29-32)

- **`ch31` carried two stray `|` characters** from a line break
  (`$65\,537\cdot60\,493` / `|=3\,964\,529\,741$`), which would print as "|=". The math
  multiset check caught both; the bars were removed so the spans match the source exactly.
- **`ch30` put `\judulpendek{...}` *after* `\chapter`.** The mechanism is one-shot: `\chaptermark`
  consumes the pending short title, so setting it after the chapter passes it to the *next* one —
  chapter 31's running head printed "CHAPTER 31. THE LIMITS OF ATTACK". `cek-en.py --pdf` reported
  `bocor-header=6`. The macro now precedes its own chapter; the rule is recorded in the file itself.
- **`ch32` had no short running head**: the full title is 68.9 pt too wide, producing 19 overfull
  headings (the same for `ch30` before its fix, 13 more). Both chapters now use
  `\judulpendek`, and `--pdf` reports `overfull>10pt=0 bocor-header=0`.
