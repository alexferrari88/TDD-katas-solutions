# String calculator Kata (extended version)
### Created with TDD
### Inspired by: https://osherove.com/tdd-kata-2

---

## Requirements

1. Add Logging Abilities to your new String Calculator (to an ILogger.Write()) interface (you will need a mock). Every time you call Add(), the sum result will be logged to the logger.
2. When calling Add() and the logger throws an exception, the string calculator should notify an IWebservice of some kind that logging has failed with the message from the logger’s exception (you will need a mock and a stub).
3. Everytime you call Add(string) it also outputs the number result of the calculation in a new line to the terminal or console. (remember to try and do this test first!)

---
### Notes:
- Install pytest-mock to run: ```pip install pytest-mock```