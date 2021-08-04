with open ('File_demo.txt','a+') as FD:
    FD.write("I am thinking your doing great!")
    FD.seek(0)
    print(FD.read())