# ============================================
# PYTHON FUNCTIONS - PARAMETERS & ARGUMENTS
# ============================================


# 1. BASIC FUNCTION
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))


# ============================================
# 2. DEFAULT PARAMETERS
# ============================================
def greet_with_default(name, message="Good Morning"):
    return f"{message}, {name}!"

print(greet_with_default("Bob"))
print(greet_with_default("Bob", "Good Night"))


# ============================================
# 3. KEYWORD ARGUMENTS
# ============================================
def student_info(name, age, grade):
    return f"Name: {name}, Age: {age}, Grade: {grade}"

print(student_info(age=20, grade="A", name="Charlie"))


# ============================================
# 4. *ARGS - MULTIPLE POSITIONAL ARGUMENTS
# ============================================
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))
print(add_numbers(10, 20, 30, 40, 50))


# ============================================
# 5. **KWARGS - MULTIPLE KEYWORD ARGUMENTS
# ============================================
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="David", city="Delhi", country="India")


# ============================================
# 6. POSITIONAL-ONLY PARAMETERS (/)
# ============================================
def multiply(a, b, /):
    return a * b

print(multiply(4, 5))


# ============================================
# 7. KEYWORD-ONLY PARAMETERS (*)
# ============================================
def divide(*, a, b):
    return a / b

print(divide(a=10, b=2))


# ============================================
# 8. LAMBDA FUNCTION (ANONYMOUS FUNCTION)
# ============================================
square = lambda x: x ** 2
print(square(6))

add = lambda x, y: x + y
print(add(3, 7))


# ============================================
# 9. RECURSIVE FUNCTION
# ============================================
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# ============================================
# 10. HIGHER ORDER FUNCTION
# ============================================
def apply(func, value):
    return func(value)

print(apply(square, 9))


# ============================================
# 11. MAP, FILTER, REDUCE
# ============================================
from functools import reduce

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

total = reduce(lambda x, y: x + y, numbers)
print(total)


# ============================================
# 12. NESTED FUNCTION
# ============================================
def outer(name):
    def inner(greeting):
        return f"{greeting}, {name}!"
    return inner("Welcome")

print(outer("Eve"))


# ============================================
# 13. DECORATOR FUNCTION
# ============================================
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


# ============================================
# 14. GENERATOR FUNCTION
# ============================================
def count_up(n):
    for i in range(1, n + 1):
        yield i

for num in count_up(5):
    print(num, end=" ")
print()


# ============================================
# 15. TYPE HINTED FUNCTION
# ============================================
def add(a: int, b: int) -> int:
    return a + b

print(add(8, 12))
