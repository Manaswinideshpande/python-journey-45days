##Question 1:
#What is the output of the following code?my_list = [10, 20, 30, 40, 50] print(my_list[1:4])
#Ans: [20, 30, 40]

#Question 2:Which method is used to add multiple elements to the end of a list?
#Ans:- extend() method is used  to add multiple elements to the end of a list.

##Question 3:Consider the following list:fruits = ['apple', 'banana', 'orange']How can you remove 'banana' from the list?
#Ans:- fruits.remove('banana')

# Question 4:What does the len() function return when applied to a list?
#ans:-The number of elements in the list

#Question 5:Which of the following list comprehensions generates a list of even numbers from 0 to 10?
#ans:- [x for x in range(11) if x % 2 == 0]

#Task 1 Coding:
"""
Reverse List:
Write Python code to reverse the order of elements in the given list my_list .
Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]

"""
my_list = [10, 20, 30, 40, 50, 11]
print(my_list )
reverse_list = my_list[::-1]
print(reverse_list )

##Common Elements:Given two lists list1 and list2 , find and print the common elements between them.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3= []
for  i in list1:
    for j in list2:
        if i == j:     
            list3.append(i)
    print('common elements',list3)
    
###Task 3:
"""
Unique Elements:
Create a new list unique_list containing only the unique elements from the
given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
# Output should be: [1, 2, 3, 4, 5]
"""
original_list = [1, 2, 2, 3, 4, 4, 5]
print(list(set(original_list)))

#Task 4:Remove Duplicates:
"""
Remove duplicate elements from the given list duplicated_list and print the list
without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]
"""
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
unique_list =[]
for num in duplicated_list :
    if num not in unique_list:
        unique_list.append(num)
print("unique elements of list after removing duplicates is:",unique_list)   

##Exercise 1: List Concatenation  Write a Python script that concatenates two lists and prints the result.
drug_names= ["Nsaids", "Dolo","atenolol","Aspirin","omeprazole" ]
drug_dosage = [0.5,600,1,2.5,50]
drug_names.extend(drug_dosage)
print(drug_names)

#method2
drug_names= ["Nsaids", "Dolo","atenolol","Aspirin","omeprazole" ]
drug_names.append("metformin")
print(drug_names)

#Exercise 2: List Repetition , 
# Write a Python script that repeats a list three times and prints the result.

list_= [2,4,6,8,9]
new_list = [list_]*3
print(new_list)

#Exercise 3: List Removal; Write a Python script that removes the elements at even indices from a list.
list_1 = [1,2,3,4,5,6,7,89,10,11,12,13,14,15,16]
empty_list =[]
for elements in list_1:
     if elements %2!=0:
         empty_list.append(elements)
print(empty_list)
#removes elements at odd indexes
list_2 = [1,2,3,4,5,6,7,89,10,11,12,13,14,15,16]
empty_list2 =[]
for elements in list_2:
     if elements %2 ==0:
         empty_list2.append(elements)
print(empty_list2)

##Exercise 4: List Insertion; Quiz Questions: 4
# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of  a list

age_list  = [20,25,30,35,60,65]

age_list.insert(0,12)
age_list.insert(0,11)
age_list.insert(0,10)
print(age_list)

#### List Comprehension

#List comprehensions 1. Square Numbers: Create a list of squares of numbers from 1 to 10.
# method 1
for i  in range(1,11):
    result =  i*i
    print( result )
    
    #Method 2 :
square_num = [ i*i for i in range(1,11)]
print(square_num )
    

## 2. Even Numbers: Generate a list of even numbers from 1 to 20.
new_list1 =[]
for i in range(1,21):
    if i % 2 == 0:
         new_list1.append(i)
print(new_list1)

#method2
list4= [i for i in range(1,21) if i%2 !=0]
print(list4)


##3. Words Lengths: Given a list of words, create a list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date"]
length_of_words = [len(words) for i in words ]
print(length_of_words)