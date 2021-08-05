from datetime import date
import time,csv
productlist=[]
Header = ["prodname","desc","price","manufacturer","manufactdate","expdate","purchased_time"]

class Products:
    def addProducts(self,prodname,desc,price,manufacturer,manufactdate,expdate):
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict3={"prodname":prodname,"desc":desc,"price":price,"manufacturer":manufacturer,"manufactdate":manufactdate,"expdate":expdate,"purchased_time":current_local_time}
        productlist.append(dict3)

obj1=Products()


while(True):
    print("1. Add products")
    print("2. view products")
    print("3. search product by name")
    print("4. List product which expire today")
    print("5. Create a CSV file of input data")
    print("6. exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
            prodname=input("Enter product name: ")
            price=input("Enter product price: ")
            desc=input("Enter product description: ")
            manufacturer=input("enter product manufacturer: ")
            manufactdate=input("enter manufacture date: ")
            expdate=input("Enter expiry date: ")
            obj1.addProducts(prodname,desc,price,manufacturer,manufactdate,expdate)
            

    if choice==2:
        print(productlist)
    if choice==3:
        search=input("Enter name to search product: ")
        print(list(filter(lambda x:x["prodname"]==search,productlist)))
    if choice==4:
        today=date.today()
        a=today.strftime("%d/%m/%Y")
        print(list(filter(lambda i:i["expdate"]==str(a),productlist)))
    if choice == 5:
        with open("ProductsList.csv",'w+',encoding='UTF8',newline ="") as p:
            writer = csv.DictWriter(p,fieldnames=Header)
            writer.writeheader()
            writer.writerows(productlist)        
    if choice==6:
        break