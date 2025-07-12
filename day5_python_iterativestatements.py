##Question 1: What is the purpose of the for loop in Python?
#ANS:-To check a condition and execute a block of code if it's true.

#Question 2: How do you iterate over a range of numbers in a for loop?
# ANS:Using the range() function.
 
#3Q#Question 3: When does a while loop stop executing?
#Ans:-) When the loop condition becomes false

#Question 4: What does the while loop syntax look like in Python?
##Ans:-while condition.

##Coding Exercise:
"""
Exercise 1: Sum of Squares
Write a Python program that calculates and prints the sum of the squares of
numbers from 1 to 5 using a 
for loop.

"""
#1ANS:
sum =0
for num in range(1,6):
    sum= sum+num**2
    print(sum)
    
""" 
 Exercise 2: Countdown
Write a Python program that uses a 
while loop to print a countdown from 5 to 1.   
"""
#2ANS:-
count =1
while count<=5:
    count = count+1
    print(count)
    
"""
  Exercise 3: Multiplication Table with Nested For Loop
Write a Python program to print the multiplication table for a user-specified
number using a nested for loop.
"""
#3Ans:-
multi_count = int(input("enter the value"))
count_1 =0
while count_1 <=11:
    result = count_1*multi_count

    print(f'{multi_count}*{count_1}= {result}')
    count_1 = count_1+1
    
#Exercise 4:
"""
Write a Python program that uses a "for" loop to find the sum of all even
numbers between 0 and 10 (inclusive).
"""
#Ans:-
num = 0
for i in range(0, 11):
    if i % 2 == 0:
       num = num+i
print("Sum of even numbers between 0 and 10 inclusive is:", num)
       
  
#Exercise 5: Calculate the sum of all numbers from 1 to a given number
#3Ans:_
n= int(input('enter the number:'))
sum = 0
for i in range(1,n+1):
     sum  = sum+i
print(sum)
     
     
#Exercise 6:Display numbers from a list using loop
#Ans:-

for i in range(0,11) :
    print(i)
    
#Exercise 7:Display numbers from -10 to -1 using for loop
#for i in range(-1,-11,-1):
    #print(i)
    
for i in range(-10,0):
    print(i) 
    
    
##Exercise 8:Write a Python program to print the cube of all numbers from 1 to a given number
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i**3)
  