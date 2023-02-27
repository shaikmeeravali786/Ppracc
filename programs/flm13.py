# check nummber is perfect number or not

# perfect number : a positie integer that is equal to sum of its proper divisors called perfect number
# ex: 6 = 1+2+3 , 28 = 1+2+4+7+14

num = int(input("enter a number: ")) # number 28
temp = num #temp = 28
sum = 0
for i in range(1,int(num/2)+1): # 28 divides 1,2,4,7,14
    if num%i==0:
        sum = sum+i # sum =0+1=0
                    # sum =1+2=3
                    # sum =3+4=7
                    # sum =7+7=14
                    # sum =14+14=28
if (sum==num): #when sum==num(28==28) then number is perfect number else not perfect number
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
