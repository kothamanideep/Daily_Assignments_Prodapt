import pytz,csv
from validation_Pro import valiModule
from datetime import datetime,time

header = ["Product Name","Description","Prize", "manufacturer","MRP Date","Expire Date","Time and date"]
prdt_list = [ ]

class Product_Details:
    def add_products(self,Prodcut_Name,Description,prize,manufacturer,MRP_Date,Expire_Date):
        self.Prodcut_name = Prodcut_Name
        self.Description=Description
        self.prize=prize
        self.manufacturer = manufacturer
        self.MRP_Date=MRP_Date
        self.Expire_Date =Expire_Date
        details ={"Product Name":Product_Name,"Description":Description,"Prize":prize,
        "manufacturer":manufacturer,"MRP Date":MRP_Date,"Expire Date":Expire_Date,"Time and date":time_date}
        prdt_list.append(details)
        return
    def timeDate(time_zone,td):
        #time1 = time.localtime()
        time_zone = pytz.timezone("Asia/kolkata")
        #current_clock_time = time.strftime("%Y %h-%d %H:%M:%S",time1)
        td = datetime.now(time_zone).strftime("%d-%h-%Y")
        return td

PD = Product_Details()


while(True):
    
    print("1.ADD_PRODUCT_DETAILS")
    print("2.DISPLAY ALL THE PRODUCTS")
    print("3.SEARCH PRODUCT")
    print("4.LIST ALL THE PRODUCTS THAT EXPIRED TODAY")
    print("5.SAVE A FILE")
    print("6.EXIT")
    choice = int(input("enter a choice: "))

    if choice == 1:
        print("Selected to add product details")
        Product_Name = input("enter a name of the product: ")
        Description = input("enter a description: ")
        prize = input("Enter a prize of product: ")
        manufacturer = input("Enter manufacturer Name: ")
        MRP_Date = input("Enter a MRP date: ")
        Expire_Date = input("Enter Expired date: ")
        if valiModule(MRP_Date,Expire_Date)==True:
            time_date =PD.timeDate("td")
        PD.add_products(Product_Name,Description,prize,manufacturer,MRP_Date,Expire_Date)

        
        
    if choice == 2:
        print("List of all the products")
        print(prdt_list)
    if choice == 3:
        print("To search specific product details")
        name = input("enter a product Name: ")
        print(list(filter(lambda i : i ["Product Name"]==name,prdt_list)))

    if choice == 4:
        print("To check a expired product")
        Time = PD.timeDate("td")
        print(list(filter(lambda j : j ["Expire Date"]==Time,prdt_list)))

    if choice == 5:
        with open('Product.csv','w+',encoding='UTF8',newline='') as p:
            writer=csv.DictWriter(p,fieldnames=header)
            writer.writeheader()
            writer.writerows(prdt_list)
    if choice == 6:
        break



