import re
def valiModule(MRP_Date,Expire_Date):
    val = re.search("^[0-9]-+[A-z]-+[21]$",MRP_Date)
    val1 = re.search("^[0-9]-+[A-z]-+[21]$",Expire_Date)  

    if val and val1:
        return True
    else:
        return False