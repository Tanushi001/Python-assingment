temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
print('temperature before conversion: ', temp)
degree = int(temp[:-1])
if 'C' in temp:
    degree=(degree*9/5)+32
    print('temperature after conversion: ', degree, 'F')
elif 'F' in temp:
    degree=(degree-32)*5/9
    print('temperature after conversion: ', degree, 'C')
else:
    print('enter temperature in recommended form')