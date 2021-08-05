#1
'''myfile =open("file.txt",'w')    #if the file is exisiting it will open. otherwise create and open it

#w - refers to write the file, r - refers to read the file

myfile.write("Hi,Amar!")
#myfile.close()      #if we put close before reding, it will give error. close should be used after the function. Until we use close, it may lead to data leakage

myfile =open("file.txt",'r')
x=myfile.read()
print(x)

myfile.close()
'''
#if we use w+ or r+, then it will read and write
#if the file is already there, we ca use r+
#if the file is not there, we can use w+ for create a file
myfile =open("test1.txt",'w+')
myfile.write("Amarthiga")
#myfile=open("test1.txt", "r")

y=myfile.read()
print(y)
#myfile.close()

#a - append. a+ - append +write. wb- for binary and rb - read binary

#task1 create menudriven app. 1. to read and write the programme

#3
myfile = open("test1.txt", 'a+')
print(myfile.tell())    # cursor current position
myfile.seek(0)           #seek function is for 

myfile.close()

