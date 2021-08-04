import pandas 
d=pandas.read_csv("student.csv")
print(d.to_string())
print(d.describe())
# print(d.tail(n=3))
# print(d.head(n=3))