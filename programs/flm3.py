# l = [1,-2,4,-5,6,-7]
# l1=[]
# l2=[]
# for i in l:
#     if i>0:
#         l1.append(i)
#         c1=len(l1)
#     else:
#         l2.append(i)
#         c2=len(l2)
# print("positive-{} count-{} negative-{} count-{}".format(l1,c1,l2,c2))
# l.sort()
# print(l)
# a=10
# b=20
# a=b+a
# b=a-b
# a=a-b
# print(a,b)
# a1=10
# b1=20
# a1,b1=b1,a1
# print(a1,b1)
str1="aaaabbbcc"
s2=" "
for i in str1:
    if i.isalpha():
        x=i
    else:
        d=int(i)
        s2=s2+x+d
print(s2)
