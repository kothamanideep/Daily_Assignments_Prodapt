import logging
myfile=open('file2.txt','w')
logging.basicConfig(filename='error.log',level=logging.ERROR)

############ menu for names
while (True):
    print("\n***FILE MENU***")
    print("1. Add your name")
    print("2. View your name")
    print("3. Exit")
    ##### try and except block using logging for handling type error
    try:  
        c=int(input("Enter your choice "))
    except:
        logging.error("Please enter correct option in integer form ")
        continue

    if c==1:
        name=input("Enter your name :")
        myfile=open('file2.txt','a')
        myfile.write(name+" ")
            
    if c==2:
        print("\nDisplaying your name ")
        myfile=open('file2.txt','r')
        x =myfile.read()
        print(str(x))
    if c==3:
        break  
myfile.close     



