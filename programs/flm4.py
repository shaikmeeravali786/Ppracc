# automorphic number : If the square of number ends with given number then we call it ass automorphic number.
num=int(input("enter a number: "))
sqr=num*num
f=0
temp=sqr
n=10
while temp>0:
    rem=sqr%n
    if num==rem:
        f=1
        break
    temp=int(temp/10)
    n=n*10
if f==1:
    print("number is automorphic")
else:
    print("number is not automorphic")