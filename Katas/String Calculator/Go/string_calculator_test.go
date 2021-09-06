package main

import "testing"

func TestStringCalculator(t *testing.T) {
	assertEqual := func(t testing.TB, want, got int) {
		t.Helper()
		if got != want {
			t.Errorf("Expected %d but received %d", want, got)
		}
	}

	t.Run("should return sum of two comma separated numbers", func(t *testing.T) {
		want := 3
		got := Add("1,2")
		assertEqual(t, want, got)
	})

	t.Run("should return 0 for empty string", func(t *testing.T) {
		want := 0
		got := Add("")
		assertEqual(t, want, got)
	})

	t.Run("should return sum of more than two comma separated numbers", func(t *testing.T) {
		want := 15
		got := Add("1,2,3,4,5")
		assertEqual(t, want, got)
	})

	t.Run("should return sum of two numbers separated by comma or newline", func(t *testing.T) {
		want := 6
		got := Add("1\n2,3")
		assertEqual(t, want, got)
	})
}
