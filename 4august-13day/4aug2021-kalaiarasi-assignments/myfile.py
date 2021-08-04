# myfile=open('file1.txt','w+')

# i=input("enter name:")
# myfile.write(i+"\n")
# #myfile=open('file1.txt','r')
# print(myfile.tell())
# myfile.seek(0)

# x=myfile.read()
# print(str(x))
# myfile.close()


# myfile=open('file1.txt','w+b')
# t=bytearray([1,3,4,5])
# myfile.write(t)
# myfile.close()


# with open('exfile.txt','w+') as f:
#     f.write("hello")
#     f.seek(0)
#     print(f.read())

import csv
headercontent=["Name","Rollno"]
studentdata=[
    {"Name":"kalai","Rollno":1},
    {"Name":"abi","Rollno":2},
    {"Name":"sam","Rollno":3}
]
with open('student.csv','w+',encoding='UTF8',newline='') as s:
    writer=csv.DictWriter(s,fieldnames=headercontent)
    writer.writeheader()
    writer.writerows(studentdata)