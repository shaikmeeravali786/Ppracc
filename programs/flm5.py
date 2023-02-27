num = int(input("enter a number: "))
temp =num
sum=0
while (temp!=0):
    reminder = temp%10
    sum = sum+reminder
    temp=int(temp/10) # withought taking float value
if num%sum==0:
    print(num,"is a harshadh number")
else:
    print(num,"not a harshadh not niven number")