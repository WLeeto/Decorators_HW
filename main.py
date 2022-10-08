from utils import path, logger_decorator


@logger_decorator
def exponentiation(a, b):
    return a ** b


path_new_file = path("new_file.txt")


@path_new_file
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    exponentiation(3, 3)
    multiply(3, 3)









