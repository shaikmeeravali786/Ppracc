"""
ipv4---internet protocal version 4
1. The IP adress must contain four integers ranging from 0 to 255
2. That are separated by dots .
3. for e.g:: 0.0.0 to 255.255.255 ----valid ip adress means below of 255.255.255.255

The decimal value of each part of the IP adress
Should not exceed 255 and must not be less than zero.

2.3.89.56 # valid ip
258.2.365 #not valid ip address

"""

"""
import re

IP=input("enter IP adress to check for validity: ")
# pettern will start with ^ and end with $
pattern="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

# """
# 0-99 ==> [1-9]?[0-9]
# 100-199 ==> 1[0-9][0-9]
# 200-249==> 2[0-4][0-9]
# 250-255==> 25[0-5]
# """
"""
 #               or
if (re.search(pattern, IP)):
    print(f"{IP} is valid IP adress")
else:
    print(f"{IP} is Invalid IP adress")

#     or  we can do like this also
def check_ip(IP):

    if (re.search(pattern,IP)):
        print(f"{IP} is valid IP adress")
    else:
        print(f"{IP} is Invalid IP adress")
check_ip(IP)

o/p:
eneter IP adress to check for validity: 256.23.21.13
256.23.21.13 is Invalid IP adress"""
"""
1.Write a function to validate if a string is a valid ip adress or not
2. a valid ip adress should be in form of x1.x2.x3.x4 where x1,x2,x3,x4
3.should be numbers between 0 and 255

steps to do in program 
1. check 4 digits or not
2.it is a digit 
3. 0 and 255
"""
import re
IP=input("enter a valid ip adress: ")   #ekada manam 255.255.255.255 dhintlo 255 anedhi 3 times unidhi soo \. use chestham and 3 times unidhi kabati {3} anedhi estham
pattern="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check_ip(IP):
    if re.search(pattern,IP):
        print(f"{IP} adress is valid")
    else:
        print(f"{IP} adress is invalid")
check_ip(IP)