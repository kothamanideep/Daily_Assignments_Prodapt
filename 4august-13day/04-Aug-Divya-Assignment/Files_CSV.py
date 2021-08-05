import csv
headerContent =["name","roll_no"]
studentData = [
    {"name":"divya","roll_no":9},
    {"name":"div","roll_no":10},
    {"name":"ya","roll_no":11},
    {"name":"ayvid","roll_no":8},
]
with open('Students.csv','w+',encoding='UTF8',newline='') as s:
    writer = csv.DictWriter(s,fieldnames=headerContent)
    writer.writeheader()
    writer.writerows(studentData)