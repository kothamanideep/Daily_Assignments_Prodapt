import re,datetime,time
from datetime import date
productlist=[]
class ProductDetails:
    def addproductdetail(self,pname,description,price,manufacturer,mfd,ed):
        dict1={"pname":pname,"description":description,"price":price,"manufacturer":manufacturer,"mfd":mfd,"ed":ed} 
        productlist.append(dict1)
 
def validate(date1):
    day=date1.split('-')
    if len(day[0])==4:
        for i in range(1000,2022):
            if int(day[0])==i:
                if len(day[1])==2:
                    for j in range(1,13):
                        if int(day[1])==j:
                            if len(day[2])==2:
                                for z in range(1,32):
                                    if z==int(day[2]):
                                        return True
obj1=ProductDetails()   
while True:
    print("1.Add Product")
    print("2.View products")
    print("3.Search a product")
    print("4.List products that expire today")
    print("5.exit") 
    choice=int(input("Enter your choice : "))
    if choice==1:
      pname=input("Enter the Product name : ")
      description=input("Enter the Description : ")
      price=int(input("Enter the Price : "))
      manufacturer=input("Enter the manufacturer name : ")
      mfd=input("Enter the manufacturing date YYYY-MM-DD: ")
      ed=input("Enter the expiry date   YYYY-MM-DD : ")
      if validate(mfd)==True and validate(ed)==True:
          obj1.addproductdetail(pname,description,price,manufacturer,mfd,ed)
    if choice==2:
        print(productlist)
    if choice==3:
        sname=input("Enter the product name to search : ")
        print(list(filter(lambda i:i["pname"]==sname,productlist)))
    if choice==4:
        current_time=time.localtime()
        tday=time.strftime("%Y-%m-%d",current_time)
        expirylist=(list(filter(lambda i:i["ed"]==tday,productlist)))    
        if len(expirylist)>0:
            print(expirylist)
        else:
            print("No records found")
    if choice==5:
        break