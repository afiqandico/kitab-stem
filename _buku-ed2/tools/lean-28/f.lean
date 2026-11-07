theorem aman (f : Nat -> Nat) (x : Nat) : exists delta : Nat, f (x + delta) = f x := by
  exact ⟨0, rfl⟩
