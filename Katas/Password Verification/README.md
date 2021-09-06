# Password Verification Kata
### Created with TDD
### Inspired by: https://osherove.com/tdd-kata-3

---

## Requirements

Create a Password verifications class or function for the purposes of password verification.  Verification will fail if any one of the rules mentioned does not pass.

1. Implement the following rules:

   - password should be larger than 8 chars

   - password should not be null

   - password should have one uppercase letter at least

   - password should have one lowercase letter at least

   - password should have one number at least

     Each one of these should throw an exception with a different message of your choosing

2. Add feature: Password is OK if at least three of the previous conditions is true

3. Add feature: password is never OK if item 1.4 is not true.

4. Assume each verification takes 1 second to complete. How would you solve  items 2 and 3  so tests can run faster?