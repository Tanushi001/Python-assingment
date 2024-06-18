str=input('enter string ')
start=input('starts with ')
end=input('ends with ')
if(str.startswith(start)):
    print("string starts with ", start)
else:
    print("string doesn't start with", start)
if(str.endswith(end)):
    print('string ends with ', end)
else:
    print("string doesn't end with ", end)