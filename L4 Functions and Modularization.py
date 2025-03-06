# maths function f(x) = 2x + 1, g(x) = x^2

# Functions
# input (domain) f(x) = 2x + 1 output(range)
# f(3) = 2*3 + 1 = 7

# Defination of a function
# is that it takes an input, does something to that input, and then produces an output
# the input is not nescassary number it can be anything like string, list, tuple, dict, set

# Function is a block of code which only runs when it is called

# f(x) = 2x^2 + 3x + 1
def f(x):
    return 2*x**2 + 3*x + 1

# quadratic formula x_1, x_2 = (-b +- sqrt(b^2 - 4ac)) / 2a
def quadratic_formula(a: float, b, c):
    x_1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x_2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return (x_1, x_2)

def foo(x: int, y: str) -> None:
    for i in range(x):
        print(y[i])

def twoSum(nums: list[int], target: int) -> None:
        length: int = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                print(f"i: {i}, j: {j} nums[i]: {nums[i]}, nums[j]: {nums[j]} nums[i] + nums[j]: {nums[i] + nums[j]}")
                if nums[i] + nums[j] == target:
                    return [i, j]
            print(" ")

def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0: # n divides i and remainder is 0 therefore n is not prime
            return False
        else:
            return True

# main function
if __name__ == "__main__": # main function  is the entry point of the program
    # print(f(3))
    # print(f(f(4)))
    # print(quadratic_formula(1, 3, 1)) # (x_1, x_2) = (-1, -2)

    # foo(5, "Hello World")

    # x: str = "Hello" # x = ['H', 'e', 'l', 'l', 'o']
    # print(x[2])

    # print(twoSum([2, 7, 11, 15], 18)) # [0, 1] 2 + 7 = 9

    print(isPrime(12345678901234567)) # True