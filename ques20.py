lst=[]
n=int(input('enter no of terms'))
for i in range(0,n):
    num=int(input())
    lst.append(num)
print(lst)
sum=0
for i in lst:
    i=int(i)
    sum=sum+i
print(sum)
    