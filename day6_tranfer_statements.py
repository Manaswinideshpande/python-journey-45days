
##Quiz:1. What does the break statement do?
#3ANS:-b) Exits the loop immediately

##2. When is the continue statement used?
#Ans:-b) To skip the rest of the code for the current iteration and move to the next

##33. What is the purpose of the pass statement?
#Ans:- Acts as a null operation, doing nothing

##Coding Exercise
""":
Problem 1: Using break in a While Loop
Write a Python program that takes a list of numbers as input numbers = [25, 30,
20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds
100, stop adding numbers and print "Sum exceeded 100
"""
#Ans:-
num =[25, 30,20, 40, 15, 25]
index=0
total = 0
while index <len(num):
    total = total+num[index]
    if total >100:
       print("Sum exceeded 100",total)
       break 
    index += 1
    
##Problem 2: Using continue in a For Loop
"""
Write a Python script that uses a for loop to iterate through numbers from 1 to
600. Print only the odd numbers, skipping the even ones using the continue
statement
"""
#Ans:-To print only odd numbers  need to skip even numbers the code is as below to represent /print only odd numbers.

for i in range(1,601):
    if i%2==0:
        continue
    print("odd numbers i",i)
    
#Problem 3: Using pass in Conditional Statements
# Quiz and Coding Exercise 2
#Write a Python script that checks if a number is even or odd. If the number is even, print "Even"; if odd, do nothing (use the pass statement)
    
check_num = int(input('enter the value'))
if check_num %2 == 0:
    print(' given input is even number',check_num)
else:
    pass
print(check_num)
     
##Problem 4: Combining Transfer Statements
"""
Write a Python script that iterates through a list of words. If the word is "break,"
exit the loop using the break statement. If the word is "skip," skip the rest of the
code for the current iteration using the continue statement. For any other word,
print the word   

"""   
#word_list =['apple','orange','pinapple', 'mangoes','custardapple']
####  break
    
   #method 1 1
fruits = ["apple", "banana", "pinapple","grape", "orange", "kiwi"]
for fruit in fruits:
    if fruit  == 'pinapple':
       continue # it prints all the list items except piapple
    print(fruit)
    
students = ["Alice", "Barbie", "Charlie", "David", "Eva"]
for student in students:
    if student == "Barbie":
       break # it breaks the loop at Barbie
    print(student)
 
 
 #method 2
 
list2 = ["apple", "banana", "skip", "grape", "break", "kiwi"]
for i in list2:
    if i == "break":
        break
    elif i == "skip":
        continue
    else:
        print(i)
   