# Chapter writing guide — First Edition
## *Why Machines Can Be Wrong? From Linear Algebra to Machine Learning Security*

A textbook written in Indonesian, **6 parts, 32 chapters**, built with pdfLaTeX.
You write **one chapter** as a `.tex` file containing only the chapter body (no preamble).

The book must be readable by **four reader tiers at once**: curious primary and lower-secondary
pupils, S1 undergraduates, the lecturers who teach it, and researchers probing the limits of knowledge.
They do not read a different book; they read the same chapter along different paths.
That is why every chapter **must** contain the tier boxes below.

## Absolute rules

1. Output: one file, at the exact path given (`_buku-ed2/chNN.tex`). No
   other file may be created inside `_buku-ed2/` except in the test directory `_wrap/chNN/`.
2. **No** `\documentclass`, `\usepackage`, `\begin{document}`, `\cite`, `\footnote`,
   and no `table` float. The chapter is pulled in with `\input{}` from `main.tex`.
   **Figures are allowed** only as a `figure` containing TikZ/pgfplots (with no external
   image file), must have a `\caption{}` and `\label{fig:...}`, and must be referenced in
   the text with `\ref{fig:...}` in the same file. At most **3 figures** per chapter,
   width not exceeding `\linewidth`, and a figure must explain an idea already
   stated in the text, not replace it. `\label`/`\ref` for figures only;
   `\eqref` and `\pageref` remain forbidden.
3. No Unicode outside math mode (do not write ε, ≈, ⇒, ×, √, α as text).
   Inside `$...$` use `\varepsilon`, `\approx`, `\Rightarrow`, `\times`,
   `\sqrt{2}`, `\alpha`, `\mathbb{R}`, `\mathbf{x}`, `\nabla`, `\sum`, `\int`,
   `\mathcal{O}`, `\mathbb{E}`.
4. Available environments: `definisi`, `teorema`, `lemma`, `akibat`, `proposisi`,
   `contoh`, `latihan`, `catatan`, `ringkasan`, `lab`, `untukanak`, `untukdosen`,
   `untukpeneliti`, `itemize`, `enumerate`, `description`, `equation`, `align`,
   `tabular`, `quote`, `verbatim`. Extra commands: `\kertas{...}`, `\peta{...}`,
   `\kamus{istilah}{padanan Inggris}{analogi}`, `\tingkat{dasar|menengah|lanjut}`.
   Do not define new environments or commands, and do not load any package.
5. **Numbers must come from real execution.** Every numerical value that is not a definition
   must come from (a) theory you derive, (b) a hand computation you
   carry out and verify with Python/numpy/scipy, or (c) a result explicitly
   printed in a source you have read. If in doubt, compute again. Do not invent.
6. Cite a source book by **chapter/section name**, not by page number (numbering
   differs between editions). Refer to another chapter of this book with "see Chapter 9", not `\ref`.
7. Standard Indonesian, addressing the reader as **"kita"** (not "aku"/"kamu"). Opening
   with an empty sentence such as "Pada bab ini kita akan membahas..." is forbidden. Start from
   one concrete problem.
8. No overclaiming ("terbukti", "selalu", "pasti") without explicit conditions.
   A skipped proof must be declared skipped, together with where to find it.

## Six learning entrances (required in every chapter)

The four tiers below serve differences in *depth*; the four boxes that follow serve differences
in *learning style*. Each chapter contains **exactly one** of each, plus 2-3 figures.
The gate rejects a chapter lacking any of the four (`bacakeras=0`, `tangan=0`, `resep=0`,
`tantangan=0`) and rejects any figure count other than 2-3 (`gambar=N`).

