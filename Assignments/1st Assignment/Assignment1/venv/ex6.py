num=input("Please enter a five digit number\n")
if(len(num)>5):
    print("error")
else:
    print("you entered the number "+ num)
    digits=[int(n) for n in num]
    print("the digits of the number are:\n",digits)
    ans=sum(digits)
    print("the sum of the digits is:",ans)