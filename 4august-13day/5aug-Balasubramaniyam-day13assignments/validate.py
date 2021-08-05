import re
def validateproduct(date1):
    day=date1.split('-')
    if len(day[2])==4:
        for i in range(1000,2022):
            if int(day[2])==i:
                if len(day[1])==2:
                    for j in range(1,13):
                        if int(day[1])==j:
                            if len(day[0])==2:
                                for z in range(1,32):
                                    if z==int(day[0]):
                                        return True
