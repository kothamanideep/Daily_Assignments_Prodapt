import re
import time
import csv
try:
    headercontent=["name","description","price","manufactdate","expirydate"]
    productlist=[]
    class Productdetail:

        def addproductdetail(self,name,description,price,manufactdate,expirydate):
            vname=re.search("^[A-Za-z]{2,25}$",name)
            m=re.search("^[0-9]{2}\s[0-9]{2}\s[0-9]{4}",manufactdate)
            e=re.search("^[0-9]{2}\s[0-9]{2}\s[0-9]{4}",expirydate)
            if vname and m and e:
                dict1={"name":name,"description":description,"price":price,"manufactdate":manufactdate,"expirydate":expirydate}
                productlist.append(dict1)
            else:
                print("invalid")

    obj1=Productdetail()
    while(True):
        print("1. add product")
        print("2. view all product")
        print("3. search a product name")
        print("4. list all product that expired today:")
        print("5. save to file")
        print("6. exit")
        print("\n")
        choice=int(input("enter ur choice:"))
        
        if choice==1:
            name=input("enter your name:")
            manufactdate=input("enter manufdate in format date month year :")
            expirydate=input("enter expirydate in format date month year:")
            price=int(input("enter the price:"))
            description=input("enter your description:")
            obj1.addproductdetail(name,description,price,manufactdate,expirydate)
            
        if choice==2:

            print(productlist)
        
        if choice==3:
            searchpro=input("enter your product name:")
            print(list(filter(lambda i:i["name"]==searchpro,productlist)))
        
        if choice==4:
            
            currenttime=time.localtime()
            currentclock=time.strftime("%d %m %Y",currenttime)
            print(list(filter(lambda i: i["expirydate"]==currentclock,productlist)))
        
        if choice==5:
            with open('product.csv','w+',encoding='UTF8',newline='') as s:
                writer=csv.DictWriter(s,fieldnames=headercontent)
                writer.writeheader()
                writer.writerows(productlist)

        if choice==6:
            break
except:
    print("please enter the correct details")

