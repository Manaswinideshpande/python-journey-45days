    ##Quiz:
1. ##1Q3 Indentation is crucial in Python to
#ans:-D. Define the scope of a code block
#2Q# 2. What will be the output of the following code?
x = 10
if x > 5: 
    print("Greater than 5")
else: 
    print("5 or less")
    
#ans:A.Greater than 5
#3Q# 3. In the if-elif-else statement, how many conditions can be checked?
#ans:-C.In the if-elif-else statement,multiple conditions are checked

#4Q#4. What is the purpose of the else statement in Python
#ans:-B. To provide an alternative block of code when the if condition is false

#5Q#5. Which of the following statements is true about a nested if statement?
#3sns:- B. It allows for more complex conditional logic

#Exercises:

"""1Q.Vowel Checker:
Write a Python program that takes a character as input and checks whether
it is a vowel or not. Use the 
if-else statement.
"""
vowel_check = ('a','e','i','o','u')
word =input('enter the text')
if 'a' in word or 'e' in word or 'i' in word or  'o' in word or 'u' in word  :
    print("The given word contains vowel")
    
else:
    print("The given word does not contains vowel")


##2Q#Age Group Classification;Write a program that takes an age as input and classifies the person into ne of the following age groups:
#Child: 0-12 years
#Teenager: 13-17 years
#Adult: 18-64 years
#Senior: 65 years and older
age = int(input("enter your age:"))
if age >0 and age<=12:
    print(f'the age of person is {age}, person is  a child.')
elif age>12 and age<=17:
    print(f'the age of person is {age}, person is  a teenager.')
elif age>17 and age<=64:
    print((f'the age of person is {age}, person is  an Adult.'))
elif age>=65:
     print(f'the age of person is {age}, person is  an old.')
else: 
 print('no input given')
 
 ##3Q#3. Number Classifier: Write a program that takes an integer as input and classifies it as positive,negative, or zero. Use the if-elif-else statement.
num = int(input('enter the number'))   
if num ==0:
     print('number is zero')   
elif num >=1: 
     print('number is positive')
else:
     print('number is negative')    
     
##4Q#4.Leap Year Checker:Create a program that checks whether a given year is a leap year or not. A leap year is divisible by 4, but not by 100 unless it is divisible by 400.
year_  = int(input('enter the year'))           
if year_ % 4  == 0:
    if year_ %100 != 0 :
        print('the year is  not a leap year')
    elif year_ %400  == 0:
        print('the year is leap year')
    else:
        print('the year is not  leap year')
else:
     print("The year is not a leap year.")
    
            
  ##5Q# Calculator:Build a simple calculator program that takes two numbers and an operator(+, -, *, /) as input and performs the corresponding operation.  

num1 = int(input('enter the number value:'))
num2 = int(input('enter the number value:'))
operation = input('enter the operation(+,-,*,/,//,%):')
if operation == '+':
    print('addition of numbers',num1 + num2)
elif operation == '-':
    print('substraction of numbers',num1 - num2)
elif operation =='*':
    print('Multiplication of numbers',num1 * num2)
elif operation =='/':
    print('divisionof numbers',num1/num2)
elif operation == '//':
    print('floor division',num1//num2)
elif operation =='%':
    print('modulus of numbers',num1%num2)
else:
    print('no operation performed')

##6Q#Short Hand If:Rewrite the following code using the short-hand 
#if statement:
#Quiz Questions: 3
#x = 8
#if x % 2 == 0: result = "Even"
#else: result = "Odd"
result=int(input("enter the value:"))
print('even') if result % 2 ==0 else print('odd') 

##7Q## Discount Calculator:
"""
 Create a program that calculates the final price after applying a discount.
The program should take the original price and the discount percentage as
input.
"""

original_price =int(input('enter the original rate:'))
discount_percent = int(input('enter the discount percent:'))
final_price  = original_price*(1-discount_percent/100)
print(final_price)


###8. BMI Calculator:
""" 
Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input
"""
weight_ = int(input('enter the weight'))
height_ = int(input('enter the value'))
bmi_ = (weight_/ height_**2)
print(bmi_)

