while (True):

    print("1.Enter a name")
    print("2.Display name")
    print("3.Exit ")
    choice = int(input("enter your choice:"))
    if choice == 1:
        
        #print("Enter a  name")
        name = input("enter a name: ")
        message = str(input("write a message:"))
        with open ('Menu_Name_file1.txt','w+') as FD:
            FD.write(name +"\n")      
            FD.write(message +"\n")
        # name_file = open('Menu_Name_file.txt','w+')
        # name_file.write(name)
        
                
    if choice == 2:
        # name_file.seek(0)
        # x = name_file.read()
        # print(str(x))
        # name_file.close
        FD.seek(0)
        x=FD.read()
        print(str(x))
        FD.close
    
    if choice == 3:
        print("Exit")
        break


    