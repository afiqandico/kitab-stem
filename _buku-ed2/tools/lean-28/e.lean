def evenSum : Nat -> Nat
  | 0     => 0
  | n + 1 => evenSum n + 2 * n

theorem benar (n : Nat) : evenSum n + n = n * n := by
  induction n with
  | zero => rfl
  | succ k ih =>
    rw [evenSum]
    have h : evenSum k + 2 * k + (k + 1) = (evenSum k + k) + (2 * k + 1) := by omega
    rw [h, ih]
    simp only [Nat.mul_add, Nat.add_mul, Nat.mul_one, Nat.one_mul]
    omega
