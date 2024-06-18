lst=[]
n=int(input('enter no of terms'))
for i in range(0,n):
    num=int(input())
    lst.append(num)
print(lst)
print("min=",min(lst))
print("max=",max(lst))