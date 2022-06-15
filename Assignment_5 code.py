
#Question 1.
print("Question 1")
sen=str(input("Enter the string: "))
reverse_sen=sen[::-1]
print("Reversed string is : ",reverse_sen)

#Question 2.
print("Question 2")
num=int(input("Enter the number: "))
range_1=int(input("Enter the value of range: "))
for i in range(range_1):
    if i%num==0:
        print(i)
    else:
        continue

#Question 3:
from math import sqrt
a=float(input("Enter the value of first side: "))
b=float(input("Enter the value of second side: "))
c=float(input("Enter the value of third side: "))
s = (a+b+c)/2
 #Herons formula = sqrt((s)(s-a)(s-b)(s-c))
area_sq = s*(s-a)*(s-b)*(s-c)
if area_sq> 0:
    print("Area : ", sqrt(area_sq))
else:
    print("Triangle will not form")

#Question 4.
print("Question 4")
for i in range(5):
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(5,10):
    for j in range(i,10):
        print('*',end=' ')
    print()

#Question 5.
print("Question 5")
n=int(input("Enter the number of rows: "))
k=ord('A')
for i in range (n):
    for j in range (i+1):
     print(chr(k),end=' ')
     k+=1
    print()

#Question 6.
lower=int(input("Enter the lower bound of the range: "))
upper=int(input("Enter the upper bound of the range: "))
for n in range (lower,upper+1):
    if n>1:
        for i in range (2,n):
            if (n%i)==0:
                break
        else:
         print(n)

#Question 7.
print("Question 7")
for i in range(1,501):
    if i%7==0 and i%11==0:
        print(i)

#Question 8.
from itertools import count
print("Question 8")
a=[]
n=int(input("Enter the number of elements: "))
for i in range (0,n):
    e=int(input())
    a.append(e)

print(a)
print('A')
for num in a:
    if num>0:
        print('Positive numbers are: ',num)
print('B')
for num in a:
    if num<0:
        print("Negative numbers are: ",num)
print('C')
for num in a:
    if num%2!=0:
        print("Odd numbers are: ",num)
print('D')
for num in a:
    if num%2==0:
        print("Even numbers are: ",num)
print('E')
for num in a:
    print("Numer of times",num,"occours is",a.count(num))

#Question 9.
print("Question 9")
a=[]
n=int(input("Enter the number of elements: "))
for i in range (0,n):
    e=(input())
    a.append(e)
print(a)
for ele in a:
    print("word",ele,"occours",a.count(ele),'time')



