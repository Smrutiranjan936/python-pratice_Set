"""Recursion is a function it cal itself"""
# Factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(7))                 #Output - 5040
print(factorial(5))                 #Output - 120
print(factorial(3))                 #Output - 6
print(factorial(0))                 #Output - 1
print(factorial(1))                 #Output - 1

# Fibonaci sequence
