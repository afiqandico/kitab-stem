# Answer-key audit rules for Chapters 6–32 (read by EVERY auditor)

Your task: check whether **the answer key really answers its exercise** and whether
**every number in it is correct**. The parity gate only proves that the ID and EN editions
agree; it does NOT prove correctness. Errors that slipped through before: a key answering
a statement different from its exercise, a missing `n-1` factor, a reversed inequality direction,
`16 GiB` where it should read `16 TiB`.

## Sources to read (do not change anything)

- Exercises: `chNN.tex`, the `\begin{latihan} ... \end{latihan}` environment.
- Key: `lampiran-kunci/kunci-*.tex`, the block from `\section*{Bab NN: ...}` up to
  the next `\section*{` or the end of the file. Item k = the k-th `\item`.
- The mapping is already verified: 304 exercise items ↔ 304 key items, 1:1. **Do not**
  propose adding or removing items.

## Hard prohibitions

1. **Do not edit any file.** You only report; the parent applies
   the fixes to both editions. (Editing it yourself makes the ID/EN editions diverge.)
2. **Do not invent numbers.** Every number you claim must have real computation
   output in your report: command + result. If the exercise says "run the lab
   block", write `BUTUH-LAB` — do not guess.
3. **Do not judge style, length, or prose quality.** Only: does the key answer
   that exercise, and are its numbers correct.
4. Legitimate asymmetry: one exercise may have several routes; a key taking a different route
   is still CORRECT if its result and claims are correct.

## Procedure per item

1. Read exercise k and key k. Ask: does the key answer **exactly** what
   the exercise asks (object, direction, condition, quantity)?
2. Extract every testable claim: numbers, matrices, roots, probabilities, dimensions,
   eigenvalues, complexity, explicit computed results.
3. Recompute with Python (`source ~/venv/bin/activate`; numpy/scipy/sympy
   are available). For Chapter 28 (Lean) run `~/.elan/bin/lean` on a temporary file
   in `~/.hermes/cache/scratch/`, not in the repo. Remember: the axioms of `omega` are
   `[propext, Quot.sound]` and it does not close non-linear goals.
4. Compare. Numerical tolerance: relative 1e-9 for exact, 1e-6 for float,
   unless the exercise states a rounding.

## Report format (concise, required)

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
A `BENAR` item needs only one line: `NN.2 BENAR (dim W=1; numpy rank=1)`.
Close with: `RINGKASAN: benar=X salah=Y ragu=Z butuh-lab=W`.

Do not copy the chapter content back. The report must be < 120 lines.
