import random
import numpy

list =[]
c=[]
for x in numpy.arange(0,15,2):

    ran=random.randint(1, 2000)
    list.append(ran)

print(list)

# for i in list:
#     if (list.index(i))%3 == 0:
#         c.append(list[i-1])
# print(c)