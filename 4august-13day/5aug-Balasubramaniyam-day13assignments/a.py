import csv
source="studentsource.csv"
rows=[]

with open(source,'r') as fi:
    data=csv.reader(fi)
    for row in data:
        rows.append(row)
print(rows)
for i in range(1,len(rows)):
    a=rows[i]
    name=a[0]
    rollno=a[1]
    admino=a[2]
    english=a[3]
    tamil=a[4]
    maths=a[5]
    science=a[6]
    social=a[7]
    dict1={'name':name,'rollno':rollno,'admino':admino,'english':english,'tamil':tamil,'maths':maths,'science':science,'social':social}
    print(dict1)

