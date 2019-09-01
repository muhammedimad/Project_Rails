def main():
    for num in range (0,101):

        temp=int(num/10)
        if((num % 7 == 0) or temp == 7 or ( num % 10 == 7)):
            print(num)
main()

