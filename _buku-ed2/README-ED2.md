# First Edition — *Why Machines Can Be Wrong? From Linear Algebra to Machine Learning Security*

A textbook written in Indonesian, **6 parts, 32 chapters**, rebuilt from the 13-chapter version
(`../_buku/`, archived as a historical record) with ideas drawn from the textbooks
in the References list. The two chapters that set it apart from the earlier assembly: Chapter 16
(Differential Equations and Dynamical Systems) and Chapter 21 (Regression and Applied Statistics).

Build result: `Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf` at the repo root —
**643 pages, 3716202 bytes (3.54 MB), 206,944 body words, 95 figures, 128 learning-channel boxes
(32 × 4), 361 index entries (402 `\index` keys, some merged), **217 glossary entries**
(all 162 `\kamus` terms in the chapters + 55 supporting terms), 34 references**,
**0 LaTeX errors, 0 overfull boxes at all**, 0 `??` references, the List of Figures holds **95 entries**
(equal to the number of `\begin{figure}`), and 32/32 chapter titles verified present in the PDF
(sha256 `d66d9c2f30704c30df98d0e666acc2f14f8be00988fcb102cc966fca6de614e9`, build 2026-11-07,
**reproducible**: two consecutive builds produce an identical sha).

> **Follow-up audit (4 more points).** Hint 5.9 wrongly used $H_{2K}$ (giving
> $0.8959$); the three-positive-one-negative pattern gives $S_K=H_{6K}-\tfrac12H_{3K}-\tfrac12H_{K}
> \to1.2424521$ — matching the direct computation, so the hint was fixed. The premise of exercise 12.9
> ("why is that bound so much looser") was wrong: $p_2(0.04)=1.0198$, error $3.90\times10^{-6}$,
> Lagrange remainder $4.00\times10^{-6}$ — the bound is tight, not loose; exercise and key were adjusted.
> Two audit notes were rejected: exercise 1.9 really does ask for judging a wrong inference (not a defect), and
> the KKT conditions in 23 already carry the right sign for a "minimize" problem ($\mathbb{N}=\{1,2,3,\dots\}$
> is defined in Chapter 1).
>
> **Answer-key audit, second pass (20 items).** All 304 key items were re-tested
> against their exercises and recomputed with Python/Lean; twenty items were wrong in both editions
> (parity aligns, it does not justify) and were fixed in this Indonesian source and then
> mirrored into the English edition: 1.9 (answered a different claim, $n^{2}-1$ instead of $n^{2}+n+41$ which
> fails at $n=40$), 10.6 (the converse was not proved), 11.6 ($\delta=\varepsilon/3$ called valid
> although $(1+\varepsilon/3)^{3}-1>\varepsilon$), 17.1 (the triple term subtracted *three* times),
> 17.8 (false positives of two tests $999\cdot0.01^{2}$, not $10$), 18.10 ($R=5\,448$, not
> $103\,514$: the $n-1$ factor was missing), 20.4 (the interval is narrow because $n=40$, not because $\hat p$ is at
> the edge; Fisher information is in fact larger), 20.7 ($p=0.02$ and a 2-hour difference outside the interval),
> 21.5 (the leverage difference vanishes like $1/n$), 21.8 ($-0.2+0.6$ is not a decomposition;
> its contribution is $-0.028571+0.428571$), 24.9 (capacity 7 discards $(1,3)$, not $(1,2)$),
> 25.7 and the Chapter 25 hint ($1+k+k(k-1)/2$ regions: $2,4,7$), 25.9 (the lab block uses ReLU, so
> $\mathbf{b}_{1}=+10$ saturates nothing), 27.6 (pair count $5+5+4+3+2=19$), 28.2
> (the goal contains $k\cdot k$: not linear, so \texttt{omega} alone does not close it), 28.7
> ($\forall\delta$ replaced by $\exists\delta$ in the weak statement), 28.8 (\texttt{omega} yields
> \texttt{propext} and \texttt{Quot.sound}, not \texttt{Classical.choice}), 29.5 (the difference
> *widens* to 54 percentage points before narrowing), 30.3 (inequality direction: below 0.35
> success is guaranteed, and at 0.35 the label still flips), 32.9 ($16$ TiB, not $16$ GiB).
> One auditor claim was rejected: Lean 4.10 on this machine rejects free $x$ in 28.9, so the old key
> is correct. All those leftover notes (1.9, 12.9, 23.2, 25.7/25.10, 27.10, hint 5.9) were
> resolved in the follow-up audit above: 5.9 and 12.9 were real defects and were fixed, the rest
> were rejected with computations.
>
> Content fix 2026-10-26 (Answer Key Chapter 32 item 7): for the Bell state
> $|\Phi^{+}\rangle$, the old key wrote "if the outcome is 1, the first qubit is $|0\rangle$
> and the outcome $01$ is certain" — contradicting the perfect correlation stated in the
> next sentence. Correction: the first qubit collapses to $|1\rangle$, the outcome $11$ is certain, and the probability
> of $01$ is also $0$ (as in the outcome-$0$ case). The source `lampiran-kunci/kunci-24-32.tex`
> and this PDF were rebuilt; the English edition follows the same correction. The old PDF
> (sha `59d576a8…`) does not contain this fix.

