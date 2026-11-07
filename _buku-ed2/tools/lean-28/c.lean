def oddSum : Nat -> Nat
  | 0     => 0
  | n + 1 => oddSum n + (2 * n + 1)

theorem dua_S_omega (n : Nat) : 2 * oddSum n = n * (2 * n) := by
  induction n with
  | zero => rfl
  | succ k ih =>
    rw [oddSum, Nat.mul_add, ih]
    omega
