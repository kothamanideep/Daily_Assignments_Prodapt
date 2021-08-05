import time
import re ,csv
from datetime import date

productlist=[]
productheadercontent=["proname","prodescp","proprice","pmanufacture","manufactdate","expdate","purchased_time"]

class Products_Details:
    def addProducts(self,proname,prodes,proprice,pmanufacture,manufactdate,expdate):
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict1={"proname":proname,"prodescp":prodes,"proprice":proprice,"pmanufacture":pmanufacture,"manufactdate":manufactdate,"expdate":expdate,"purchased_time":current_local_time}
        productlist.append(dict1)
pro=Products_Details()

###################validation function
def validation_of_product(pname,pprice,desp):
    valid=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",pname)
    valid2=re.match("[0-9]{0,7}$",pprice)
    valid3=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",desp)
    
    if valid and valid2 and valid3:
        return True
    else:
        return False

################## menu
while(True):
    print("1. Add products")
    print("2. View products")
    print("3. Search product by name")
    print("4. Product which expire today")
    print("5. Generating product in csv files")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        while(True):
            proname=input("enter product name: ")
            proprice=input("Enter product price: ")
            prodescp=input("Enter product description: ")
            if validation_of_product(proname,proprice,prodescp):
                
                promanufacture=input("Enter product manufacturer: ")
                manufactdate=input("Enter manufacture date: ")
                expdate=input("Enter expiry date: ")
                pro.addProducts(proname,prodescp,proprice,promanufacture,manufactdate,expdate)
            else:
                print("Please Try again by entering valid name , price and description")
                continue
            break

    if choice==2:
        print(productlist)
    if choice==3:
        searchitem=input("Enter name to search product: ")
        print(list(filter(lambda a:a["proname"]==searchitem,productlist)))
    if choice==4:
        today=date.today()
        d=today.strftime("%d/%m/%Y")
        print(list(filter(lambda i:i["expdate"]==str(d),productlist)))     

    if choice==5:
        with open("product.csv","w+",encoding="UTF8",newline="") as s:
            writer=csv.DictWriter(s,fieldnames=productheadercontent)
            writer.writeheader()
            writer.writerows(productlist)  
    if choice==6:
        break
    