> Content fix 2026-10-25 (Chapter 25): three defects in the `tantangan` box and in the exercise
> hints were corrected. `\nabla` and `\neq` on lines 640-643 were truncated into
> `abla` and `eq` (the old PDF printed "ablaW₁L = 0" and "W1 eq0"); the hint mentioned
> "Item 10" although that chapter's exercises have only 9 items (the hint's content matches
> Item 9); and the validity limits referred to "Chapters 26 and 25", that is, the chapter itself.
> The old PDF (sha `d10584af…`) does not contain this fix.

## What changed from the 13-chapter archive

| Aspect | Archive (`../_buku/`, 13 chapters) | First Edition (this folder) |
|---|---|---|
| Scope | 13 chapters, 5 topics | 6 parts, 32 chapters: foundations, linear algebra, analysis, probability/statistics/numerics, optimization, ML + security + cryptography + privacy |
| Chapter length | ±2,500 words | 5,500–6,500 body words + computational lab |
| Readers | undergraduates | four tiers: children 10+, undergraduates, lecturers, researchers |
| Markers | — | orange boxes (young readers), green (lecturers), grey (researchers), `\kamus`, `\tingkat`, plus four learning-channel boxes: `bacakeras` (auditory), `tangan` (kinesthetic), `resep` (procedural), `tantangan` (problem solver) |
| Exercises | 4–6 items | 8–10 items + hints for the hardest items |
| Figures | none | 95 numbered TikZ/pgfplots figures (2–3 per chapter), captioned, referenced in the text, with a List of Figures |
| Extras | — | notation appendix, glossary with **217 entries** (every `\kamus` term in the chapters has an entry), exercise grading criteria, index (makeindex) |

## Folder contents

