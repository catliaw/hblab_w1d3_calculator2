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
		try:
			user_input = raw_input("")
			tokens = user_input.split(" ")
			if tokens[0] == "q":
				break 
			if len(tokens) >= 3 and (tokens[0] == "square" or tokens[0] == "cube"):
				print "Too many integers entered. Please try again."
			elif len(tokens) > 3:
				print "Too many integers entered. Please try again."
			elif len(tokens) < 3 and (tokens[0] == "+" or tokens[0] == "-" or tokens[0] == "*" or tokens[0] == "/" or tokens[0] == "pow" or tokens[0] == "mod"):
				print "Too few integers entered, please try again."  
			elif len(tokens) == 3:
				num1 = int(tokens[1])
				num2 = int(tokens[2])
				if tokens[0] == "+":
					total = add(num1, num2)
					print total
				elif tokens[0] == "-":
					total = subtract(num1, num2)
					print total
				elif tokens[0] == "*":
					total = multiply(num1, num2)
					print total
				elif tokens[0] == "/":
					if num2 == 0:
						print "Dividing by 0 results in undefined error. Please try again."
					else:
						total = divide(num1, num2)
						print total
				elif tokens[0] == "pow":
					total = power(num1, num2)
					print total
				elif tokens[0] == "mod":
					total = mod(num1, num2)
					print total
			elif len(tokens) == 2:
				num1 = int(tokens[1])
				if tokens[0] == "square":
					total = square(num1)
					print total
				elif tokens[0] == "cube":
					total = cube(num1)
					print total
			else:
				print "[ELSE] I do not understand that command. Please try again!"
		except IndexError:
			print "[EXCEPT] I do not understand that command. Please try again!"

calculator_interface()