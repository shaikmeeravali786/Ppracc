# natural Number > 1
# which hs only 2 faactors 1 and itself

# 19 ==> 1 and 19 ==> prime number
# 28 ==> 1,2,4,7,14,28 ==> Not a prime number

num = int(input("enter a number: "))
count = 0

if num>1:
    for i in range(1, num+1):
        if (num%i)== 0:
            count = count + 1
    if count == 2:
        print("Number is prime")
    else:
        print("Number is not prime ")

