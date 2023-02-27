# check number is automorphic number or not
# if the square of number ends with given number then we can call it as automarphic number

# ex -1:
# n = 5
# n*n = 5x5 =25 -- ends with 5=n
# 5 is Automarphic number

# ex-2:
# n=25
# n*n=25x25=625 --ends with 25=n
# 25 is Automarphic number

num = int(input("enter a number: "))
sqr = num*num
f = 0
temp = sqr
n=10
while temp>0:
    rem=sqr%n
    if num==rem:
        f=1
        break
    temp=int(temp/10)
    n=n*10
if f == 1:
    print("number is automorphic number")
else:
    print("number is not a automorphic number")
