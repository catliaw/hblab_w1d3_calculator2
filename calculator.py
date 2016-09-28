"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator_interface():
	"""Prefix based calculator interface.
	Function potentiality for +, -, *, /, square, cube, pow, mod, q (quit).
	Maximum of 2 integer arguments taken by functions."""

	while True:
		user_input = raw_input("")
		tokens = user_input.split(" ")

		if tokens[0] == "q":
			break 
		elif tokens[0] == "+":
			num1 = int(tokens[1])
			num2 = int(tokens[2])
			total = add(num1, num2)
			print total
		elif tokens[0] == "-":
			num1 = int(tokens[1])
			num2 = int(tokens[2])
			total = subtract(num1, num2)
			print total

calculator_interface()