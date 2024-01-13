"""
    Day 12: Recursion
        Solve a problem using recursion.
        Discuss the concept of recursion and base cases.
"""

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

def power(x,n):
    #Base case: power of 0 is 1
    if n == 0:
        return 1
    else:
        #Recursive case of x^n = x * x^(n-1)
        return x * power(x,n-1)
    
def main():
    # Example: Calculate the factorial of 5
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is {result}")

    # Example: Calculate the power of 5^2
    number = 5
    pow = 2
    result = power(number, pow)
    print(f"The power of {number} to power of {pow} is {result}")

if __name__ == "__main__":
    main()
