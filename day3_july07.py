
###TASK.DAY3.Operators
##1Question 1:What is the value of result in the following code 
x = 15
y = 4
result = x // y
print(result)# ans =option.b that is 3

##2Q#:-What is the output of the following code?
1 # ans = optionb. that is 1
a = 7
b = 3
c = a % b
print(c)

##3Q#:-Question 3:Which assignment operator is equivalent to x = x * 5 
x *= 5 # or
x = x*5 # both are same ,ans is c option ,x *= 5 

##4Q:-Question 4:
# What is the result of the expression 5 < 3 or 2 == 2 ?
"""
 ans:- is option a) True because according to Truth table 
 whenever or logical operator is used then it checks 
 the condition is atleast true for any one of the variable assigned value, 
 here condition is true for 2==2 hence its true (f,t = t)
 """

##5Q:-Question 5:If a = True and b = False , what is the value of not a or b ?
#ans is option b , that is false. because not a means false. here or b which means that b  value is given as false.

##Coding Exercise:

#Exercise 1
"""
1Q Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user.
"""
#ANS;-
length= int(input('enter the value of length:'))
width = int(input('enter the value of width:'))
area = length*width
print(f"The length of a rectangle is{length}, The width of the rectangle is {width}, and the area of the rectangle id {area}")

##Exercise 2:Write a Python program to demonstrate incrementing and decrementing a variable

rice_price= 30
rice_price = rice_price + 1

print(f' rice_price after increasing 1 value is {rice_price}')

#Exercise 3:-
"""
3Q:-Write a Python program to convert temperature from Celsius to Fahrenheit. 
The formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as
input from the user.
"""
#ANS
c = int(input('enter the celcius value:'))
F = (c*9/5)+32
print(F)

#Exercise 4:Write a Python program to calculate the simple interest given the principal amount, rate, and time (in years).
principal_amount = int(input('enter the amount value: '))
rate = int(input('enter the rate value: '))
time_in_years = int(input('enter the year:'))
simple_intrest = (principal_amount*rate*time_in_years) /100
print(simple_intrest)

##Exercise 5:Write a Python program to concatenate two strings and display the result. The strings should be taken as input from the user.
name_1 = input('enter your first name:')
name_2 = input('enter the second name')
name =name_1+name_2
print(name)

##Exercise 6:Write a Python program to convert a distance from kilometers to miles

kilo_metres = int(input("enter the kilometer value: "))

miles_=kilo_metres *0.621371
print(miles_)


####TASK1 
         ##Quiz Questions:
         
         
##Question: What do identity operators ( is and is not ) check in Python?/it defines  whether the two variables locate to the same memory object or not returns boolean 
# ans Identity operators are useful to check the memory storage of the variable.it defines the memory location of the objects 
# for example
arr1 = int(input("enter the  value: "))
arr2= int(input("enter the  value: "))
print(arr1 is arr2)
#if arr1 == arr2 then it returns true else it returns false
#ans:) Memory address identity

##Question: Which of the following statements is correct for the identity operator is ?

#ans:-b) x is y is True if x and y refer to the same object.

#Question: What do membership operators ( in and not in ) check in Python?
 #ans"- Value equality , for example
list_x= [1,2,3,4,5]
result = 3 in list_x
print(result) # returns true since sis present in listx nad viceversa
 

##Question: Which membership operator is used to check if a value is not present in a sequence?
#ans:_ option b) not in is crct answer.

##Q:-Coding Exercise:
"""
1. Exercise: Create a program that takes user input for their name and age.
Use formatted strings (f-strings) to print a message welcoming the user and
stating their age
"""
student_name =input('enter the name')
student_age = int(input('enter the age'))
print(f'Welcome to python classes here is a student name {student_name} age {student_age}')


##Create a list called numbers that contains integers from 1 to 10,
# Quiz Questions: 1.check if the number 5 is in the list.
#2.Check if the number 15 is not in the list.
number_of_mangoes =[1,2,3,4,5,6,7,8,9,10]
count_1 = 5 in number_of_mangoes
print(count_1)
coun_2 = 15 in number_of_mangoes
print(coun_2)

