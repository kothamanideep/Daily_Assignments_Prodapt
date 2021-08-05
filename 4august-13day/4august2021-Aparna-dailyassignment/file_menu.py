#Menu driven program to perform write, read and append operations on a file
while(True):
    print("1.Write to file")
    print("2.Reading from file")
    print("3.Append data to file")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        myfile=open('file1.txt','w')
        myfile.write("hello world")
        myfile.close()
    if choice==2:
        myfile=open('file1.txt','r')
        x=myfile.read()
        print(str(x))
        myfile.close()
    if choice==3:
        myfile=open('file1.txt','a')
        myfile.write("\nhello world")
        myfile.close()

    if choice==4:
        break
