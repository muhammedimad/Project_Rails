def fib(prev0,prev1):
    return (prev0+prev1)




def main():
    n = 2
    temp0=0
    temp1=1
    print(temp0)
    print(temp1)
    while (True):
        if (n==0):
            print("0")
        if (n==1):
            print("1")
        if (n<=10000):
            res = int(fib(temp0,temp1))
            temp0 = temp1
            temp1=res
            print(int(res))
            n = n+1
main()
