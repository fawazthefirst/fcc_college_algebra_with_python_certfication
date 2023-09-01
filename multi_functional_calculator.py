# Write your code here
import math
from sympy import symbols, solve

# PROJECT PART A - Define all functions (including "Menu" function) for use later

# 0. MENU FUNCTION
def main_menu():
    print("Main Menu")
    print("1. Add, Subtract, Multiply, Divide")
    print("2. Detect prime numbers")
    print("3. Generate prime factors of a number")
    print("4. Simplify square roots")
    print("5. Solve for a variable")
    print("6. Exit")


# 1. ARITHMETIC FUNCTION
def arithmetic(a, b, operator):
    if operator == '+':
      result = a+b
    elif operator == '-':
      result = a-b
    elif operator == '*':
      result = a*b
    elif operator == '/':
        if b != 0:
            result = a/b
        else:
            result = 'Division by Zero is NOT allowed!'
    else:
        result = 'Invalid operator!'
    return result

# 2. PRIME NUMBERS FUNCTION
def prime_numbers(number):
    prime_or_composite = 'prime'
    sqrt = math.floor(math.sqrt(number))+1
    if number <= 1:
        return 'Neither prime nor composite'
    for x in range(2, sqrt):
        if number % x == 0:
            prime_or_composite = 'composite'
            break
    return prime_or_composite

# 3. PRIME FACTORS FUNCTION
def prime_factors(number):
    factors = []
    x = 2
    while (x * x) <= number:
        if number % x == 0:
            factors.append(x)
            number //= x
        else:
            x += 1
    if number > 1:
        factors.append(number)
    return factors

# 4. SIMPLIFY SQUARE ROOT FUNCTION
def simplify_sqrt(n):
    upper_limit = math.floor(math.sqrt(n)) + 1
    max_factor = 1
    for factor in range(1, upper_limit):
        if n % (factor**2) == 0:
            max_factor = factor**2
    other_factor = n // max_factor
    square_root = int(math.sqrt(max_factor))
    other_factor = int(other_factor)
    output = square_root * sympy.sqrt(other_factor)
    return output

# 5. SOLVE FOR X FUNCTION
def unknown_solver():
    x = symbols('x')
    eq = input('Enter an equation to solve for x: 0 = ')
    solutions = solve(eq, x)
    if solutions:
        print(f'Total solutions: {len(solutions)}')
        for index, sol in enumerate(solutions):
            print(f'x{index+1} = {sol}')
    else:
        print('No solutions found.')

# PART B - Call functions inside a while-loop to improve readability and modularity
while True:
    main_menu()
    choice = input("Enter the number of your choice (1-6): ")
    if choice == "1":
        print("Selected: Add, Subtract, Multiply, Divide")
        first_num = int(input('Enter first number: '))
        op = input("Enter operator ('+', '-', '*', '/')")
        second_num = int(input('Enter second number: '))
        try:
            result = arithmetic(first_num, second_num, op)
            print(f"{first_num} {op} {second_num} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        print("Selected: Detect prime numbers")
        digit = int(input('Enter a positive number: '))
        result = prime_numbers(digit)
        print(result)
    elif choice == "3":
        print("Selected: Generate prime factors of a number")
        num = int(input("Enter a number: "))
        factors = prime_factors(num)
        print(f"Prime factors of {num}: {factors}")
    elif choice == "4":
        print("Selected: Simplify square roots")
        number = int(input('Without the radical, enter a square root to factor: '))
        result = simplify_sqrt(number)
        print(f"Simplified square root: {result}")
    elif choice == "5":
        print("Selected: Solve for a variable")
        unknown_solver()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")