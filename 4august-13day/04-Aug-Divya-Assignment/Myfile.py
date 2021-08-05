myfile= open("File_demo.txt","w")
myfile.write("are you doing well")


myfile= open("File_demo.txt","r")
x =myfile.read()
print(str(x))

myfile.close()