# find factorial number
 # 5! = 1 x 2 x 3 x 4 x 5 = 120

 # iteratie approach

factorial = 1
num = 5

if num<0:
    print("factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("the factorial of", num, "is", factorial)

fact = 1
num = int(input("enter a number: "))
if num<0:
    print("fact does not exist")
elif num==0:
    print("fact of o is 1")
else:
    for i  in range(1,num+1):
        fact = fact*i
    print("the fact is", num, "is", fact)

# recursion approach
def factorial(n):
     if (n==0 or n==1):
         return 1
     else:
         return n*factorial(n-1)
num = 3
print("factorial of", num, "is", factorial(num))

# recursive approach
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
num = 6
print("fact of", num, "is", factorial(num))
