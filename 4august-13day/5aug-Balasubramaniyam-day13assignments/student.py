'''menu driver 1)add student(nmae,rollno,adminno,marks of 5 subjects) use the oops concepts (inheritance)
             2) search students details using rollno 
               3)List students api with marks
               4)print all the students based on ranking (sum of marks)'''
import csv
t=0          
class Student:
    def __init__(self,name,rollno,admino) :
        self.name=name
        self.rollno=rollno
        self.admino=admino
class Marks(Student):
    def __init__(self, name, rollno, admino,english,tamil,maths,science,social):
        self.english=english
        self.tamil=tamil
        self.maths=maths
        self.science=science
        self.social=social
        super().__init__(name,rollno,admino)
    def add(self):
        
        dict1={'name':self.name,'rollno':self.rollno,'admino':self.admino,'english':self.english,'tamil':self.tamil,'maths':self.maths,'science':self.science,'social':self.social}
        studentslist.append(dict1)
        

        #else:
        #   Studentdict=Studentdict.new_child(dict1)
    def search(self,rollno):
        for i in studentslist:
            if str(i['rollno'])==str(rollno):
                print(i)
    def display(self):
        print(studentslist)
    def ranking(self):
        for i in range(len(studentslist)):
            for j in range(0,len(studentslist)-i-1):
                a=studentslist[j]
                sum1=int(a['english'])+int(a['tamil'])+int(a['maths'])+int(a['science'])+int(a['social'])
                b=studentslist[j+1]
                sum2=int(b['english'])+int(b['tamil'])+int(b['maths'])+int(b['science'])+int(b['social'])
    
                if sum1<sum2:
                    studentslist[j],studentslist[j+1]=studentslist[j+1],studentslist[j]
        for i in studentslist:
            a=i
            sum1=int(a['english'])+int(a['tamil'])+int(a['maths'])+int(a['science'])+int(a['social'])
            print(i,sum1)
studentslist=[]
def validationstudent(name,rollno,admino,english,tamil,maths,science,social):
    return True
while(1):
    print("1)Add Student : ")
    print("2) Search Students using Roll No")
    print("3) Display students like API")
    print("4) Ranking ")
    print("5) Save")
    option=int(input("Enter your Option : "))
    if option==1:
        rows=[]
        source="studentsource.csv"
        with open(source,'r') as fi:
            data=csv.reader(fi)
            for row in data:
                rows.append(row)
            print(rows)
            length=int(input("Enter the row that we have to add : "))
            for i in range(1,length+1):
                a=rows[i]
                name=a[0]
                rollno=a[1]
                admino=a[2]
                english=a[3]
                tamil=a[4]
                maths=a[5]
                science=a[6]
                social=a[7]
                if validationstudent(name,rollno,admino,english,tamil,maths,science,social)==True:
                    obj1=Marks(name,rollno,admino,english,tamil,maths,science,social)
                    t=obj1.add()
    if option==2:
        srollno=int(input("Enter  Roll no to search : "))
        obj1.search(srollno)
    if option==3:
        obj1.display()
    if option==4:
        obj1.ranking()
    if option==5:
        headercontent=["name","rollno","admino","english","tamil","maths","science","social"]
        destination="studentdestination.csv"
        with open(destination,"a+",encoding="UTF8",newline="") as stdwriter:
            swriting=csv.DictWriter(stdwriter,fieldnames=headercontent)
            swriting.writeheader()
            swriting.writerows(studentslist)
    if option==6:
        break