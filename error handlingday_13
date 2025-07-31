
#ValueError: since str1 cannot be converted into integer as it is an string object it throws a value error and it can be haadled as follows:
try:
    # code that might raise a ValueError
   str_1= "Hello python"
   print(int(str_1))
except ValueError as e:
    print(f"ValueError: {e}")
    
#TypeError  :- Raised when an operation or function is applied to an object of an inappropriate type):
try:
    # code that might raise a ValueError
   str_1= "Hello python"
   print(int(str))
except TypeError as e:
    print(f"TypeError: {e}")
    
#   FileNotFoundError Raised when a file or directory is requested but cannot be found):
try:
    with open("non_existent_file.txt", "r") as file:
     contents = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
    
#ZeroDivisionError Raised when the second operand of a division or module operation is zero):
try:
    a =10
    b=0
    print(a/b)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
    
#IndexError Raised when a sequence subscript is out of range):
try:
     list1 =[1,2,3,4,5,6,6]
     print(len(list1))
     print(list1[10])
    # code that might raise an IndexError
except IndexError as e:
    print(f"IndexError: {e}")

#KeyError raised when a key is not given in dictionary
try:
    dict1 ={"Key1":"value1","key2":"value2"}
    print(dict1["key3"])
except KeyError as e:
    print(f":KeyError  {e}")
    
    
#AttributeError Raised when an attribute reference or assignment fails):calling a method that does'nt exists
try:
    text = "hello"
    text.append("world")
except AttributeError as e:
    print(f":AttributeError  {e}")
    
