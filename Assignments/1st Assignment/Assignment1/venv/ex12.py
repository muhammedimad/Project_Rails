def content(name):
    f=open(name,"r")
    contents=f.read()
    print(contents)

content("test.txt")