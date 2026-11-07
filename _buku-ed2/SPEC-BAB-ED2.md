# Specification of the 32 chapters — First Edition

> **Numbering note (October 2026).** This file originally numbered thirty chapters.
> After Chapter 16 (Differential Equations and Dynamical Systems) and Chapter 21 (Regression and
> Applied Statistics) were inserted, the numbering shifted: 1--15 stay; 16--19 become
> 17--20; 20 becomes 22; 21--30 become 23--32. The chapter titles below remain valid as
> content; the numbers follow that map. The specifications of the two new chapters are at the end of the file.

Read `PANDUAN-BAB-ED2.md` first (the absolute rules **and the "Four reader
tiers" section**). This file only supplies content.

Cross-chapter reminder (applies to every chapter below): each chapter must contain
2-4 `untukanak` boxes, 1 `untukdosen`, 1 `untukpeneliti`, at least 3 `\kamus`, and
every `\section` given a `\tingkat{dasar|menengah|lanjut}`. The tier boxes do not
replace the main prose: the theory content stays complete and formal, while the boxes
are entrances and notes for other readers.

The source PDFs are in `~/Documents/05_Archive/kitab-stem-sumber-2026-11-07/<folder>/`. Read a slice with
`pdftotext -f N -l M "<berkas>" -` (do not dump the whole file; limit yourself to 2-4 pages
per read and search the result with `grep -n`). Python: `source ~/venv/bin/activate`.

The **Basis** column points to a first-edition chapter in `../_buku/` that you may read as
starting material. Expand and deepen it; do not copy it raw, and you must re-verify
the old numbers yourself.

---

## Chapter 1 — Mathematical Language and the Art of Proof
Basis: `../_buku/ch01.tex`. Sections: (1) statements, logical connectives, truth
tables, quantifiers and how to negate them; (2) reading definitions literally
(definitions as necessary-and-sufficient conditions, counterexamples); (3) four proof patterns:
direct, contrapositive, contradiction, constructive; (4) mathematical induction and strong
induction; (5) when proof fails: the claim that $n^2+n+41$ is prime for all $n \ge 0$ breaks at
$n=40$, one typical flawed proof and where its defect lies; (6) writing a proof that others
can check (sentence structure, notation, what may be skipped).
Must be computed: the value of $n^2+n+41$ for $n=0..40$ and the factorization at $n=40$; the sum
$1+3+\dots+(2n-1)$ for several $n$; the negation of two quantified statements.
Sources: `Analisis Real/Abbott - Understanding analysis.pdf` (the opening part on
sets and proofs), `Metode Formal & Lean 4/mathematics_in_lean.pdf` (introduction).

## Chapter 2 — Sets, Relations, Functions, and Cardinality
Basis: none (new chapter). Sections: (1) sets, operations, De Morgan's laws, power
sets; (2) Cartesian products and relations; (3) equivalence relations and partitions;
(4) functions: injective, surjective, bijective, composition, inverse; (5) finite,
countable, and uncountable sets; Cantor's diagonal argument; (6) inequalities, absolute value, and
supremum as a tool (without constructing $\mathbb{R}$; that is Chapter 3).
Must be computed: the number of subsets $2^n$ for small $n$ and a check of the
enumeration with Python; the Cantor pairing as a bijection $\mathbb{N}\times\mathbb{N}
\to \mathbb{N}$ (check 10 values); an enumeration of the positive $\mathbb{Q}$.
Sources: `Analisis Real/Abbott - Understanding analysis.pdf` (the parts on sets,
cardinality, infinite sets), `Aljabar Linear/Kenneth M Hoffman, Ray Kunze -
Linear Algebra (2nd Edition)-Prentice Hall (1971).pdf` (the chapters on sets and
functions), `Metode Formal & Lean 4/mathematics_in_lean.pdf` (sets and functions).

## Chapter 3 — Axioms of the Real Numbers and Supremum
Basis: the first half of `../_buku/ch02.tex`. Sections: (1) field axioms; (2) order
axioms and their consequences; (3) absolute value and the triangle inequality; (4) completeness:
least upper bound, the supremum property, consequences (Archimedes, density of $\mathbb{Q}$);
(5) why $\mathbb{Q}$ is not enough and the existence of $\sqrt{2}$ (proof + Newton
approximation); (6) intervals, accumulation points, open and closed sets (briefly,
without full topology).
Must be computed: 5 Newton iterations for $\sqrt{2}$ with the relative error at each
step; a sequence of rational approximations with error $<10^{-6}$; verification that
$\{q \in \mathbb{Q}: q^2<2\}$ has no maximum.
Sources: `Analisis Real/Rudin Principles of Mathematical Analysis.pdf` (the chapter on the
real number system), `Analisis Real/Abbott - Understanding analysis.pdf` (the chapter on real
numbers).

## Chapter 4 — Sequences and Limits
Basis: the second half of `../_buku/ch02.tex`. Sections: (1) the $\varepsilon$-$N$ definition and
how to use it; (2) uniqueness of the limit, algebraic properties of limits (proof); (3) the
squeeze theorem and the ratio test for sequences; (4) monotone sequences and the monotone convergence theorem;
(5) subsequences, Bolzano-Weierstrass, Cauchy sequences and completeness; (6) limit
superior and inferior.
Must be computed: an explicit $N$ for $(3n+1)/(n+2) \to 3$ at $\varepsilon=10^{-2}$
and $10^{-4}$; $(1+1/n)^n$ for $n=10,10^2,\dots,10^7$; the recursive sequence
$x_{n+1}=\sqrt{2+x_n}$ (limit and error).
Sources: Rudin (the chapter on sequences and series of numbers), Abbott (the chapter on sequences and series).

## Chapter 5 — Infinite Series
Basis: none (new chapter; do not reuse the content of Chapter 4 as prose). Sections:
(1) series, partial sums, geometric and telescoping series; (2) the $n$-th term test and
the comparison test; (3) the ratio test, the root test, $p$-series; (4) alternating series and
the Leibniz test with its error bound; (5) absolute convergence, regrouping, and
the Riemann rearrangement theorem (statement); (6) the very slowly divergent harmonic
series: why $H_{10^6}$ is still about 14.
Must be computed: $H_{10^6}$ with numpy (and the estimate $\ln n+\gamma$); the truncation
error of the Leibniz series for $\pi/4$ at 1000 terms; the sum $\sum 1/n^2$ numerically
vs $\pi^2/6$; the ratio test on two series with different outcomes.
Sources: Rudin (the chapter on sequences and series of numbers), Abbott (the chapter on sequences and series).

## Chapter 6 — Vector Spaces and Subspaces
Basis: the first half of `../_buku/ch03.tex`. Sections: (1) vector space axioms and
examples ($\mathbb{R}^n$, matrix spaces, function spaces, polynomial spaces); (2) subspaces
and the subspace test; (3) linear combinations and span; (4) linear independence and
dependence; (5) basis and dimension (the exchange theorem, with proof); (6) direct
sums and complementary subspaces.
Must be computed: the rank and a column-space basis of a $3\times4$ matrix (numpy +
manual elimination); a check that three vectors in $\mathbb{R}^3$ are dependent;
the dimension of the polynomial space of degree $\le 3$.
Sources: `Aljabar Linear/Book_H_Anton_11_Ed_Linear_Algebra.pdf` (the chapter on general
vector spaces), `Aljabar Linear/LADR4e.pdf` (the chapters on vector spaces and
finite-dimensional vector spaces).

## Chapter 7 — Basis, Dimension, and Linear Transformations
Basis: the second half of `../_buku/ch03.tex`. Sections: (1) coordinates relative to a basis and
change-of-basis matrices; (2) linear transformations, kernel, range; (3) representation
matrices and their link to matrix multiplication; (4) rank-nullity with proof;
(5) isomorphisms and dimension invariance; (6) linear transformations on finite-dimensional
spaces expressed as matrices (the space $\mathcal{L}(V,W)$).
Must be computed: a $3\times3$ matrix with one dependent row: rank, nullity,
kernel and range bases step by step; verification with `numpy.linalg.matrix_rank`
and `scipy.linalg.null_space`; the representation matrix of one transformation in two different
bases and a check that $[T]_{\mathcal{B}'} = P^{-1}[T]_{\mathcal{B}}P$.
Sources: Anton (the chapter on general linear transformations), Axler (the chapter on linear maps), Hoffman-Kunze
(the chapter on linear transformations).

## Chapter 8 — Linear Systems, Determinants, and Inverses
Basis: none (new chapter). Sections: (1) row echelon form and Gaussian elimination,
the single/many/no-solution cases; (2) determinants: the axiomatic definition
(multilinear and alternating), properties, cofactor expansion; (3) Cramer's rule and
the adjugate; (4) matrix inverses, elementary matrices, and equivalent
invertibility conditions; (5) computational cost and condition number (a bridge to Chapter 20).
Must be computed: one $3\times3$ system solved two ways (elimination and Cramer);
a $4\times4$ determinant by cofactor expansion vs `numpy.linalg.det`; the condition
number of a $4\times4$ Hilbert matrix; a nearly singular system (the solution jumps).
Sources: Anton (the chapter on linear systems and matrices, the chapter on determinants),
Hoffman-Kunze (the chapter on linear equations, the chapter on determinants).

## Chapter 9 — Eigenvalues and Diagonalization
Basis: the first half of `../_buku/ch04.tex`. Sections: (1) the characteristic polynomial and
eigenvalues as its roots; (2) eigenspaces, algebraic and geometric multiplicity;
(3) the diagonalizability condition (proof); (4) similar matrices and invariants; (5) an example
$2\times2$ that fails to diagonalize; (6) applications: matrix powers, linear
differential systems, a short Markov chain.
Must be computed: the eigenvalues and eigenvectors of one $3\times3$ matrix (numpy, with
a check of $A\mathbf{v}=\lambda\mathbf{v}$); $A^{10}$ via diagonalization vs
direct multiplication; one defective matrix and the rank of its eigenspace.
Sources: Anton (the chapter on eigenvalues), Axler (the chapter on eigenvalues and eigenvectors, the chapter on
operators on complex vector spaces), Hoffman-Kunze (the chapter on elementary canonical forms).

## Chapter 10 — Orthogonality, SVD, and Least Squares
Basis: the second half of `../_buku/ch04.tex`. Sections: (1) inner products, norms,
the Cauchy-Schwarz inequality (proof); (2) orthogonal sets, projections, Gram-Schmidt
and its classical instability; (3) least squares: normal equations, geometric
interpretation; (4) the singular value decomposition $A=U\Sigma V^{\top}$ and its link to
the eigenvalues of $A^{\top}A$; (5) the pseudoinverse and the minimum-norm solution; (6) why SVD
is numerically safer than the normal equations.
Must be computed: the projection of one vector onto a two-dimensional subspace; least squares
for a $5\times2$ matrix via normal equations vs `numpy.linalg.lstsq` (error difference
and condition number); the SVD of one $3\times2$ matrix (singular values, rank, condition
ratio); manual Gram-Schmidt vs `numpy.linalg.qr` (orthogonality $\|Q^{\top}Q-I\|$).
Sources: Axler (the chapter on inner product spaces, the chapter on operators on inner product spaces),
`Introduction to Linear Algebra 6th edition...pdf` (the chapter on orthogonality, the chapter on the SVD),
Anton (the chapter on inner product spaces).

## Chapter 11 — Continuity and Uniform Continuity
Basis: the first half of `../_buku/ch05.tex`. Sections: (1) limits of functions and the
$\varepsilon$-$\delta$ definition; (2) continuity, algebraic properties, composition; (3) the intermediate
value theorem and the extreme value theorem (brief proofs); (4) uniform continuity and
how it differs from pointwise continuity; (5) $x^2$ is not uniformly continuous on
$\mathbb{R}$ but is on $[0,1]$; Lipschitz; (6) a function continuous at only
one point, and a modified Dirichlet function.
Must be computed: an explicit $\delta$ for $f(x)=x^2$ at $x_0=2$ for
$\varepsilon=10^{-3}$; a search for a $\delta$ that fails to be uniform at large $x_0$
(numerical table); the continuity of $1/x$ on $[1,\infty)$ vs $(0,1]$.
Sources: Rudin (the chapter on continuity), Abbott (the chapter on limits of functions and continuity).

## Chapter 12 — Derivatives: One and Several Variables
Basis: the second half of `../_buku/ch05.tex`. Sections: (1) the definition of the derivative and
basic rules; (2) the chain rule with proof; (3) the mean value theorem and its consequences
(monotonicity, zero derivative, inequalities); (4) Taylor polynomials with remainder;
(5) partial derivatives, gradient, Jacobian; differentiability vs partials existing (a
counterexample); (6) the multivariable chain rule and the Hessian matrix.
Must be computed: finite differences vs the analytic derivative for one function at several $h$;
the gradient and Jacobian of one function $\mathbb{R}^2\to\mathbb{R}^2$ at one point;
a check of the multivariable chain rule via numerical composition; an example of a function whose
partials exist at $(0,0)$ but which is not continuous.
Sources: Rudin (the chapter on differentiation), Abbott (the chapter on derivatives),
`Kalkulus Multivariabel/Stewart.pdf` (the chapter on partial derivatives),
`Kalkulus Multivariabel/spivak-calculus-on-manifolds.pdf` (the chapter on differentiation).

## Chapter 13 — Riemann Integrals and the Fundamental Theorem of Calculus
Basis: the first half of `../_buku/ch06.tex`. Sections: (1) partitions, upper and lower
sums, the integrability criterion; (2) classes of integrable functions (continuous,
monotone) and an example of a non-integrable function; (3) the fundamental theorem of calculus, parts
1 and 2 with proofs; (4) substitution and integration by parts; (5) the mean value theorem
for integrals; (6) improper integrals briefly and their link to series (Chapter 5).
Must be computed: left/right/midpoint Riemann sums for $\int_0^1 x^2\,dx$
with $n=10,100,1000$ and their error rates ($\mathcal{O}(1/n)$, $\mathcal{O}(1/n^2)$);
a comparison with `scipy.integrate.quad`; one integral whose value cannot
be computed with an elementary antiderivative.
Sources: Rudin (the chapter on the Riemann-Stieltjes integral), Abbott (the chapter on the Riemann integral).

## Chapter 14 — Series of Functions and the Exchange of Limits
Basis: the second half of `../_buku/ch06.tex`. Sections: (1) pointwise vs uniform
convergence; (2) the Weierstrass M-test and the example $x^n$ on $[0,1]$; (3) exchanging limits
with continuity, differentiation, and integration (three theorems + proof sketches); (4) power
series, radius of convergence, term-by-term differentiation and integration; (5) an example where
the exchange fails and its practical cost; (6) approximating functions with series and
the resulting error bounds.
Must be computed: $\sup_{x\in[0,1]} |x^n - 0|$ for several $n$; the approximation error
of $\exp(x)$ with a Taylor series at $x=1$ up to term $N$; the radius of convergence of three
power series.
Sources: Rudin (the chapter on sequences and series of functions), Abbott (the chapter on sequences and series of functions).

## Chapter 15 — Multiple Integrals, Change of Variables, and Vector Field Theorems
Basis: none (new chapter). Sections: (1) double and triple integrals, Fubini's
theorem; (2) change of variables and the Jacobian determinant; polar, cylindrical,
and spherical coordinates; (3) line integrals and conservative fields; (4) Green, Gauss, and Stokes
theorems (statement + one example each); (5) differential forms as the general
language (an introduction via Spivak, without full formalism); (6) when the vector field
theorems fail (boundary conditions and singularities).
Must be computed: one multiple integral over a circular region computed two ways (Cartesian
vs polar) and checked with `scipy.integrate.dblquad`; the volume of a ball with the spherical
Jacobian; one line integral computed directly vs via a potential.
Sources: `Kalkulus Multivariabel/Stewart.pdf` and `.../Calculus Early
Transcendentals 9th Edition...pdf` (the chapter on multiple integrals, the chapter on vector calculus),
`Kalkulus Multivariabel/acm-full-text.pdf` (Active Calculus: multiple integrals and
vector calculus), `Kalkulus Multivariabel/spivak-calculus-on-manifolds.pdf`
(integration on chains and manifolds).

## Chapter 16 — Probability and Conditional Probability
Basis: the first half of `../_buku/ch07.tex`. Sections: (1) probability axioms and their consequences;
(2) counting and combinatorial probability; (3) conditional probability and the multiplication
rule; (4) Bayes' theorem with a two-step example and a medical interpretation; (5)
independence and the "mutually exclusive" misunderstanding; (6) paradoxes that demand computation
(the birthday problem, Monty Hall).
Must be computed: the Bayes probability for a diagnostic test with given sensitivity and
specificity; the birthday probability for $n=23$ and $n=50$; a Monty Hall
simulation with at least $10^4$ trials in numpy.
Sources: `Probabilitas & Statistika/preview-9780429766749_A36188955.pdf`
(Blitzstein-Hwang: probability and counting, conditional probability).

## Chapter 17 — Random Variables and Distributions
Basis: the second half of `../_buku/ch07.tex`. Sections: (1) random variables, mass functions,
densities, cumulative distribution functions; (2) expectation, variance, moments; (3) the
Bernoulli, binomial, geometric, Poisson distributions; (4) the normal and exponential distributions, and
their link; (5) joint distributions, covariance, correlation; (6) transformations of random
variables and the Jacobian.
Must be computed: derive the binomial mean and variance, then match them against a
$10^5$ Monte Carlo; the sum of the Poisson pmf for several $\lambda$ (must be 1 within machine
error); the transformation $Y=X^2$ for uniform $X$ and a check of the resulting density.
Sources: Blitzstein-Hwang (random variables and their distributions, expectation),
`Probabilitas & Statistika/2004 - wasserman - all of statistics.pdf` (probability,
random variables, expectation).

## Chapter 18 — The Law of Large Numbers and the Central Limit Theorem
Basis: the third part of `../_buku/ch07.tex`. Sections: (1) sequences of random variables and
convergence in probability; (2) the weak law of large numbers (proof via Chebyshev's
inequality) and the strong law (statement); (3) the central limit theorem and a proof sketch
via characteristic functions; (4) the normal approximation, continuity correction; (5) the
Monte Carlo error rate and why $1/\sqrt{n}$ is slow; (6) when the CLT misleads
(heavy tails, infinite variance).
Must be computed: an LLN simulation for the mean of a die at $n=10,10^2,\dots,10^5$;
a CLT simulation for exponential means (compare quantiles with the normal, test
Kolmogorov-Smirnov via scipy); the empirical Monte Carlo standard error vs $1/\sqrt{n}$;
one heavy-tailed distribution example (Cauchy) that violates the CLT.
Sources: Blitzstein-Hwang (the convergence part), Wasserman (the chapter on convergence of
random variables, the chapter on inequalities).

## Chapter 19 — Estimation, Confidence Intervals, and Hypothesis Testing
Basis: the fourth part of `../_buku/ch07.tex` + the Wilson and rule-of-three parts of
`../_buku/ch11.tex`. Sections: (1) estimators, bias, variance, standard error; (2) confidence
intervals for a mean (normal and t); (3) confidence intervals for a proportion: Wald vs
Wilson, with a comparison table; (4) the rule of three for zero events; (5) hypothesis
testing, p-values, type I/II errors, power; (6) the most common
p-value misinterpretations, and how to report results correctly.
Must be computed: Wilson and Wald for 33/50 and 53/100 (compare the width and
behaviour near 0 and 1); the rule of three for $n=100$; a power simulation for a proportion test
for one scenario (numpy) and a comparison with the normal approximation formula.
Sources: Wasserman (the chapter on statistical inference and learning, the chapter on
parametric inference, the chapter on hypothesis testing and p-values), Blitzstein-Hwang (the expectation and
convergence parts).

## Chapter 20 — Floating-Point Arithmetic and Error Analysis
Basis: `../_buku/ch08.tex`. Sections: (1) the IEEE-754 format: sign, exponent, mantissa,
bias; normal and subnormal; (2) rounding, ULP, machine epsilon; (3) $0.1+0.2 \ne
0.3$ and the actual difference in ULP; (4) absolute/relative error, condition
number, loss of significant digits; (5) algorithmic instability: $(1-\cos x)/x^2$
for small $x$, sequential summation vs Kahan summation; (6) practical guidelines
for writing numerical code.
Must be computed: the `struct`/`numpy.float32` bitfields for several numbers and
`float.hex()`; ULP and machine epsilon; Kahan vs naive summation for $10^6$ terms;
the relative error of $(1-\cos x)/x^2$ at $x=10^{-1},\dots,10^{-10}$ and a comparison
with the Taylor series.
Sources: `Numerik/goldberg.pdf`.

## Chapter 21 — Convex Optimization and Duality
Basis: the first half of `../_buku/ch09.tex`. Sections: (1) convex sets and
convex combinations; (2) convex functions, first- and second-order tests (positive definite
Hessian); (3) the standard form of an optimization problem and why convex means a global
optimum; (4) the Lagrangian, the Lagrange dual, weak duality with proof, strong duality
and Slater's condition (statement); (5) the KKT conditions and the interpretation of multipliers; (6) a small
quadratic example solved via KKT.
Must be computed: one two-variable QP with constraints, solved via KKT
by hand then `scipy.optimize.minimize` (compare $x^{*}$ and the multipliers); a
Hessian convexity test for one function of two variables (eigenvalues); an illustration of the duality gap
on one small nonconvex problem.
Sources: `Optimasi & Neural Networks/bv_cvxbook.pdf` (the chapter on convex sets, the chapter on
convex functions, the chapter on convex optimization problems, the chapter on duality).

## Chapter 22 — Linear and Integer Programming
Basis: the second half of `../_buku/ch09.tex`. Sections: (1) standard LP form and formulation;
(2) geometry: extreme points and vertices; (3) the simplex method: one tableau
worked through in full; (4) LP duality, complementary slackness, and the interpretation of shadow prices;
(5) LP relaxation for integer programs, integrality gap, branch and bound; (6) one small
integer program solved by enumeration and with `scipy.optimize.milp`.
Must be computed: one two-variable LP graphically and with `scipy.optimize.linprog`
(optimal value and shadow prices); the dual and a numerical check of strong
duality; one IP (a 4-item knapsack) via enumeration vs MILP, plus the integrality gap
of its relaxation.
Sources: `Optimasi & Neural Networks/WSPrinted.pdf` (Bertsimas-Tsitsiklis: formulation,
geometry, simplex, duality), `Optimasi & Neural Networks/IntegerProgramming-Wolsey.pdf`
(formulation and relaxation).

## Chapter 23 — Neural Networks and Backpropagation
Basis: `../_buku/ch10.tex`. Sections: (1) the perceptron and linear boundaries; (2) MLPs,
activation functions (ReLU, sigmoid), universal approximation (statement); (3) softmax
and cross-entropy; (4) complete backpropagation for a network with 4 inputs - 2 ReLU units
- 1 sigmoid output, all numbers exact; (5) numerical gradient checking; (6)
the gradient with respect to the inputs (a bridge to Chapter 27) and one gradient descent step.
Must be computed: an exact forward pass with prescribed weights; the gradient of every
weight by hand and with numpy (the difference must be below $10^{-12}$); one
gradient descent step with a given learning rate; the gradient with respect to the inputs
verified by finite differences.
Sources: `Optimasi & Neural Networks/book.pdf` (Nielsen, chapters 1-2),
`Optimasi & Neural Networks/Deep+Learning+Ian+Goodfellow.pdf` (the deep
feedforward networks part).

## Chapter 24 — Generalization, Regularization, and Training
Basis: none (new chapter). Sections: (1) training vs test error; underfitting and
overfitting; (2) the bias-variance decomposition; (3) L2 and L1 regularization, early stopping,
dropout; (4) feature standardization using training-data statistics only (data leakage);
(5) gradient descent: SGD, momentum, Adam — how the updates differ; (6) learning
rate schedules, hyperparameter selection, and an honest validation protocol.
Must be computed: a small numpy experiment (logistic regression or a one-layer MLP) on
synthetic data with three settings (no regularization, L2, L1) — report the training and
validation error, and show overfitting concretely; one optimization trajectory
SGD vs Adam (number of steps to an error threshold).
Sources: Goodfellow (the chapter on regularization for deep learning, the chapter on optimization for
training deep models), Nielsen (the chapter on improving the way neural networks learn).

## Chapter 25 — Honest Model Evaluation
Basis: `../_buku/ch11.tex` (except the Wilson part already used in Chapter 19) and
examples from `../note.md` where relevant. Sections: (1) confusion matrices and derived metrics
(precision, recall, F1) and when each metric misleads; (2) ROC curves and AUC,
and their dependence on prevalence; (3) class imbalance and deceptive
accuracy; (4) metric uncertainty: intervals for proportions (see Chapter 19), the rule
of three, intervals for the difference between two models; (5) data leakage, train/test splits,
correct cross-validation; (6) a checklist for reporting experimental results.
Must be computed: an example confusion matrix with 1000 predictions (precision/recall/F1
by hand vs `sklearn` if available, otherwise numpy); AUC from a small score dataset
computed by hand; the effect of prevalence on precision at fixed recall; an example of leakage
that artificially raises test accuracy (a small simulation).
Sources: Wasserman (the chapter on models, statistical inference and learning),
`../note.md` (the author's own worked example; state its limits).

## Chapter 26 — Formal Methods with Lean 4
Basis: `../_buku/ch12.tex`. Sections: (1) propositions as types, proofs as terms;
(2) quantifiers and introduction/elimination rules; (3) basic tactics (`intro`, `exact`, `rw`,
`simp`, `induction`, `linarith`); (4) one complete induction proof (the sum of odd
numbers $=n^2$) written in stages with an explanation of each tactic; (5) structures,
typeclasses, and `native_decide`: what is actually guaranteed, what is assumed;
(6) the limits of formalization: a wrong specification yields a useless proof;
its link to certificates and honest model evaluation (Chapter 25).
Must be stated honestly: Lean is **not installed** on this machine, so the code snippets are not
executed; the code was matched against `mathematics_in_lean.pdf` and `print.pdf` and
the chapter says so. The numbers computed (e.g. the sum of odd numbers
for several $n$) are still verified with Python.
Sources: `Metode Formal & Lean 4/mathematics_in_lean.pdf`,
`.../matematika-dalam-lean-bahasa-indonesia.pdf`, `.../print.pdf` (Theorem Proving
in Lean 4).

## Chapter 27 — Adversarial Machine Learning: Attacks and Defenses
Basis: the first half of `../_buku/ch13.tex`. Sections: (1) threat definitions: the
$L_\infty$ norm, $\varepsilon$, the attacker's goal; (2) why the sign of the gradient suffices:
deriving FGSM from linearization; (3) PGD and the min-max formulation, adversarial training;
(4) transferability and black-box attacks; (5) numerical examples on a linear model
and a small MLP (gradient with respect to the inputs, change in prediction); (6) computational cost
and practical limitations.
Must be computed: FGSM on a linear model with given weights (the exact change in output);
multi-step PGD on a small MLP: clean accuracy vs accuracy under
attack for several $\varepsilon$; a comparison with finite-difference gradients.
Sources: `Adversarial ML/1412.6572v3.pdf` (FGSM),
`Adversarial ML/1706.06083v4.pdf` (PGD, adversarial training).

## Chapter 28 — The Limits of Attack: Obfuscated Gradients and NIDS Evasion
Basis: the second half of `../_buku/ch13.tex` + `../note.md`. Sections: (1) seven techniques
for obfuscating gradients and why evaluation becomes misleading; (2) attacks that
break through them: BPDA, EOT, reparameterization; (3) how to design an honest
evaluation (adaptive budget, several seeds, report the variance); (4) case study: evasion
against ML-based NIDS, why dynamic NIDS are more robust; (5) the author's own results
from `note.md` — label them as the author's work, include their limits
explicitly, and do not claim more than the notes contain; (6) a checklist
for a claim that "the attack succeeded".
Must be computed: an attack simulation on a classifier with deliberately obfuscated
gradients (e.g. output quantization) and a demonstration that a naive attack fails
while the model stays fragile (a simple BPDA, numpy); success metrics with
several seeds (mean and spread).
Sources: `Adversarial ML/1802.00420v4.pdf` (obfuscated gradients),
`main/Evasion Adversarial Attacks Remain Impractical Against ML-based Network
Intrusion Detection Systems, Especially Dynamic Ones.pdf`, `../note.md`.

## Chapter 29 — Cryptography: Modular Integers to the Quantum Threat

Prerequisites: Chapters 2, 3, 26. Added 2026-10-24 by the author's decision so that the title
"to Machine Learning Security" would not stop at adversarial attacks.
Content: modular arithmetic and residue classes; gcd, Euclid, modular inverses; Fermat's little
theorem and Euler's theorem with proofs; cyclic groups, just enough; Diffie-Hellman with a worked
example computed in Python; RSA (why it works, why it is wrong without padding); hashes and MACs;
signatures; computational security as an assumption, not a theorem; Shor and what it
collapses; post-quantum cryptography conceptually; one section that
links leakage through outputs to the threat patterns of Chapters 27-28.
Required figure: a modular clock and/or the Diffie-Hellman flow (TikZ, captioned, referenced).

## Chapter 30 — Differential Privacy and the Mathematical Foundations of QML

Prerequisites: Chapters 10, 16, 17. Added 2026-10-24 to close the gap on "privacy" and
"quantum", which had zero occurrences in the previous edition.
Content: data leakage through models and membership inference attacks; the
$\varepsilon$-$\delta$ definition and why we choose a worst-case guarantee, not an average one;
global sensitivity; the Laplace mechanism with a proof of its guarantee; Gaussian, just enough;
composition and the privacy budget; DP-SGD (clipping + noise) and the privacy-utility
trade-off; the limits of DP claims. Then the foundations of QML: complex numbers, modulus and
phase, finite-dimensional Hilbert space, bra-ket, unitary gates and norm preservation,
Fourier as a change of basis, the Born rule, one 1-2 qubit circuit computed by hand,
and the $2^{n}$ dimension explosion as the reason advantage claims must be kept in check.
Required figure: a trade-off curve from a real experiment or a phase diagram (TikZ).
Honesty: QML has no settled proof of practical advantage yet; state its limits.


---

## Chapter 16 — Differential Equations and Dynamical Systems

**File:** `ch16.tex` · **Part III** · **Prerequisites:** Chapters 12, 14, 15
**Key message:** a differential equation is not a formula to be guessed, but
a promise that tomorrow's state is determined by today's state — and that promise needs conditions so it
does not break.

Minimum content:
1. First-order ODEs: separation of variables, linear equations + integrating factor, examples of decay
   rate and Newton cooling.
2. When a solution exists and is unique: the Lipschitz condition, the Picard-Lindelof theorem (full
   statement, proof sketch via Picard iteration), the example $x'=\sqrt{|x|}$ that fails uniqueness.
3. Autonomous systems and phase portraits: two dimensions, trajectories, equilibrium points, linearization
   using eigenvalues (links to Chapter 9), classification of nodes/saddles/centers.
4. The harmonic oscillator, damping, the nonlinear pendulum: why linearization only holds locally.
5. Numerical methods: Euler (local error order 2, global order 1), 4th-order Runge-Kutta,
   a comparison on one problem whose exact solution is known; stiffness qualitatively.
6. Lyapunov stability: definition, a simple Lyapunov function, the pendulum example with energy.
7. One researcher box: why long-run numerical integration can give answers
   that look plausible but are qualitatively wrong.

**Figures (3):** (a) the pendulum phase portrait with several trajectories; (b) Euler vs
RK4 error against step size on a log-log scale; (c) a classification diagram of equilibrium points
by the sign and type of the eigenvalues.

---

## Chapter 21 — Regression and Applied Statistics

**File:** `ch21.tex` · **Part IV** · **Prerequisites:** Chapters 10, 20
**Key message:** regression is a projection, and every number that comes out of it is only
as honest as the assumptions that accompany it.

Minimum content:
1. Simple and multiple linear regression from least squares; the normal equations
   $X^{\top}X\hat{\beta}=X^{\top}y$ derived via orthogonal projection (Chapter 10).
2. Interpretation of coefficients together with their units; what changes when one explanatory variable
   is rescaled.
3. The Gauss-Markov assumptions and the meaning of "best linear unbiased estimator"; when those assumptions
   are violated and what follows.
4. $R^2$, its correlation with the residuals, and why a high $R^2$ is not proof that the model is right.
5. Confidence intervals and the $t$ test for coefficients (links to Chapter 20); prediction intervals
   versus intervals for the mean.
6. Residual diagnostics: patterns, heteroscedasticity, outliers; multicollinearity and VIF.
7. Logistic regression briefly: why OLS is not used for binary outcomes,
   and how its coefficients are interpreted via odds ratios.
8. Correlation is not causation, with Simpson's paradox using a table of numbers computed
   in full inside the chapter.
9. Researcher box: honest reporting — number of observations, data splits, and the ban on
   choosing a model after seeing the results.

**Figures (2-3):** (a) data points + least-squares line + residuals as vertical segments;
(b) the multiple-regression surface projected as contours on two variables; (c) Simpson's
paradox: two group trends running opposite to the pooled trend.
