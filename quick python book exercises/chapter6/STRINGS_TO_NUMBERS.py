Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"""
Which of the following will not be converted to numbers, and why?
int('a1')
int('12G', 16)
float("12345678901234567890")
int("12*2")
"""
'\nWhich of the following will not be con\x02verted to numbers, and why?\nint(\'a1\')\nint(\'12G\', 16)\nfloat("12345678901234567890")\nint("12*2")\n'
int('a1')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int('a1')
ValueError: invalid literal for int() with base 10: 'a1'
int('12G', 16)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('12G', 16)
ValueError: invalid literal for int() with base 16: '12G'
float("12345678901234567890")
1.2345678901234567e+19
int("12*2")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("12*2")
ValueError: invalid literal for int() with base 10: '12*2'