| Box | For type | Required content | Length |
|---|---|---|---|
| `bacakeras` | auditory | a script that **reads well aloud**: rhythm, repetition, two-voice dialogue, or a mnemonic; write sentences that can be spoken, not stacked formulas; end with one line the reader must repeat | 90-200 words |
| `tangan` | kinesthetic | an activity with real objects or body movement: cards, coins, folded paper, a tiled floor, string, fingers, walking backwards; name the materials, the physical steps, and what the reader must **see** happen | 80-180 words |
| `resep` | procedural | a numbered step card (3-6 steps) short enough to memorize for solving any problem on that topic, plus one warning about an order that must not be swapped | 60-140 words |
| `tantangan` | problem solver | one open problem or puzzle that is **not** routine, with 2 graded hints (hint 1 vague, hint 2 close to the answer) and one sentence "if you get stuck, go back to section X" | 70-160 words |

Additional rules:
- The four boxes **must not** repeat sentences from the chapter body; each
  must add a new angle on the same idea.
- `bacakeras` and `tangan` must be free of heavy notation; `resep` must on the contrary be concrete and
  may contain symbols; `tantangan` must have an answer that genuinely exists.
- Figures serve as the entrance for the visual type: 2-3 TikZ/pgfplots `figure`s per chapter,
  with captions naming the same numbers as the text, always referenced from the prose.
- Place the four boxes near the sections they serve, not stacked at the end of the chapter.

## Four reader tiers (required in every chapter)

Different readers need different entrances. These four boxes are those entrances;
do not mix them into the main prose, so that readers can skip them.

| Box | For whom | Required content | Length |
|---|---|---|---|
| `untukanak` | readers aged 10-14, with no mathematics background | one everyday-object analogy, **no mathematical notation** (simple numbers are fine), one question that sparks curiosity, and one sentence "in this chapter we will find out why" | 120-250 words |
| `untukdosen` | lecturers/teachers | a suggested teaching order, 2 typical student misconceptions, one blackboard or classroom activity, and signs that students are ready to move on | 120-250 words |
| `untukpeneliti` | researchers/advanced readers | what is actually proved vs merely popularized, primary sources (work name + section), open questions, and the limits within which the result holds | 120-250 words |
| `\kamus{...}{...}{...}` | all tiers | a new term + its English equivalent + a one-sentence analogy; must be used for 3-5 key terms per chapter | 1-2 sentences |

**Every `\kamus` term must have a glossary entry.** After adding a term in a chapter,
also add a (label, definition) pair in `tools/glosarium.py`, then run
`python3 tools/glosarium.py tulis` — the Glossary Appendix block in `main.tex` is rewritten
in alphabetical order, so do not edit that block by hand. `python3 build_ed2.py
check` flags `Istilah \kamus tanpa entri glosarium: N` if any entry is missing, and
`test_gerbang.py` contains the negative control for it.

Additional rules:
- `untukanak` **must not** use mathematical symbols. If needed, write "akar dua"
  instead of `$\sqrt{2}$`. This box is for curiosity, not for definitions.
- Every `\section` starts with a line `\tingkat{dasar}`, `\tingkat{menengah}`, or
  `\tingkat{lanjut}` so that readers know which parts may be skipped on
  a first reading.
- Every important theorem/definition is preceded by one plain sentence explaining
  what it means in everyday language, before its formal statement.
- Short sentences. One idea per sentence. Avoid nested parentheses.
- Foreign terms are italicized and given an Indonesian equivalent at first occurrence.
- A chapter title is at most 55 characters. If longer, give a short form for
  the running head: `\chapter[Bentuk Pendek]{Judul Panjang yang Sebenarnya}`.
  Without a short form, the running head overflows past the margin in the complete book —
  this defect does **not** appear when the chapter is compiled on its own.
- A chapter title must match exactly its row in the "Peta Ketergantungan Bab" table
  in `main.tex`. The gate checks both; if they differ, fix the table
  (the chapter manuscript is the reference), not the chapter title.

## Required structure of one chapter (target 5,500-6,500 body words)

