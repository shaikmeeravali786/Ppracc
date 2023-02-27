""""
l1=[10,20,30,40]
l2=[10,20,30,40]
print(l1 is l2)
print(id(l1))
print(id(l2))

#find max of 3 given numbers

a=int(input("enter a first value:"))
b=int(input("enter a second value: "))
c=int(input("enter a third value: "))

max = a if a>b and a>c else b if b>c else c
print("max value:", max)

#write a program to reverse the string
s="durga"
output=s[::-1]
print(output)

s=input("enter a string: ")
output=s[::-1]
print("Reversed string is",output)

#another type of reversed
s="thing"
r=reversed(s)
for ch in r:
    print(ch)"""
"""
#wpt to reverse content of the given string by using reversed() function
s=input("enter some string: ")
r=reversed(s)
output="".join(r)
print(output)
 
#write a program to reverse of the given string by using while loop?

s=input("enter some string: ")
output=""
l=len(s)-1
while l>=0:
    output=output+s[l]
    l=l-1
print(output)


# wpt to reverse order of words present in the given string?

s=input("enter some string: ")
l=s.split()
l1=l[::-1]
output=" ".join(l1)
print(output)

s=input("enter some string: ")
l=s.split()
l1=l[::-1]
output=" ".join(l1)
print(output)

#wpt REVERSE internal content of each word?
s=input("enter :")
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
    output=" ".join(l1)

print(output)

#wpt REVERSE internal content of every second word present in the givwn string?

#input:one two three four five sx
#output:one owt three ruof five xis

s="one two three four five six"
l=s.split()
l1=[]
i=0
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output=" ".join(l1)
print(output)

s="B4A1D3"
alphabets=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output="".join(sorted(alphabets)+sorted(digits))
print(output)"""

#wpt for the following requiremnets?
#input=a4b3c2
#o/p:aaaabbbcc



