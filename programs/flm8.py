
num = int(input("enter a number"))
def perfect(num):
    sum=0
    i=1
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
        i=i+1
    return num
a = int(input("enter a number: "))
result=perfect(a)
if result==a:
    print("perfect number")
else:
    print("not a perfect number")
