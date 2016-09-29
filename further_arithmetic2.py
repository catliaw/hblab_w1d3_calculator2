def add(int_num_list):
    """Takes integers and returns the sum of the inputs."""
    total = sum(int_num_list)
    return total

def subtract(int_num_list):
    """Takes integers and returns the result of subtracting in sequence from left to right."""
    total = None
    for num in int_num_list:
        if total == None:
            total = num
        else:
            total = total - num
    return total


def multiply(int_num_list):
    """Takes integers and returns the product of the inputs."""
    total = None
    for num in int_num_list:
        if total == None:
            total = num
        else:
            total = total * num
    return total

def divide(int_num_list):
    """Takes integers, divides the first input by the second, returning a floating point number."""
    total = None
    for num in int_num_list:
        if total == None:
            total = num
        else:
            total = total / num
    return total

def square(num1):
    """Takes 1 integer and returns the square of that integer."""
    return num1 ** 2

def cube(int_num_list):
    """Takes 1 integer and returns the cube of that integer."""
    return num1 ** 3

def power(int_num_list):
    """Takes 2 integers and returns the result of raising the first integer to the power of the second integer."""
    for ind, item in enumerate(int_num_list):
        if ind != 0:
            num_list[ind] = int(item)
            int_num_list = num_list[1:]
            total = None
            for num in int_num_list:
                if total == None:
                    total = num
                else:
                    total = total ** num
            return total

def mod(int_num_list):
    """Takes 2 integers and returns the remainder when the first input is divided by the second input."""
    for ind, item in enumerate(int_num_list):
        if ind != 0:
            num_list[ind] = int(item)
            int_num_list = num_list[1:]
            total = None
            for num in int_num_list:
                if total == None:
                    total = num
                else:
                    total = total % num
            print total
            return total
listy = ["mod", 5, 4, 3]
mod(listy)