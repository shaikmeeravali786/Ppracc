# abundant number

num = int(input("enter a number : ")) # num = int(input("12") taken number is 12

sum = 0
for i in range(1,num):  # for i in range(1,num means num-1 then value is 11) ( for i in range(1,11)
    if num%i==0:  #12%1==0: 12%2==0: 12%3==0: 12%4==0:12%6==0 (12%5==0, 12%7==0,12%8==0, 12%9==0...those not divided to 12)
        sum = sum+i # 0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+6=16
if sum > num: #16>12:  condition is which taken sum is greater than taken number then it is called abundant
    print("Number is an abundant number")
else:
    print("Number is not an abundant number")