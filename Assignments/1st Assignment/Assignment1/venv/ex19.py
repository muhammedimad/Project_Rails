def smaller(num):
    nums = [n for n in range(num) if n % 3 == 0]

    return nums



l=smaller(30)
l.reverse()
print(l)

