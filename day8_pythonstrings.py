#Question 1:What is the main characteristic of Python strings?
#Ans:- ) the main characteristic of Python strings is that they are Immutable

#Question 2: How can you access the last character of a string in Python?
#Ans:-) my_string[-1]

##Question 3: Which method is used to convert a string to uppercase in Python?
#Ans:-string.upper()

#Question 4: What does the split() method do?
#Ans:- Splits a string into a list of substrings

#Question 5:Quiz Questions: Which method is used to check if a string starts with a specific prefix?
##Ans:-startswith()

#Coding Exercise :
"""
Problem:
You are given a string sentence . Print the characters at even indices.
Example:
sentence = "Python is amazing"
# Output: "Pto saaig"
"""
#Ans:-
sentence = "Python is amazing"
result = sentence[::2]  
print(result)     #Pto saaig


#Problem:
"""
You are given a string s.Replace all spaces in the string with underscores ( _ )
and print the modified string.
Example:
s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"
"""

#Ans:-
s = "Python is fun and powerful"
result1 =s.replace(" ",'_')
print(result1)


#Problem:
"""
You are given a string s . Check if the string contains only digits.
Example:
s = "12345"
"""
#ans:-
s = "12345"
check_string = s.isdigit()
print(check_string)

#Problem:
"""
You are given a string s . Print the string in reverse order.Example:
Quiz Questions: 3
s = "Python is amazing"
# Output: "gnizama si nohtyP
"""
#Ans:-
s = "Python is amazing"
result3 = s[::-1]
print(result3)

##Problem:
"""
You are given a string s . Capitalize the first letter of each word in the string
and print the modified string.
Example:
s = "python programming is fun"
# Output: "Python Programming Is Fun
"""
s = "python programming is fun" 

#method1
#for word in s:
    #if s.split(","):
      ## result4 = word.capitalize()
    #print(result4)
    
#method2

sentence = "python programming is fun"
result_5 = sentence.title()
print(result_5)
        