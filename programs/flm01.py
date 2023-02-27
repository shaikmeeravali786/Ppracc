""""
l2=[]
def nes_list(l1):
    for i in l1:
        if type(i)==list:
            nes_list(i)
        else:
            l2.append(i)
    return l2
l1={"a":10,{"a":10}}
print(nes_list(l1))
l2=[]
l1=[2,3,4,5,5,[45,6],8,[9,[10]]
for i in l1:
    if type(i) == list:
       nes_list(i)
    else:
      l2.append(i)
print(l2)
"""
#Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
#for x in Employee.values():
#    print(x)
#LIST
l1=[1,5,4,7,6,8]
l2=[2,3]
for i in l2:
    l1.insert(1,i)
l2=[]
while l1>[]:
    a=0
    for i in l1:
        if a<=0:
            a=i
    l2=[a]+l2
    l1.remove(a)
l2.reverse()
print(l2)
print("highest 3 numbers",l2[n-1])






