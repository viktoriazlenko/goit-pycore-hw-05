'''
Exercise 1: Caching Fibonacci
In this exercise, the caching mechanism for the Fibonacci function to optimize its performance has been implemented.
'''

def caching_fibonacci():
    cache = {}

    def fibonacci(n): #The function takes an integer n as input, checks if the Fibonacci number for n is already in the cache, and if not, calculates it recursively while storing previously computed values in the cache to avoid redundant calculations. The function returns the Fibonacci number for n.
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()

# Testing the caching Fibonacci function
print(fib(10))  # 55
print(fib(15))  # 610