import string
str=input('enter string')
punc=string.punctuation
for i in punc:
    str=str.replace(i, '')
print(str)