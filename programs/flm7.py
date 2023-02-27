# abunndant number

num = int(input("enter a number: "))# 12
sum=0
for i in range(1,num): #(1,11)
    if num%i==0: #1,2,3,4,6,
        sum=sum+i # 0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+6=16
if sum>num: # 16>12
    print("number is a abundant number")
else:
    print("number is not a abundant number")