| File | Role |
|---|---|
| `main.tex` | skeleton: preamble (tikz, pgfplots, caption), the four tier boxes + four learning-channel boxes, the "Six ways to learn, six entrances" page, title page, preface, how to read (4 paths), 32-chapter dependency map, 6 `\part`s, 32 `\input`s, Table of Contents, List of Figures, appendices A–D (D = answer keys for 304 items), index, colophon, 34 references |
| `ch01.tex` … `ch32.tex` | chapter bodies (no preamble; `\input` by `main.tex`) |
| `PANDUAN-BAB-ED2.md` | absolute rules (including the figure rules) + the "Four reader tiers" section + the compilation-test recipe |
| `SPEC-BAB-ED2.md` | contents of each chapter: sections, sources, required numbers (including Chapters 29–30) |
| `build_ed2.py` | builder + quality gate: `check`, `status`, `pdf` |
| `tools/glosarium.py` | source of the definitions for all `\kamus` terms + the glossary-block writer: `tulis` (rewrites `main.tex`, alphabetical order), `cek` (reports terms without an entry), `daftar` |
| `tools/cek-kunci-01-05.py` | checker for the Appendix D key numbers of **Chapters 1–5**: 121 `assert` lines, output `OK: seluruh angka kunci cocok` |
| `tools/cek-cacah-kunci.py` | maps 304 exercise items ↔ 304 key items per chapter; prints `Semua bab 1:1` (fails if a chapter does not match or the parser is blind) |
| `tools/verify-kunci-06-15.py` | 37 checks for the fixes to 6.5, 9.9, 12.2, 13.7, 14.5 (both editions' text + recomputation) |
| `tools/verify-kunci-16-23.py` | 36 checks for the fixes to 18.8, 18.10, 19.10, 20.4, 20.7 |
| `tools/verify-kunci-21-25.py` | 38 checks for 21.5, 21.9, 22.10, 25.5, 25.9; item 25.9 is tested by re-running the lab block from `ch25.tex` |
| `tools/verify-kunci-26-32.py` | 20 checks for 26.2, 27.9, 28.2, 28.3, 28.5, 28.9, 29 (chapter text), 30.3, 31.9, 32.6; runs Lean 4 on `tools/lean-28/*.lean` |
| `AUDIT-KUNCI.md` | audit contract: the auditor only reports, the parent edits both editions, and every number must come with command + output |
| `test_gerbang.py` | skeleton tests, **36 checks** (`make test` → 36/36 PASS): quality gate (positive + negative, including the figure and glossary rules), PDF title/edition, and a `main.tex` compile through to PDF in a `tempfile` sandbox |
| `_wrap/` | per-chapter test directory (must be empty when clean) |

## Rebuilding

```
cd "_buku-ed2"
source ~/venv/bin/activate
python3 test_gerbang.py       # skeleton tests: must print "N/N PASS", exit 0
python3 build_ed2.py status   # which chapters already exist
python3 build_ed2.py check    # per-chapter gate; exit 0 = ready, 2 = empty, 1 = defective
python3 build_ed2.py pdf      # pdflatex, makeindex, pdflatex x2 -> repo root
```

## Quality gate used by `check`

Per chapter: 5,000–7,500 body words (ambiguous in both directions: `pendek` <5,000, `kepanjangan`
>7,500; verbatim **and figures** are not counted because they are not prose), ≥5 `\section`s and
every section has a `\tingkat`, ≥4 theory environments, 2–4 `untukanak`, exactly 1
`untukdosen` and 1 `untukpeneliti`, ≥3 `\kamus`, ≥8 `\index`, 8–10 exercise items, present:
`\kertas`, `\peta`, `lab`, `verbatim`, `ringkasan`; pure ASCII; no
`\documentclass`/`\usepackage`/`\cite`/`\footnote`/`table` float; only environments from
the allow-list.

Figure rules (since figures were allowed): a `figure` containing TikZ/pgfplots with no external
image file, must have `\caption{}` + `\label{fig:...}`, and must be referenced by `\ref{fig:...}`
in the same file. `\label`/`\ref` are opened only for figures; `\eqref` and
`\pageref` remain forbidden.

Gates that are only useful on the **complete book**, found from real builds:

| Flag | Meaning |
|---|---|
| `judul-panjang` | a `\chapter` title >55 characters without a short form `\chapter[short]{...}`; the running head will overflow past the margin |
| `verbatim>N` | a code line >90 columns; with global `\footnotesize` the safe limit is ±90 columns |
| `figure-tanpa-caption/label` | a `figure` without a caption or without a `fig:...` label |
| `figure-tak-dirujuk` | the figure label is never `\ref`-ed in the same file |
| `Judul di tabel peta tidak cocok` | chapter title ≠ its row in the "Peta Ketergantungan Bab" table in `main.tex` |
| `Istilah \kamus tanpa entri glosarium` | a `\kamus{...}` in a chapter has no entry in the Glossary Appendix; add it via `tools/glosarium.py` then run `tulis` |

`build_ed2.py pdf` **fails** (exit 1) if there is an overfull >10 pt in the built book; the overfull
count and the page count are printed at the end.

## Honest limits

- The skeleton has a canonical test: `python3 test_gerbang.py` (36 checks), run in a
  `tempfile` sandbox. What those tests do **not** cover is chapter content quality and defects that only
  appear when the 32 chapters are assembled: for that `make pdf` is used, which rejects a book with
  overfull >10 pt. The numbers in this README come from the 2026-10-25 build after
  the third wave (Chapters 21–30) and the glossary completion, not from estimates.
- `build_ed2.py pdf` pins `SOURCE_DATE_EPOCH` + `FORCE_SOURCE_DATE`, so two builds from
  the same source produce an **identical** sha256 (tested twice in a row); before this
  the sha changed on every build because pdfTeX wrote the date and `/ID` from the system clock.
- `pdf` also rejects a build containing duplicate labels. The label `fig:kisi` was once used in Chapter 2
  *and* Chapter 7, so `\ref{fig:kisi}` in Chapter 2 displayed the Chapter 7 figure; now that label
  is `fig:kisi` (Chapter 2) and `fig:kisi-07` (Chapter 7), and the build is free of
  `multiply defined` warnings.
- Glossary: 215 of 217 entries give an English equivalent `(\emph{...})`; two entries
  (`Kamus`, `Ringkasan`) explain this book's own boxes, so they are deliberately left
  without an equivalent. The `check` gate only guarantees **completeness** (every `\kamus` has
  an entry) and does not machine-check **format**.
- Numbers inside the chapters (including in figure captions) come from real execution of
  Python/NumPy/SciPy/sklearn on this machine; each chapter contains code the reader can
  rerun. Chapter 30 states that four simulation-time numbers are run-to-run.
- The Lean 4 snippets in Chapter 26 were run with **Lean 4.10.0** (`~/.elan/bin/lean`) without
  Mathlib: 8 of 16 blocks compile cleanly, the rest are deliberate failure demonstrations
  and error transcripts. Library tactics such as `linarith`/`ring` were not run.
- All 32 chapters sit within 5,500–6,500 body words (actual range 6,237–6,498;
  lowest is Chapter 21, highest Chapter 15). Trimming to pay for the boxes and figures was done on prose that
  repeated itself; numbers, theorems, and exercise items were not reduced.
- **Appendix D holds the keys to 304 exercise items** (one answer per item, all 32 chapters).
  Their form is deliberately incomplete: final number + a 2–5 line sketch of steps, not a full proof;
  the key numbers of **Chapters 1–5** can be re-checked with `tools/cek-kunci-01-05.py`,
  the 304 ↔ 304 mapping with `tools/cek-cacah-kunci.py`, and the fixes for Chapters 6–32 with
  `tools/verify-kunci-06-15.py`, `-16-23.py`, `-21-25.py`, `-26-32.py` (37 + 36 + 38 + 20 checks,
  all passing). The Chapters 6–32 audit ran in six waves guided by `AUDIT-KUNCI.md`
  and found **23 defective key items** (14 in Chapters 6–25, 9 in Chapters 26–32), plus one exercise
  (21.5) and one chapter-text number (Chapter 29); all were fixed in both editions.
  Known leftovers, deliberately left open: 30.5 demands a two-layer model architecture that
  the exercise does not state, so its key only gives a qualitative estimate; and the 29.4 number
  depends on the random draw (`rng(1)`/`rng(2)` give 95.48 percent, `rng(0)` gives 95.64);
  the Chapter 29 `lab` block holds only the attack library without the training driver, so tables 29.5/29.9
  cannot be re-derived from the repo without writing a driver (that driver is what was used
  during the audit: clean accuracy $0.9799$ reproduced, untargeted attack $88.21$ percent
  replacing $89.06$ on the same protocol).
  **3 items are flagged ambiguous** because the exercises themselves are problematic. Appendix C still gives grading
  criteria and verification tools before the reader opens the keys.
