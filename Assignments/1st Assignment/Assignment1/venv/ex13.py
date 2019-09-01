
f= open("Homowrk.txt",'r')
f2= open("Answers.txt",'w')

lines = [line.strip('\n') for line in f]
length=len(lines)

for i in range(length):
    try:
        s=str(lines[i])
        list=lines[i].split(" ",3)
        print(list)
        operator=list[1]
        print(operator)
        if operator=='+':
            ans = int(list[0]) + int(list[2])
            string=" ".join(list[0:])+" ="
            print(string)
            f2.write(str(string)+' '+str(ans)+'\n')
        elif operator == '*':
            ans = int(list[0]) * int(list[2])
            string = " ".join(list[0:]) + " ="
            print(string)
            f2.write(str(string) + ' ' + str(ans) + '\n')
        elif operator == '/':
            ans = int(list[0]) / int(list[2])
            string = " ".join(list[0:]) + " ="
            print(string)
            f2.write(str(string) + ' ' + str(ans) + '\n')
        elif operator == '-':
            ans = int(list[0]) - int(list[2])
            string = " ".join(list[0:]) + " ="
            print(string)
            f2.write(str(string) + ' ' + str(ans) + '\n')

    except:
        f2.write("Wrong entry"+"\n")
