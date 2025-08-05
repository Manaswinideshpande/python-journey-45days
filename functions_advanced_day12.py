#What is the purpose of the map() function in Python?
# Ans: To apply a function to each element of an iterable

#Which of the following functions is NOT a part of the functools module?
#Ans:-map  and filter are not the part of functools module

#What does the filter() function do?
#Ans:- Filters elements from an iterable based on a condition (function returns True)

#4. In Python, what is the purpose of the reduce() function?
 #Ans:-) To apply a function to pairs of elements in an iterable until it's reduced to a single value

#5.Coding exercises:
"""
Q:_Write a Python function square_all(numbers) that takes a list of numbers as input
and returns a new list containing the square of each number in the input list.
Use the map() function with a lambda function to implement this.
"""
def square():
    a = int(input("Enter the number: "))
    return a * a
print(square())

 #or 
def square_all(numbers):
    return list(map(lambda x: x * x, numbers))
print(square_all([5]))


"""
Q:_Write a Python function filter_positive(numbers) that takes a list of numbers as
input and returns a new list containing only the positive numbers from the
input list. Use the filter() function with a lambda function to implement this.
"""
a=[1,2,3,4,5,5,-2,-3,-4,5,6]
result = list(filter(lambda x: x>0,a))
print(result)

"""
Q:_Write a Python function calculate_factorial(n) that calculates the factorial of a
given number n . Use the reduce() function with an appropriate lambda
function to implement this.
"""
#method-1
import math

print(math.factorial(5)) 
#method2
def factorial(n):
    factorial = 1  
    for i in range(1, n + 1):
        factorial *= i  
    return factorial  

n = int(input("Enter an integer: "))
print("Factorial of", n, "is", factorial(n))
#method3

from functools import reduce

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

factorial_of_5 = calculate_factorial(5)
print(factorial_of_5)  


"""
Write a Python function count_vowels(string) that takes a string as input and
returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce()
function with an appropriate lambda function to implement this.
"""
from functools import reduce

vowels = "aeiouAEIOU"
string = input("Enter a string: ")

count_vowels = lambda s: reduce(lambda acc, ch: acc + (1 if ch in vowels else 0), s, 0)

print("Number of vowels:", count_vowels(string))    