```
\chapter{Judul Persis Seperti di Tugas}

[2-3 paragraf: satu masalah konkret + mengapa alat bab sebelumnya belum cukup]

\begin{untukanak} ... \end{untukanak}

\section{...}
\tingkat{dasar}
[prosa + definisi/teorema + bukti]

\section{...}
\tingkat{menengah}
...
\section{...}
\tingkat{lanjut}
...

\section{Contoh hitung}
\tingkat{menengah}
[angka eksak, langkah antara ditulis, satu kotak \kertas{...}]

\section{Lab komputasi}
\tingkat{lanjut}
\begin{lab}
\begin{verbatim}
kode Python yang benar-benar dijalankan
\end{verbatim}
\end{lab}
[keluaran nyata apa adanya, lalu tafsirannya]

\begin{untukdosen} ... \end{untukdosen}

\section{Ringkasan}
\begin{ringkasan} ... \end{ringkasan}   % 4-6 butir, padat

\section{Latihan}
\begin{latihan}
\begin{enumerate}
  ... 8-10 butir ...
\end{enumerate}
\end{latihan}

\begin{untukpeneliti} ... \end{untukpeneliti}

\peta{Bab ... pada [kitab] ...}
```

Quantitative requirements checked by the quality gate:
- 5,000-7,500 body words (target 5,500-6,500). Fewer than 5,000 is rejected.
- at least 5 `\section`s, at least 4 theory environments (`definisi`/`teorema`/`lemma`/
  `akibat`/`proposisi`), every theory and example `\section` given a `\tingkat{...}`
  (may be skipped only for `Ringkasan` and `Latihan`).
- 2-4 `untukanak` boxes, exactly 1 `untukdosen`, exactly 1 `untukpeneliti`,
  at least 3 `\kamus{...}{...}{...}`.
- at least 1 `\kertas`, 1 `\peta`, 1 `\begin{lab}`, 1 `\begin{verbatim}`,
  1 `\begin{ringkasan}`.
- 8-10 exercise items; there must be (a) one item "evaluate this claim: true, false, or
  not enough evidence", (b) at least two proof items, (c) at least two computation items that
  can be checked with Python. Include brief hints for the 3 hardest items.
- at least 8 `\index{istilah}` (lowercase, ASCII, one or two words; do not
  index common words such as "bilangan" — the index must be useful).

## What is graded for quality

- Every definition is used in that chapter. Definitions from earlier chapters are cited, not repeated.
- Theorems come with a complete proof, or with an honest statement that the proof is skipped
  together with where it is proved. A half-finished proof is worse than admitting it.
- Worked examples: exact numbers, intermediate steps written out, a final result the
  reader can re-check. Verify with Python before writing the result.
- Computational lab: code you actually ran, output exactly as it came out
  (it may be cut with "..." if long, but the numbers shown must be genuine).
- Exercises can really be done from the chapter's content, not from outside it.
- Tone: explanatory, not preachy; no "jelas sekali" or "mudah".

## How to test the compilation (required, before declaring done)

