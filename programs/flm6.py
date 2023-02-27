"""num=int(input("enter a number"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum>num:
    print("number is abundant")
else:
    print("not a abundant")"""

"""
num=int(input("enter a number: ")) # 26=1,2,13 ==1+2+13=16
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(num, "is perfect number")
else:
    print(num, "not a perfect number")"""

num=int(input("enter a number"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum>num:
    print("number is abundant")
else:
    print("not a abundant")