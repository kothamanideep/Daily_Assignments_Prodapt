from datetime import datetime
import time
import re
import csv
header=['productname','description','price','manufracturingdate','expirydate']
productlist=[]
class ProductDetails:
    def addproductdetails(self,productname,description,price,manufracturingdate,expirydate):
        
        dict1={"productname":productname,"description":description,"price":price,"manufracturingdate":manufracturingdate,"expirydate":expirydate,}
        productlist.append(dict1)
obj1=ProductDetails()
def validate(productname,price):
    valproductname=re.search("[A-Z]{1}[^A-Z]{0,25}$",productname)
    valprice=re.search("[0-9]{0,7}$",price)
    if valproductname and valprice:
        return True
    else:
        return False
while(True):
    print("1.Add products:")
    print("2.view all products:")
    print("3.Search a product:")
    print("4.list all products expire today:")
    print("5.header")
    print("6.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        while(True):
            product_name=input("enter the product name:")
            price_=input("enter price :")
            if validate(product_name,price_):
                description=input("enter description:")
                manufracturingdate=str(input("Enter mfdate(yyyy-mm-dd):"))
                print(datetime.strptime(manufracturingdate, "%Y-%m-%d"))
                expirydate=str(input("enter epdate(mm-dd-yyyy):"))
                print(datetime.strptime(expirydate, "%m-%d-%Y"))
                obj1.addproductdetails(product_name,description,price_,manufracturingdate,expirydate)
            else:
                print("Please  entered valid product name and price")
                continue
            break
    if choice==2:
        print(productlist)
    if choice==3:
        sproduct=input("enter your product to search:")
        print(list(filter(lambda i:i["productname"]==sproduct,productlist)))
    if choice==4:
        local_current_time=time.localtime()
        find_date=time.strftime("%m-%d-%Y",local_current_time)
        expire=(list(filter(lambda i:i["expirydate"]==find_date,productlist)))
        print(expire)
    if choice==5:
        with open('student1.csv','w+',encoding="UTF8",newline='') as s:
           writer=csv.DictWriter(s,fieldnames=header)
           writer.writeheader()
           writer.writerows(productlist)
    if choice==6:
        break