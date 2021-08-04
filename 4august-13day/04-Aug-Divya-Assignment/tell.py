myfile= open("File3_demo.txt","a+")
i = input("enter a name:")

myfile.write(i+"\n")
print(myfile.tell())
myfile.seek(0)
x =myfile.read()
print(str(x))
myfile.close