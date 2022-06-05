Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"""
If the string x equals "(name, date),\n", which of
the following would return a string containing "name, date"?
x.rstrip("),")
x.strip("),\n")
x.strip("\n)(,")
"""
'\nIf the string x equals "(name, date),\n", which of\nthe following would return a string containing "name, date"?\nx.rstrip("),")\nx.strip("),\n")\nx.strip("\n)(,")\n'
x = "(name, date),\n"
x.rstrip("),")
'(name, date),\n'
x.strip("),\n")

'(name, date'
x.strip("\n)(,")
'name, date'
