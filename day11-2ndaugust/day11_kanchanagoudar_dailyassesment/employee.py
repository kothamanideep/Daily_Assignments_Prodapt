employee_dict={}
sal2=[]
list1=[]
from os import name
import re
import collections

dict1={}
def addemployee():
    name=input("Enter the employee name:")
    designation=input("Employee desgination:")
    employeeid=int(input("Enter the Employeeid:"))  
    salary=int(input("Enter the salary:"))
    phonenumber=int(input("Enter the phonenumber:"))
    address=input("Enter the address:")
    pincode=int(input("Enter the pincode:"))
    dict1={"Name":name,"designation":designation,"employeeid":employeeid,"salary":salary,"phonenumber":phonenumber,"address":address,"pincode":pincode}   
    return dict1
def validate(dict1): 
    valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])  
    valsalary=re.search("[0-9]{0,7}$",dict1["salary"])  
    valpincode=re.search("(^6)[0-9]{5}$",dict1["pincode"])
    if valname and valsalary and valpincode:
        return True
    else:
        return False


    
    


while(1):
    print("1.add employee")
    print("2.view employee")
    print("3.salary as mentioned")
    print("3.exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        n=int(input("Enter the number of employees you want to enter"))
        for i in range(0,n):
            a=addemployee()
            if len(employee_dict)==0:
                employee_dict=collections.ChainMap(a)
            else:
                employee_dict=collections.new_child(a)

    if(choice==2):
        print(employee_dict.maps)

    if(choice==3):
        sal=int(input("Enter the minimum salary:"))
        for i in employeedict.maps:
            if int(i['salary'])>=sal:
                print(i)
    if(choice==4):
        break
        
        


        
            

