# def func(str):
#     print("This is:",str)
# func("Akansha")

# def func(str):
#     print(str)
#     func(str)    #RecursionError: maximum recursion depth exceeded while calling a Python object
#     print("This is:",str)
# func("Akansha")



# n!=n*(n-1)*(n-2)*(n-3)....1
# n!=n*(n-1)!
def factorial_iteration(n):
    """parameter n: integer
    return :n*(n-1)*(n-2)*(n-3)....1"""
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def factorial_recursion(n):
    """parameter n: integer
    return :n*(n-1)*(n-2)*(n-3)....1"""
    if n==1:
        return 1
    else:
        fact=n*factorial_recursion(n-1)
        return fact
    #return n*factoraial(n-1)
number=int(input("Enter a number of which you want to find factorial:"))
print("Factorial of a number through iterative approach:",factorial_iteration(number))
print("Factorial of a number through recursive approach:",factorial_recursion(number))


# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# A series of numbers in which each number is the sum of the two preceding numbers.

def fibonacci_recursive(n):
    if n<=0:
        print("Invalid number")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
number=int(input("Enter a number"))
print(fibonacci_recursive(number))





