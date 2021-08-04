import re
def valiModule(MRP_Date,Expire_Date):
    val = re.search("2021$",MRP_Date)
    val1 = re.search("2021$",Expire_Date)  

    if val and val1:
        return True
    else:
        return False

