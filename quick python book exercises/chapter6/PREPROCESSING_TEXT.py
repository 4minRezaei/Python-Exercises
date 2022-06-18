# 6.9 page: 88
'''
In this lab,
the task is to read the first part of the first chapter of Moby Dick (found in the book's source code),
make sure that everything is one case, remove all punctuation, and write the words one per line to a second file.
'''
import re
import string

infile = open("moby_01.txt")
outfile = open("moby_01_clean.txt", "w")
clean_words = list()
puncs = string.punctuation
table = dict()
for symb in puncs:
       table[ord(symb)] = ''

for line in infile:
       line = line.lower()
       line = line.translate(table)
       line = line.split()
       if bool(line): 
         line.append('\n')
       clean_words.extend(line)

outfile.write(' '.join(clean_words))
