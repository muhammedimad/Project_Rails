import random

DEFAULT = 5
length=DEFAULT
pool = "abcdefghijklmnopqrstuvwxyz012_34567890ABCDE_FGHIJKLMNOPQRSTUVWXYZ_@"
s=input('how strong you want the password to be?\n')
if s=='High':
    length= 8
elif s == 'Mid':
    length = 6
elif s == 'low':
    length = 6

else:
    length=DEFAULT

p =  "".join(random.sample(pool,length))

print (p)