#To print the string in reverse order"
"""
data=input("enter a sting:")
out=data[::-1]
print(out)"""
"""
# Reverse the strng by using the reversed funtion
data=input("enter number:")
reverse_fuc=reversed(data)
out=" ".join(reverse_fuc)
print(out)"""

# python interview
"""
# is operator & == operator

l1=[10,20,30,40]
l2=[10,20,30,40]
#print(l1 is l2)
#print(l1 == l2)

l3 = l1
#print(l1 == l3)
#print(l1 is l3)
"""
"""
# max of given 2 nummbers
a=input("enter first value:")
b=input("enter second value:")
c=input("enter third value:")
max=a if a>b and a>c else b if b>c else c
print("max of given values", max)
"""
"""
data1=input("enter first value:")
data2=input("enter second value:")
data3=input("enter third value:")
min = data1 if data1<data2 and data1<data3 else data2 if data2<data3 else data3
print("min value", min)

l1=[1,2]
s="empty list" if l1==[] else "not empty"
print(s)

l1=[1]
s="empty list" if not l1 else "empty not"
print(s)

l1=[1,2,3]
s="empty" if not l1 else"not list"
print(s)
# first character is upper case
s="meeravali"
s1=s[0].upper()+s[1:]
print(s1)
s="meeravalithat"
s1=s[0].upper()+s[1:]
print(s1)"""

# s="meeravali"
# length=len(s)
# s1=s[0:len(s)-1] + s[-1].upper()
# print(s1)
#
# s="dfbouorbyfuebre"
#
# s1=s[0:len(s)-1]+s[-1].upper()
# print(s1)
#
# s="rrefberwbh"
# s1=s[0].upper()+s[0:len(s)-1]+s[-1].upper()
# print(s1)
