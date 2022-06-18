
# Suppose that you have a list of strings in which
# some (but not necessarily all) of the strings begin and end with the double
# quote character:
#  x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']

# What code would you use on each element to remove just the double quotes?
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
for i in range(len(x)):
    if x[i][-1] == '"':
        x[i] = x[i].rstrip('"')
print(x)
# What code could you use to find the position of the last p in Mississippi?
y = 'Mississippi'
print(y.rfind('p'))


# When you have found that position, what code would you use to remove just that letter
yls = []
for i in y:
    yls.append(i)
yls.pop(y.rfind('p'))
y = "".join(yls)
print(y)
