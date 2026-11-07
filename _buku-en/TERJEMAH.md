# TERJEMAH — English-edition rules

Source: `../_buku-ed2/chNN.tex`. Target: `chNN.tex` in this directory. One chapter per file.
Preamble: `preamble-en.tex` (environment names deliberately stay Indonesian so a single structure
checker can compare both editions; only the printed labels are translated).

## Translate
- All prose, section titles, box contents, figure captions (`\caption`), exercise item text,
  analogies, and procedural text inside `verbatim` **if** it is a comment or output in words.
- `\kamus{A}{B}{C}`: **A = English term**, **B = original Indonesian term**, C = the analogy
  translated. Example: `\kamus{vertex}{verteks}{the corner of the feasible region...}`.
- `\tingkat{dasar|menengah|lanjut}` → `\tingkat{basic|intermediate|advanced}` (consistently).
- `\index{...}`: translate its contents into English; the number of keys must match the source.
- `\peta{...}`: translate its contents; the book title stays in `\emph{}`, chapter/section numbers stay.

## Do not change
- LaTeX command and environment names (`\begin{teorema}`, `\section`, `\label`, `\ref`).
- `\label{...}` and `\ref{...}` keys — **exactly the same** as the source (used to
  compare the two editions). Do not add or remove labels.
- Symbols, numbers, and notation inside `$...$`, `\[...\]`, `equation`, `align`. The only
  exception: how digit separators are written (see the Numbers section) — the numbers themselves stay exactly the same.
- **Do not touch `../_buku-ed2/` at all.** That Indonesian source is final. If
  you think something there is wrong, write it in the summary, do not edit. (This happened once: one
  translator changed `95\%` to `95 persen` and dropped `\\[3pt]` in a TikZ node in
  `_buku-ed2/ch20.tex`; all those edits were reverted.)
- `\begin{verbatim}` and `\end{verbatim}` must stand on their own lines (do not
  merge them with `\begin{lab}` on the same line) — all 32 source chapters use that pattern and
  merging makes LaTeX report that `\begin{lab}` is never closed.
- Python/Lean code inside `verbatim`: logic and numbers **must not change**. Printed
  labels (`print("selisih :", ...)`) may be translated together with the output block below them,
  provided every number in the output stays identical to the source — the gate compares
  numbers, not label text.
- TikZ/pgfplots code: coordinates, colors, options. Only printed text (`\node{...}`,
  `\caption`, axis labels `xlabel`/`ylabel`) gets translated.

## Numbers
- Numeric values do not change. The Indonesian decimal comma (`3,14`) becomes a point (`3.14`); the
  Indonesian thousands separator (`1.000`) becomes a comma (`1,000`).
- **The same holds inside mathematics.** `$0{,}5$` becomes `$0.5$` and `$100.000$` becomes
  `$100{,}000$`; do not change digits, order of magnitude, or symbols. The gate normalizes the
  comma/point convention before comparing, so a convention change cannot be used to
  disguise a change in numbers.
- **The percent sign is copied as is.** If the source writes `$95\%$`, the translation writes
  `$95\%$`; if the source writes `$95$ persen`, the translation writes `$95$ percent`. The gate
  compares the two as different mathematics, so do not standardize them yourself.

## Style
- American English, active voice, "we" as in the source.
- Do not add content, do not summarize, do not delete exercise items or boxes.
- Target word count: 0.85–1.35 × the source word count (English is usually shorter).

## Output
- The file starts with `\chapter{...}`, without a preamble, without `\begin{document}`.
- It must compile with `preamble-en.tex` with no errors and no overfull > 10 pt.
- When finished, run: `python3 ../_buku-en/tools/cek-en.py chNN`
