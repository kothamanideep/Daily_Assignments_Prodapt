import re
import time
import csv
try:
    headerContent=["name","rollno","admin","english","chemistry","maths","physics","addedon"]
    studlist=[]
    class Student:
       def addStudents(self,name,rollno,admin):
        name=" "
        rollnum=0
        adminnum=0    
    class marks:
      def marks():
        english=0
        chemistry=0
        math=0
        physics=0
    class studentdetails(Student,marks):
     def addstudentdetails(self,name,rollno,admin,english,chemistry,maths,physics):
        total=english+chemistry+maths+physics
        current_local_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
        dict1={"name":name,"rollno":rollno,"admin":admin,"english":english,"chemistry":chemistry,"maths":maths,"physics":physics,"total":total,"addedon":current_local_time}
        studlist.append(dict1)
    obj1=studentdetails()
    while(True):
        print("1. Add Students:")
        print("2. display student details: ")
        print("3. search student using roll number")
        print("4. Ranking")
        print("5. display csv file")
        print("6.exit")
        choice=int(input("enter your choice: "))
        if choice==1:

            name=input("Enter your name: ")
            temp_name=name
            while True:
                if not re.match("[A-Za-z]+", temp_name):
                    
                    name=input("Enter valid name:")
                    temp_name= name
                else:
                    break
            rollno=(input("enter your rollno: "))
            temp_rollno=rollno
            while True:
                if not re.match("[0-9]{2}",temp_rollno):
                    rollno=input("enter the valid rollno:")
                    temp_rollno=rollno
                else:
                    break    
        
            admin=(input("enter your admin: "))
            temp_admin=admin
            while (True):
                if not re.match("[0-9]{5}",temp_admin):
                    admin=input("enter the valid admin:")
                    temp_admin=admin
                else:
                    break    
            
            english=int(input("enter english marks: "))
            chemistry=int(input("enter chemistry marks: "))
            maths=int(input("enter maths marks: "))
            physics=int(input("enter physic marks: "))

                
            
            obj1.addstudentdetails(name,rollno,admin,english,chemistry,maths,physics)
            
        if choice==2:
            print(studlist)
        if choice==3:
            srollno=int(input("Enter roll number to search: "))
            print(list(filter(lambda i:i["rollnum"]==srollno,studlist)))
        if choice==4:
            print(sorted(studlist,key=lambda i:i["total"],reverse=True))
        if choice==5:
            with open("file3.csv","w+",encoding="UTF8",newline="") as s:
                writer=csv.DictWriter(s,fieldnames=headerContent)
                writer.writeheader()
                writer.writerows(studlist)
        if choice==6:
            break
         
except Exception:
    print("something went wrong")
finally:
    print("Thank You!!")