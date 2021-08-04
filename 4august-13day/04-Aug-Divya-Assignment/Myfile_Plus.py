myfile= open("File1_demo.txt","a+")
myfile.write("I am doing great ..")
myfile.seek(0)

#myfile= open("File_demo.txt","r")
x =myfile.read()
print(str(x))

myfile.close()