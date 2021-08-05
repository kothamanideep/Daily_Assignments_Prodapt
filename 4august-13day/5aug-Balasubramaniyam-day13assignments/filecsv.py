########CSV
import csv
headerContent=["Name","Roll"]
studentData=[
    {"Name":"Tamil","Roll":1},
    {"Name":"Sharmi","Roll":2},
    {"Name":"Sona","Roll":3},
    {"Name":"Surya","Roll":4},
    {"Name":"Swe","Roll":5},
    {"Name":"Selva","Roll":6},
    {"Name":"Malu","Roll":7},
]
with open("student.csv","w+",encoding="UTF8",newline="") as s:
    writer=csv.DictWriter(s,fieldnames=headerContent)
    writer.writeheader()
    writer.writerows(studentData)