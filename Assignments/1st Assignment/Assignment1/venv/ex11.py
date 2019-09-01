f = open("file.txt", "r")
f2 = open("file2.txt", "w")

contents=f.read()
f2.write(contents)

print(f2)
