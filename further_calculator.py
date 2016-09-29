"""
calculator.py

Using our further_arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from further_arithmetic import *


# Your code goes here
def calculator_interface():
    """Prefix based calculator interface.
    Function potentiality for +, -, *, /, square, cube, pow, mod, q (quit).
    Besides square and cube functions, functions can take any number of integer arguments."""

    while True:
        try:
            user_input = raw_input("")
            tokens = user_input.split(" ")
            if tokens[0] == "q":
                break 
            if len(tokens) >= 3 and (tokens[0] == "square" or tokens[0] == "cube"):
                print "Too many integers entered. Please try again."
            elif len(tokens) < 3 and (tokens[0] == "+" or tokens[0] == "-" or tokens[0] == "*" or tokens[0] == "/" or tokens[0] == "pow" or tokens[0] == "mod"):
                print "Too few integers entered, please try again."  
            elif len(tokens) == 2:
                num1 = int(tokens[1])
                if tokens[0] == "square":
                    total = square(num1)
                    print total
                elif tokens[0] == "cube":
                    total = cube(num1)
                    print total
            elif len(tokens) >= 3:
                if tokens[0] == "+":
                    for ind, item in enumerate(tokens):
                        if ind != 0:
                            tokens[ind] = int(item)
                            int_num_list = tokens[1:]
                            total = add(int_num_list)
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


#       for ind, item in enumerate(tokens):
#           if ind != 0:
#             num_list[ind] = int(item)
#             int_num_list = num_list[1:]
#             total = sum(int_num_list)
#             print total
#             return total

            
            
            else:
                print "[ELSE] I do not understand that command. Please try again!"
        except IndexError:
            print "[EXCEPT] I do not understand that command. Please try again!"

calculator_interface()