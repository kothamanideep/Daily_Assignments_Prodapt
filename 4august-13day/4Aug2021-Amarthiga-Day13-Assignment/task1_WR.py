#task1 create menudriven app. 1. to read and write the programme
while(True):
    print("1.Write a file: ")
    print("2.Read a file: ")
    print("3. Close the file")

    selection= int(input("Type your response: "))

    if selection==1:
        print("Write a file option has selected")
    #     def write1(file1):
    #         file_name=input("Enter a file name, you want to write: ")
    #         content = input("Enter your content: ")
    #         file1 = open(file_name,'w+')
    #         file1.write(content)
    #         print(file1.write(content))
    #         return
        file_name=input("Enter a file name, you want to write: ")
        with open(file_name, 'w+')as i: 
            content = input("Enter your content: ")
            i.write(content)       
            i.seek(0)
            print(i.read())
            #file_name.close()
    if selection ==2:
        print("Read a file option has selected: ")
        exist_file = input("Type your file name to read: ")
        with open(exist_file, 'r+')as n: 
            #content = input("Enter your content: ")
            #n.write(content)       
            n.seek(0)
            print(n.read())
            #exist_file.close()
    if selection ==3:
        print("File Colsed")
        break



    



