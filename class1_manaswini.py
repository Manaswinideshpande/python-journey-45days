### 1Q:-Create a Python script with both single-line and multi-line comments explaining the purpose of the script.
# Ans:- Purpose of Script: the main purpose of script is to explain the code Steps, or explain the purpose of task which we are performing, it is also used to Write the Aim of the project, Object and conclusion of the project steps involved in the project.
# Script can be of two types based on its length and purpose. 
#1. single line script, denoted by # symbol which means comment in python .eg: ##Welcome to fundamentals of python by python life
#2. multiline script,denoted by triple quoted string :eg:"""so far we have studied the basic fundamental definitions of python, now we are going to learn a brief introduction to python Data types and how to use them in python coding/""""

# 2Q#Declare two variables, one storing an integer and the other a string. Print their values.
product_cost= 10
procuct_name = ' pencil'
print(product_cost,procuct_name)

#3Q#Write a program that prints a pattern using multiple print statements.
print('         *')
print('       ***')
print('     *****')
print('   *******')
print(' *********')

#4Q# Create a Python script for a simple task and add comments to explain each step


fruit_name = 'orange' # here variable  fruitname is  holding a string  named orange fruit 
tree_name  ="orange tree" # here variable  treename is  holding a string  named orange fruit
number_of_fruits = 20 # here  variable number of fruits is holding the int datatype
print(f'fruit name is {fruit_name} and it came from {tree_name} and it contains{number_of_fruits}')

#5Q ##Create variables of different data types(int,float,str) and print their values.
int_datatype = 90
float_datatype = 9.0
string_datatype = "Hello python world"
print(int_datatype,float_datatype,string_datatype)

##6Q#Determine the data type of a variable.
print(f"the data type of above variables is:'{type(int_datatype)},{type(float_datatype)},{type(string_datatype)}")

#7Q#Display the memory addresses
# The memory addresses of x and y 
employee_id = 10
person_age = 10
print(f'The memory adress of:id(employee_id ), id(person_age)')


#8Q#Create a program that takes user age = “35”, converts it to an integer,and then prints the result type.
user_age ="35"
age =int(user_age)
print(age)
print(type(age))

#9Q## Concatenate two strings and print the result
user_1 = "Welcome to "
user_2 = "Python life"
result =user_1 + user_2
print(result)