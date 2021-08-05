import csv,re
bookslist=[]
Header = ["title","description","price","publisher","distributor"]
class bookDetails:
    def AddBook(self,title,description,price,publisher,distributor):
        dict2={"title":title,"description":description,"price":price,"publisher":publisher,"distributor":distributor}
        bookslist.append(dict2)
obj1=bookDetails()

def val_book(title,price):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",title)
    val2=re.match("[0-9]{0,7}$",price)
    if val1 and val2:
        return True
    else:
        return False



while(True):
    print("1. add book ")
    print("2. view book ")
    print("3. View all books in alphabetical order  ")
    print("4. search a book using title")
    print("5. To create CSV File")
    print("6. Exit")
    choice=int(input("Enter a choice: "))
    if choice==1:
            while(True):
            
                title=input("Enter title of book: ")
                price=input("Enter price of book: ")
                if val_book(title,price):
                    title=input("Enter title of book: ")
                    description=input("Enter description of book: ")
                    price=input("Enter price of book: ")
                    distributor=input("Enter distributor of book: ")
                    publisher=input("Enter publisher of book: ")
                
                    obj1.AddBook(title,description,price,publisher,distributor)
                else:
                    print("Please enter valid data ")
                    continue
                break    
                
    if choice==2:
        print(bookslist)
    if choice==3:
        print(sorted(bookslist,key=lambda i:i["title"]))
    if choice==4:
        search=input("Enter title to search product: ")
        print(list(filter(lambda a:a["title"]==search,bookslist)))
    if choice == 5:
        with open("Books.csv", 'w+', encoding='UTF8', newline="") as b:

            writer = csv.DictWriter(b, fieldnames=Header)
            writer.writeheader()
            writer.writerows(bookslist)    
    if choice==6:
        break