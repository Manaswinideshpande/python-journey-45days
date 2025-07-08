###1Q# Print Statement:
##Write a Python program that prints your name
Name = 'Manaswini Deshpande'
print(Name)

##2Q#Comments:Create a Python script with both single-line and multi-line comments
##explaining the purpose of the script.
list_1 = [1,2,3,4,5]
#here we are assigning  a sequence of elements to a variable named list1  
print(list_1)
""" 
Print function is used to print the list_1 as output which displays
all the elements in list_1 as output here list_1 is a datatype
which holds integers as elements in square brackets
"""
###3Q. Data Structures & Data Types:
##a.Define a list containing three different data types.
##b.Define a set containing employee id’s.
#3ans: Data types defines a kind of value a variable holds(such as data types= int,string, float, complex_numbers)
# while data structures organize and store the collection of datatypes.like lists,tuple,strings,dictionaries,sets,boolean.
list_data_types=[1,2,3,4,5.6,7.8,9.0,"ramu","ravi"]
print(list_data_types)
print(type(list_data_types))

set1={"3629Id","6748Id","53678Id","75424Id"}
print(set1)
print(type(set1))

###4Q# String Operations:Concatenate two strings and print the result.
#Repeat a string three times and display the output
Strin_name= "Welcome to Hello python life"
String_numbr = " 35th batch"
print(Strin_name + String_numbr)
result = Strin_name + String_numbr
print(result)
print(result)
print(result)

##5Q#. Python Keywords:Create a variable with a name that is a Python keyword. What happens?observation..
#if = 5
#print(if) # observation: it throughs syntax error,since the keywords of python cannot ne used as a variable according to python

##.6Q## Python Variables:Declare two variables, one storing an integer and the other a string.Print their values

var_1 ="India has got its rank as"
var_2 = 4
print(var_1,var_2)

##7Q#Type Conversions:Convert a float to an integer and print the result.
#Convert an integer to a string and display the output.
float_value =9.9
print(float_value)
print(type(float_value))
convertion_value =int(float_value)
print(convertion_value)
print(type(convertion_value))

int_value =365
print(type(int_value))
str1 = str(int_value)
print(str1)
print(type(str1))


### EXERCISE
##1QPrint Statement:Write a program that prints a pattern using multiple print statements.
print('*****##*****' )
print('*****###*****' )
print('*****####*****')
print( '*****#####*****' )
print( '*****######***** ')

##2Q#Comments:Create a Python script for a simple task and add comments to explain each step.
employee_id = 354786 # here employee variable is holding an integer  datatype
employee_name = "ramu"# here variable  holds the string 
employee_salary =150000 # here an int value as salary is given to the employee_salary  object/variable
employee_status = "working in lic"# here employee variable holds the string 
print(f"Here is an employee named {employee_name } andhis ID is {employee_id} his salary is {employee_salary} he is {employee_status}") # this will print the whole employee details as output


###3Q# Data Structures & Data Types:Implement a program that uses a dictionary to store information about a book (title, author, publication year).
dict1 = {'Title':'The things you can see only when you slow down','author':'Haemin sunim','Publication year':2017}
print(dict1)

##4Q#String Operations:Write a python program that takes a string as input ( 35 ) and return float value.
price = input("enter the age:")
print(type(price))
result1=float(price)
print(type(result1))

##5Q## Concatenate Strings: Write a program to take two names as input and print them together.
name1= "Stars in the sky"
name2 ="  shines when their time comes"
print(name1 + name2)

###6Q#Type Conversions:Create a program that takes user input for their age, converts it to an integer, adds 5, and then prints the result
user_age = int(input("enter the value:"))
print(type(user_age))
final_result = user_age + 5
print(final_result)

###7Q## Simple Input & Output:Build a calculator program that takes two numbers as input and performs the arithmetic operation.
num1 = int(input("enter the value:"))
num2 = int(input("enter the value:"))
substraction_value = num1 - num2
print('substraction_value',substraction_value)
addition_value = num1+num2
print('addition_value',addition_value)
multi_value   =  num1*num2
print('multi_value',multi_value )
div_value = num1/num2
print('div_value',div_value)
floor_div_value =num1//num2
print('floor_div_value',floor_div_value)
mod_value = num1%num2 
print('mod_value', mod_value )
