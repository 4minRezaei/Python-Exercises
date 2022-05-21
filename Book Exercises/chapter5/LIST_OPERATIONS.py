'''
What would be the result of len([[1,2]] * 3)? 
What are two differences between using the in operator and a list's index() method?
'''

print(len([[1, 2]] * 3))
# Return 3

ls = [1, 2, 3, 4, 5, 6]
print(3 in ls)
# Return boolean value.

print(ls.index(3))
# Return first index of value.

'''
Which of the following will raise an exception?:
min(["a", "b”, "c"]);
max([1, 2, "three"]);
[1, 2, 3].count("one")
'''
print(min(['a', 'b', 'c']))
# Return 'a'

#print(max([1, 2, 'three']))
# Return Error (typeError: '>' not supported between instances of 'str' and 'int')

print([1, 2, 3].count('one'))
# Return 0 (there is no 'one' in that list)

'''
If you have a list x, write the code to safely remove
an item if—and only if—that value is in the list.
'''
ls = [1, 2, 3, 4, 5, 6]
# assume we want to remove 3.
if (3 in ls):
    ls.remove(3)
else:
    pass

'''
Modify that code to remove the element only if the item occurs in the list
more than once.
'''
ls = [1, 2, 3, 3, 3, 4, 5, 6]
# assume we want to remove 3.
if (ls.count(3)>1):
    ls.remove(3)
else:
    pass