```bash
cd _buku-ed2/_wrap/chNN   # from the repo root; this is your own directory
cp ../../chNN.tex .
cat > w.tex <<'EOF'
\documentclass[11pt,a4paper]{book}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{makeidx}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage[a4paper,margin=2.5cm]{geometry}
\theoremstyle{definition}\newtheorem{definisi}{Definisi}[chapter]
\theoremstyle{plain}\newtheorem{teorema}{Teorema}[chapter]
\newtheorem{lemma}[teorema]{Lemma}
\newtheorem{akibat}[teorema]{Akibat}
\newtheorem{proposisi}[teorema]{Proposisi}
\theoremstyle{remark}\newtheorem{contoh}{Contoh}[chapter]
\newtheorem{latihan}{Latihan}[chapter]
\newtheorem{catatan}{Catatan}[chapter]
\newtheorem*{ringkasan}{Ringkasan}
\newenvironment{lab}{\par\medskip\noindent\textbf{Lab komputasi}\par\nopagebreak}{\par\medskip}
\newtcolorbox{untukanak}{colback=orange!6,colframe=orange!65!black,
  title={\small\bfseries Untuk pembaca muda (10 tahun ke atas)},
  fonttitle=\bfseries,breakable,left=6pt,right=6pt,top=4pt,bottom=4pt}
\newtcolorbox{untukdosen}{colback=teal!5,colframe=teal!55!black,
  title={\small\bfseries Catatan untuk dosen},
  fonttitle=\bfseries,breakable,left=6pt,right=6pt,top=4pt,bottom=4pt}
\newtcolorbox{untukpeneliti}{colback=black!4,colframe=black!55,
  title={\small\bfseries Untuk peneliti: batas dan lanjutan},
  fonttitle=\bfseries,breakable,left=6pt,right=6pt,top=4pt,bottom=4pt}
\newcommand{\kamus}[3]{\par\smallskip\noindent\colorbox{blue!5}{\parbox{\dimexpr\linewidth-2\fboxsep}{\small\textbf{#1} (\emph{#2}) --- #3}}\par\smallskip}
\newcommand{\tingkat}[1]{\par\noindent{\footnotesize\scshape Tingkat: #1}\par\smallskip}
\newcommand{\kertas}[1]{\par\medskip\noindent\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{\small #1}}\par\medskip}
\newcommand{\peta}[1]{\par\medskip\noindent{\small\itshape Peta ke kitab sumber: #1}\par\medskip}
\makeindex
\begin{document}
\input{chNN.tex}
\printindex
\end{document}
EOF
pdflatex -interaction=nonstopmode -halt-on-error w.tex
makeindex w.idx >/dev/null 2>&1
pdflatex -interaction=nonstopmode -halt-on-error w.tex
```

Replace `chNN` with your chapter number. **Required**: pdflatex finishes with no `!` error and no
overfull box above 10pt. Fix until clean, then delete the auxiliary files
(`w.aux`, `w.log`, `w.idx`, `w.ilg`, `w.ind`, `w.toc`, `w.out`, `w.pdf`, `w.tex`,
and the copy of `chNN.tex`) — the `_wrap/chNN/` directory must be empty when you finish.

## Contents of the whole book (context; do not write other chapters)

**Part I — Foundations: Language, Sets, and Numbers**
1. The Language of Mathematics and the Art of Proof
2. Sets, Relations, Functions, and Cardinality
3. Axioms of the Real Numbers and Supremum
4. Sequences and Limits
5. Infinite Series

**Part II — Linear Algebra**
6. Vector Spaces and Subspaces
7. Basis, Dimension, and Linear Transformations
8. Linear Systems, Determinants, and Inverses
9. Eigenvalues and Diagonalization
10. Orthogonality, SVD, and Least Squares

**Part III — Analysis and Calculus**
11. Continuity and Uniform Continuity
12. Derivatives: One and Several Variables
13. Riemann Integrals and the Fundamental Theorem of Calculus
14. Series of Functions and the Exchange of Limits
15. Multiple Integrals, Change of Variables, and Vector Field Theorems

**Part IV — Probability, Statistics, and Computer Arithmetic**
16. Probability and Conditional Probability
17. Random Variables and Distributions
18. The Law of Large Numbers and the Central Limit Theorem
19. Estimation, Confidence Intervals, and Hypothesis Testing
20. Floating-Point Arithmetic and Error Analysis

**Part V — Optimization**
21. Convex Optimization and Duality
22. Linear and Integer Programming

**Part VI — Machine Learning and Security**
23. Neural Networks and Backpropagation
24. Generalization, Regularization, and Training
25. Honest Model Evaluation
26. Formal Methods with Lean 4
27. Adversarial Machine Learning: Attacks and Defenses
28. The Limits of Attack: Obfuscated Gradients and NIDS Evasion
