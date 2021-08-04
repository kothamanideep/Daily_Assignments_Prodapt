#tell cursor in which postiton
#seek() helpthe cursor to move the specified postion
#a+ used to append the word into the file
myfile=open("demo.txt",'a+')
print(myfile.tell())
myfile.seek(0)
print(myfile.read())
myfile.write("  hi i am balu")
#myfile.close()
myfile.seek(0)
#myfile=open("demo.txt",'r')
print(myfile.read())
myfile.close()

