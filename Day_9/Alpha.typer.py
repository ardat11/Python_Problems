#This code takes 3 numbers as input and output letters from the alphabet list that correspond to those indexes.
#Keep in mind that indexes starts from 0 so if you want to print "A" you should input 0.

import string


alp = string.ascii_uppercase

x = int(input())
y = int(input())
z = int(input())

print(alp[x])
print(alp[y])
print(alp[z])