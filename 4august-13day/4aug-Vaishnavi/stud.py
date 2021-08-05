import re,sys,time,csv

header =['total','name','rollno','admin','english','hindi','maths','science','social','Addon']


studentlist=[]
class StudentDetails:
    def adddetails(self,name,ls,):
        totalmarks=sum(ls[2:])
        date_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
        dict1={'total':totalmarks,'name':name,'rollno':ls[0],'admin':ls[1],'english':ls[1],'hindi':ls[2],'maths':ls[3],'science':ls[4],'social':ls[5],'Addon':date_time} 
        studentlist.append(dict1)
obj1=StudentDetails()      
while(True):
    print("1.add student")
    print("2.search student")
    print("3.display")
    print("4.ranking")
    print("5.exit")
    print("6. save to file") 
    choice=int(input("Enter your choice : "))
# obj=StudentDetails()
    if choice==1:
        name=input("Enter the name : ")
        rollno=int(input("Enter the roll no : "))
        admin=int(input("Enter the admission no : "))
        english=int(input("Enter the marks of English : "))
        hindi=int(input("Enter the marks of Hindi : "))
        maths=int(input("Enter the marks of maths : "))
        science=int(input("Enter the marks of Science : "))
        social=int(input("Enter the marks of Social : "))
    #obj=StudentDetails()
        def validate(rollno,admin,english,hindi,maths,science,social):
            val=re.match('^[1-9]',rollno)
            val1=re.match('^[1-9]',admin)
            val2=re.match('^[0-9]',english)
            val3=re.match('^[0-9]',hindi)
            val4=re.match('^[0-9]',maths)
            val5=re.match('^[0-9]',science)
            val6=re.match('^[0-9]',social)
            if val and val1 and val2 and val3 and val4 and val5 and val6:
                return[int(rollno),int(admin),int(english),int(hindi),int(maths),int(science),int(social)]
            else:
                print("Incorrect input")
                sys.exit()
        obj1.adddetails(name,validate(rollno,admin,english,hindi,maths,science,social))
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=int(input("Enter the rollno to search : "))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
    if choice==5:
        sys.exit()
    if choice==6:
        with open('student.csv','w+',encoding='UTF8',newline='')as s:
            writer=csv.DictWriter(s,fieldnames=header)
            writer.writeheader()
            writer.writerows(studentlist)
