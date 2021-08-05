# with open('test2.txt', 'w+')as f:        #with is for exception handling
#     f.write("Hello,world!")
#     f.seek(0)
#     print(f.read())

with open('test2.txt', 'r+')as f:        #it will not create new file
    f.write("Hell,world!")
    f.seek(0)
    print(f.read())

with open('test2.txt', 'a+')as f:        #it will not create new file
    f.write("It's ok. Fine, let's move on")
    f.seek(0)
    print(f.read())