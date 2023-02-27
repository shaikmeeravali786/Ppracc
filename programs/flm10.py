# perfect number : a number which is equal to sum of all its factors except given number is known as perfect number


# 28 = 1+2+3+4+7+14 = 28
# 6 = 1+2+3 = 6
"""
num = int(input("enter a number: "))
temp = num
s = 0
for i in range(1,int(num/2)):
    if num%i==0:
        s=s+i
if(s==num):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
"""
n = int(input("enter a number: "))
sum = 0
i = 1
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if n==sum:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")

"""
num=int(input("enter a number: "))
sum=0
i=1  -- initialization
while i<num:
    print(i)
    i=i+1 #6==1,2,3,4,5
while i<num:
    if num%i==0:
        print(i) #6= 1,2,3 which are divisible by 6
        # now which  are divisible values u have to sum 
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if (num==sum):
    print(num, "is perfect number")
else:
    (num, ""is not a perfect number")
    
    
"""