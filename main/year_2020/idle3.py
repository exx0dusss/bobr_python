Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = [1,2,3,4,5]
>>> 7 in my_list
False
>>> 7 in my_list or 7 not in my_list
True
>>> my_list = []
>>> bool(my_list)
False
>>> my_list = [1,2,3,4]
>>> bool(my_list)
True
>>> my_list is True
False
>>> my_list is False
False
>>> len(my_list)
4
>>> bool(0)
False
>>> bool(1)
True
>>> bool(-1)
True
>>> bool((0,0,0,0))
True
>>> str = " ".strip()
>>> 
>>> bool(str)
False
>>> bool(True)
True
>>> x1 = 5
>>> y1 = 5
>>> print
<built-in function print>
>>> print(x1 is y1)
True
>>> my_dict = {id: 273912, "Name", "age": 15}
SyntaxError: invalid syntax
>>> my_dict = {idd: 273912, "Name": "Peter". "age": 15}
SyntaxError: invalid syntax
>>> my_dict = {"idd": 273912, "Name": "Peter", "age": 15}
>>> my_dict
{'idd': 273912, 'Name': 'Peter', 'age': 15}
>>> "Value" in my_dict
False
>>> 15 in my_dict
False
>>> 15 in my_dict.values()
True
>>> 34 in my_dict.values() or 16 in my_dict.values()
False
>>> this_string = "I am batman"
>>> "I am" in my_str
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    "I am" in my_str
NameError: name 'my_str' is not defined
>>> "I am" in this_string
True
>>> "You" in this_string
False
>>> this_string.lower()
'i am batman'
>>> this_string.upper()
'I AM BATMAN'
>>> this_string.strip()
'I am batman'
>>> "I" in this_string
True
>>> strthis = "  I    love mc   donalds"
>>> strthis.strip()
'I    love mc   donalds'
>>> strthis.lower()
'  i    love mc   donalds'
>>> "i" in strthis
False
>>> "  i    " in strthis
False
>>> "I" in strthis
True
>>> return
SyntaxError: 'return' outside function
>>> my_list = range(100)
>>> my_list
range(0, 100)
>>> type(my_list)
<class 'range'>
>>> my_list = for i in range(100)
SyntaxError: invalid syntax
>>> my_list
range(0, 100)
>>> for i in range(100):
	my_list.append(i)

	
Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    my_list.append(i)
AttributeError: 'range' object has no attribute 'append'
>>> my_list
range(0, 100)
>>> my_list = {}
>>> my_list = []
>>> for i in range(100):
	my_list.append(i)

	
>>> my_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> new_list = [el for el in my_list if el % 2 == 0]
>>> 2 % 2
0
>>> 3 % 2
1
>>> 3 % 44
3
>>> 3/44
0.06818181818181818
>>> 9 % 9
0
>>> 9 % 2
1
>>> 9 % 6
3
>>> my_dict = {"id" : 1234567, 'Name' = "Max", "Position": 'Student'}
SyntaxError: invalid syntax
>>> my_dict = {"id" : 1234567, 'Name' : "Max", "Position": 'Student'}
>>> "position" in my_dict
False
>>> "Position" in my_dict
True
>>> mandatory = ["Position", "id", "Name", "Age", "City"]
>>> for i in mandatory:
	print(f"Field{i} is {el in my_dict}")

	
Traceback (most recent call last):
  File "<pyshell#76>", line 2, in <module>
    print(f"Field{i} is {el in my_dict}")
NameError: name 'el' is not defined
>>> for i in mandatory:
	print(f"Field{i} is {in in my_dict}")
	
SyntaxError: invalid syntax
>>> for i in mandatory:
	print(f"Field{i} is {i in my_dict}")

	
FieldPosition is True
Fieldid is True
FieldName is True
FieldAge is False
FieldCity is False
>>> def func1():
	return False
def func2():
	
SyntaxError: invalid syntax
>>> my_dict
{'id': 1234567, 'Name': 'Max', 'Position': 'Student'}
>>> my_dict["age"] = 15
>>> my_dict
{'id': 1234567, 'Name': 'Max', 'Position': 'Student', 'age': 15}
>>> if my_dict ["age "] >= 18:
	print("You Are Adult")

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    if my_dict ["age "] >= 18:
KeyError: 'age '
>>> else:
	
SyntaxError: invalid syntax
>>> 
