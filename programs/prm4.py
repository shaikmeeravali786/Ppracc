# fibonacci series

# a series of number in which each number (fibonacci series) is the sum of the  two preceeding numbers

 # 0 -(0+1)- 1 -(1+1)- 2 - (1+2)- 3 -(2+3) - 5 - (3+5)- 8

 # 0  1  1  2 3 5 8 13 21 34

n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(2,3):
    sum = n1 + n2
    print(sum)
    n1 = n2
    n2 = sum
