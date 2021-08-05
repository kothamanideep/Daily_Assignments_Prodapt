import collections
import re,csv
headerContent= ['Emp_name','Emp_id','Designation','Salary','Address','Mob_no','Pincode']
Emp_list=[]

# -----Function to add employee-----
def addEmployee():
    Emp_name=(input("Enter Employee Name: "))
    Emp_id=(input("Enter Employee ID: "))
    Designation=(input("Enter the Employee Designation: "))
    Salary=(input("Enter Employee salary: "))
    Address=(input("Enter Employee address: "))
    Mob_no=(input("Enter Employee mobile number: "))
    Pincode=(input("Enter the pincode: "))
    dict1={"Emp_name":Emp_name,"Emp_id":Emp_id,"Designation":Designation,"Salary":Salary,"Address":Address,"Mob_no":Mob_no,"Pincode":Pincode}
    Emp_list.append(dict1)

#-------Validation function------
def validation(dict1):
    # valname=re.search("[A-Z]{1}[A-Za-z]{0,25}$",dict1["name"])
    # valsalary=re.search("[0-9]{0,7}$",dict1["salary"])
    valpincode=re.search("[0-9]{6}$",dict1["pincode"])
    valemp_name=re.match("[A-Za-z]$",dict1["Emp_name"])
    valsalary=re.search("[0-9]{0,8}$",dict1["Salary"])
    valmob_no=re.search("[6-9]{1}[0-9]{9}$",dict1["Mob_no"])
    if valsalary and valpincode and valmob_no:
        return True
    else:
        return False


# -----Menu------
while(True):
    print("1.Add Employee")
    print("2.View Employee")
    print("3.Salary check")
    print("4.Save employee details to a file")
    print("5.Exit")
    choice=(int(input("Enter your response: ")))
    if choice == 1:
        addEmployee=addEmployee()
        if validation(addEmployee):
            if len(Emp_list)==0:
                Emp_list=collections.ChainMap(addEmployee)
            else:
                Emp_list=Emp_list.new_child(addEmployee)

    if choice == 2:
        print("Employee details")
        print(Emp_list.maps)
    if choice==3:
        Sal=int(input("Enter the salary to check: "))
        Salarylist=[i for i in Emp_list.maps if int(i['Salary'])>Sal]
        for i in Salarylist:
            print(i)
    if choice == 4:
        with open('Employee.csv','w+', encoding='UTF8',newline='') as s:
            writer=csv.DictWriter(s,fieldnames=headerContent)
            writer.writeheader()
            writer.writerows(Emp_list)
    if choice==5:
        print("Exit from the menu")
        break