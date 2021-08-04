import datetime,time
from datetime import date
product_list=[]
class ProductDetails:
    def init(self,pname,description,price,manufucturer,mfd,efd):
        self.pname=pname
        self.description=description
        self.price=price
        self.manufacturer=manufacturer
        self.mfd=mfd
        self.efd=efd
        def validate(dict1):
             valpname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["pname"])
             valdescription=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",dict1["description"])
             valprice=re.search("[1-9]{1}[1-9]{2,7}$",dict1["price"])
             valmanufacturer=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",dict1["manufacturer"])
             valmfd=re.search("^(?:[0-9]{2})?[0-9]{2}-(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])$",dict1["mfd"])
             valed=re.search("^(?:[0-9]{2})?[0-9]{2}-(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])$",dict1["efd"])
             if valname and valsalary and valpincode:
                 return True
             else:
                 return False       

           
       
        
       
    def addproductdetail(self,pname,description,price,manufucturer,mfd,efd):
        
        dict1={"pname":pname,"description":description,"price":price,"manufacturer":manufacturer,"mfd":mfd,"efd":efd} 
        product_list.append(dict1)
obj1=ProductDetails()    
today=datetime.date.today()
while True:
    print("1.Add Product")
    print("2.View products")
    print("3.Search a product")
    print("4.List products that expire today")
    print("5.exit") 
    choice=int(input("Enter your choice : "))
    
    if choice==1:
      pname=input("Enter the  name of the product : ")
      description=input("Enter the Description of a product: ")
      price=int(input("Enter the Price of product in rupees : "))
      manufacturer=input("Enter the manufacturer name : ")
      mfd=input("Enter the manufacturing date : ")
      efd=input("Enter the expiry date   YYYY-MM-DD : ")
    
      obj1.addproductdetail(pname,description,price,manufacturer,mfd,efd)
    if choice==2:
        print(product_list)
    if choice==3:
        sname=input("Enter the product name to search : ")
        print(list(filter(lambda i:i["pname"]==sname,product_list)))
    if choice==4:
 
        exp=datetime.date(efd)
        # ed=time.strftime("%d-%m-%y")
        today=datetime.date.today()
        if(exp==today):
            print(product_list)
        else:
            print("No products")    
    if choice==5:
        break