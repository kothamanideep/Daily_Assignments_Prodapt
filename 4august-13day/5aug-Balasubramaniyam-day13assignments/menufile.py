while(1):
    print("1) adding text to file")
    print("2) display the text in file")
    print("3) Exit ")
    option=int(input("Enter the option : "))
    myfile=open("demo.txt",'w+')
    if option==1:
        text=input("Enter the text : ")
        myfile.write(text)
    if option==2:
        print(myfile.read())
    if option==3:
        break
myfile.close()