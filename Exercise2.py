'''
Exercise 2: Generator for Extracting Numbers from Text
In this exercise, you will create a generator function that extracts numbers from a given text and calculates their total sum. 
The numbers in the text are in the format of floating-point numbers with two decimal places (e.g., 1000.01, 27.45, 324.00).
'''


import re
from typing import Callable

def generator_numbers(text: str): #The function takes a string of text as input, uses a regular expression to find all occurrences of numbers in the specified format, and yields each number as a float.
    pattern = r'(?<!\S)\d+\.\d{2}(?!\S)'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable): #The function takes a string of text and a generator function as input, calls the generator function to extract numbers from the text, and returns the total sum of those numbers.
    return sum(func(text))


text = "The company made a profit of 1000.01 dollars as main income, enriched additional 27.45 dollars and 324.00 dollars"
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")       



    