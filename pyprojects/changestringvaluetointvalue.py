Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 1
>>> num2 = 2
>>> 
>>> print(num1 + num2)
3
>>> num1 = 1.2
>>> num2 = 2.1
>>> print(num1 + num2)
3.3
>>> num1 = "1"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> print(int(num1) + num2)
3.1
>>> 
