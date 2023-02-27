# whether the given number is a harshadh number or not niven number

# 81 = 8+1 = 9
# 81 % 9 = 0 this is the condition for harshadh number

num = int(input("enter a number: ")) # 81
temp = num
sum = 0
while(temp!=0): #(81!=0)  ,, (8!=0)
    rem=temp%10 #rem=81%10 --rem = 1  ,, rem=8%10--rem=8
    sum=sum+rem # sum = 0+1   ,, sum= 1+8=9
    temp=int(temp/10) # temp=int(81/10)--temp=8  ,, temp=int(8/10)--temp=0---here loop closes
if num%sum == 0: # 81 % 9==0
    print(num,"is a harshad number or niven number")
else:
    print(num,"is not a harshad or niven number")
