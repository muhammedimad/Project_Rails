def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


a = int(input("enter a\n"))
b = int(input("enter b\n"))
if b==0:
    ans2 = print('division is illegal')
else:
    ans2 = float(division(a, b))
    print('div is',ans2)

ans1 = int(multiplication(a, b))


print('mul is '+str(ans1))
