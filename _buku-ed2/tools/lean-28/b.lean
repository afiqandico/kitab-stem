def oddSum : Nat -> Nat
  | 0     => 0
  | n + 1 => oddSum n + (2 * n + 1)

theorem bantu (k : Nat) : k * (2 * k) + 2 * (2 * k + 1) = (k + 1) * (2 * (k + 1)) := by
  simp only [Nat.mul_add, Nat.add_mul, Nat.mul_one, Nat.one_mul]
  omega

theorem dua_S (n : Nat) : 2 * oddSum n = n * (2 * n) := by
  induction n with
  | zero => rfl
  | succ k ih =>
    rw [oddSum, Nat.mul_add, ih]
    exact bantu k
