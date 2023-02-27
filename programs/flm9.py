# 6 = sum of all factors not a given number
"""
num = int(input("enter a number: "))
sum = 0
i =1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if (num==sum):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")"""

num = int(input("enter a number: "))
sum = 0
i = 1
for i in range(1,num):
    if num%i==0:
        sum=sum+i
    i=i+1
if (num==sum):
    print(num, "ia a perfect number")
else:
    print(num, "not a perfect number")