#Question 1:What is the output of the following code?
#my_dict = {'a': 1, 'b': 2, 'c': 3}
#print(len(my_dict))
#Ans:-3

#Question 2:Which method is used to add a new key-value pair to a dictionary?
# update() method is used to add a new key-value pair to a dictionary
my_dict = {}
my_dict["key"] = "value"
print(my_dict)


##Question 3:
"""
Consider the following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Tadepalligudem'}
How can you access the value associated with the key 'age'?
"""
my_dict = {'name': 'python', 'age': 30, 'city': 'Tadepalligudem'}
print(my_dict.get('age'))


##Question 4:What happens if you try to access a key that doesn't exist in a dictionary using square brackets notation?
#Ans:- ) It raises a KeyError

#Question 5:Which of the following methods returns a list of all the keys in a dictionary?
# Ans:_keys()

#Task 1: Dictionary Update
"""
Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
# Your code here
# Output should be: {'name': 'python', 'age': 25, 'city': 'west godavari'}
"""
my_dict = {'name': 'python', 'age': 25}
print(len(my_dict))
my_dict["city"] ="west godavari"
print(my_dict)
print(len(my_dict))


#Task 2: Dictionary Access
"""
Write Python code to access and print the value associated with the key 'price' in
the following dictionary:
Dictionary Quiz: 3
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
"""
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
result= product_info['price']
print(result)

"""
#Task 3: Dictionary Removal
Write Python code to remove the key-value pair with the key 'city' from the
following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Your code here
# Output should be: {'name': 'John', 'age': 30}
"""
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop('city')
print(my_dict)


#Task 4: Dictionary Keys
"""
Write Python code to print all the keys present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# Your code here
# Output should be: ['name', 'age', 'city']
"""
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
result_2 = my_dict.keys()
print(result_2)

#Task 5: Dictionary Values;Write Python code to print all the values present in the following dictionary:Dictionary Quiz: 4
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
result4 = my_dict.values()
print(result4)
# Your code here
# Output should be: ['python', 25, 'tanuku']



#Exercise 1: Dictionary Update
#Write a Python script that updates a dictionary with a new key-value pair
dict1 = {'course_name': 'python', 'age': 25, 'city':'Rajahmundry'}
dict1.update({'student_name':'manu','qualification':'postgraduate'})
print(dict1)

#Exercise 2: Dictionary Access
"""
Write a Python script that accesses and prints the value associated with a specific
key in a dictionary
"""

dic_5 = {
    'Fruit' : 'orange',
    'Tree'  : 'orange tree',
    'family':'Rutaceae',
    'genus ': 'Citrus',
'scientific_name': 'Citrus sinensis',
}
print(dic_5)
print(dic_5.get('family'))

#Exercise 3: Dictionary Removal; Write a Python script that removes a key-value pair from a dictionary

dic_5 = {
    'Fruit' : 'orange',
    'Tree'  : 'orange tree',
    'family':'Rutaceae',
    'genus ': 'Citrus',
'scientific_name': 'Citrus sinensis',
} 

print(dic_5.pop('Tree'))
print(dic_5)

#Exercise 4: Dictionary Keys ; Write a Python script that prints all the keys present in a dictionary.

print(dic_5.keys())

#Exercise 5: Dictionary Values Write a Python script that prints all the values present in a dictionary
print(dic_5.values())