# n=100
#
# primeNumbers=[]
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#         primeNumbers.append(i)
#
# print("numbers of prime numbers in 1 to 100 is", len(primeNumbers))

"""
primeNumbers=[]
for i in range(2,100+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        primeNumbers.append(i)
print("numbers of prime numbers in 1 to 100 is", len(primeNumbers))
"""

primeNumbers=[]
for i in range(2,50):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        primeNumbers.append(i)
print("2 to 100", len(primeNumbers))