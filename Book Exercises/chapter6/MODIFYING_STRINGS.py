'''
What would be a quick way to change all
punctuation in a string to spaces? 
'''

text = ''' hello.world.this. is . a . test. '''

text = text.replace('.', ' ')

# list_text = list(text)
# for i in range(0, len(list_text)):
#     if list_text[i] == '.':
#         list_text[i] = ' '
# text = ''.join(list_text)

print(text)
