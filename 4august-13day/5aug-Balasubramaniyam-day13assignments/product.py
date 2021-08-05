import re,datetime,time,csv
from datetime import date
from validate import validateproduct
productlist=[]
class ProductDetails:
    def addproductdetail(self,pname,description,price,manufacturer,mfd,ed):
        dict1={"pname":pname,"description":description,"price":price,"manufacturer":manufacturer,"mfd":mfd,"ed":ed} 
        productlist.append(dict1)
 
obj1=ProductDetails()   
while True:
    print("1.Add Product")
    print("2.View products")
    print("3.Search a product")
    print("4.List products that expire today")
    print("5.Save") 
    print("6.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        rows=[]
        source="productsource.csv"
        with open(source,'r') as fi:
            data=csv.reader(fi)
            for row in data:
                rows.append(row)
            print(rows)
            length=int(input("Enter the row that we have to add : "))
            for i in range(1,length+1):
                a=rows[i]
                pname=a[0]
                description=a[1]
                price=a[2]
                manufacturer=a[3]
                mfd=a[4]
                ed=a[5]
                if validateproduct(mfd)==True and validateproduct(ed)==True:
                    obj1.addproductdetail(pname,description,price,manufacturer,mfd,ed)

    if choice==2:
        print(productlist)
    if choice==3:
        sname=input("Enter the product name to search : ")
        print(list(filter(lambda i:i["pname"]==sname,productlist)))
    if choice==4:
        current_time=time.localtime()
        tday=time.strftime("%d-%m-%Y",current_time)
        expirylist=(list(filter(lambda i:i["ed"]==tday,productlist)))    
        if len(expirylist)>0:
            print(expirylist)
        else:
            print("No records found")
    if choice==5:
        destination="productdestination.csv"
        headercontent=["pname","description","price","manufacturer","mfd","ed"]
        with open(destination,"a+",encoding="UTF8",newline="") as stdwriter:
            swriting=csv.DictWriter(stdwriter,fieldnames=headercontent)
            swriting.writeheader()
            swriting.writerows(productlist)
    if choice==6:
        break