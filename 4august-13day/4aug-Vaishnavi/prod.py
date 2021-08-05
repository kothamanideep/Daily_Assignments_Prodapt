import re,sys,time,csv
header=['product_name','product_desc','product_price','product_manufacture','product_manufacturedate','product_expiry','Addon']
product_list=[]
class Details_Of_Products:
    def addProduct(self,product_name,product_desc,product_price,product_manufacture,product_manufacturedate,product_expiry):
        date_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
        dict1={'product_name':product_name,'product_desc':product_desc,'product_price':product_price,'product_manufacture':product_manufacture,'product_manufacturedate': product_manufacturedate,'product_expiry':product_expiry,'Addon':date_time} 
        product_list.append(dict1)
obj1=Details_Of_Products()
def product(product_name,product_price,product_description):
    val=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",product_name)
    val2=re.match("[0-9]{0-7}$",product_price)
    val3=re.match("([a-z]+)([a-z]+)*$",product_description)

    if val and val2 and val3:
        return True
    else:
        print("Incorrect input")
        sys.exit()

while(True):
    print("1. Add product :")
    print("2. view product :")
    print("3. search product :")
    print("4. expiry product :")
    print("5. save product :")
    print("6. exit :")
    choice=int(input("Enter your choice :"))
    if choice==1:
        
        product_name=input("Enter a product name :")
        product_price=input("Enter a product price :")
        product_description=input("Enter a product description :")
        product_manufacture=input("Enter product manufactures :")
        manufacture_date=input("Enter manufacture date :")
        product_expiry=input("Enter expiry date :")
        # obj1.addProduct(product_name,product_description,product_price,manufacture_date,product_expiry)
        
    if choice==2:
        print(product_list)
    if choice==3:
        search_product=input("Enter name to search product :")
        print(list(filter(lambda i:i["product_name"]==search_product,product_list)))
    if choice==4:
        today=date.today()
        date=today.strftime("%d-%m-%Y")
        print(list(filter(lambda i:i["expiry_date"]==str(date),product_list)))
    if choice==5:
        with open('product.csv','w+',encoding='UTF8',newline='')as s:
            writer=csv.DictWriter(s,fieldnames=header)
            writer.writeheader()
            writer.writerows(product_list)

    if choice==6:
        sys.exit()