def add(num_list):
	"""Takes integers and returns the sum of the inputs."""
	for ind, item in enumerate(num_list):
		if ind != 0:
			num_list[ind] = int(item)
			int_num_list = num_list[1:]
			total = sum(int_num_list)
			print total
			return total
listy = ["+", 1, 2, 3, 4, 5]
add(listy)

def subtract(num_list):
	"""Takes integers and returns the result of subtracting in sequence from left to right."""
	for ind, item in enumerate(num_list):
		if ind != 0:
			num_list[ind] = int(item)
			int_num_list = num_list[1:]
			total = None
			for num in int_num_list:
				if total == None:
					total = num
				else:
					total = total - num
			print total
			return total
listy = ["+", 10, 5, 4, 3, 1]
subtract(listy)


def multiply(num_list):
	"""Takes integers and returns the product of the inputs."""
	for ind, item in enumerate(num_list):
		if ind != 0:
			num_list[ind] = int(item)
			int_num_list = num_list[1:]
			total = None
			for num in int_num_list:
				if total == None:
					total = num
				else:
					total = total * num
			print total
			return total
listy = ["*", 10, 5, 4, 3, 1]
multiply(listy)

# def divide(num_list):
# 	"""Takes 2 integers, divides the first input by the second, returning a floating point number."""
# 	return float(num1) / num2

# def square(num_list):
#     """Takes 1 integer and returns the square of that integer."""
#     return num1 ** 2

# def cube(num_list):
#     """Takes 1 integer and returns the cube of that integer."""
#     return num1 ** 3

# def power(num_list):
#    	"""Takes 2 integers and returns the result of raising the first integer to the power of the second integer."""
#    	return num1 ** num2

# def mod(num_list):
#     """Takes 2 integers and returns the remainder when the first input is divided by the second input."""
#     return num1 % num2
