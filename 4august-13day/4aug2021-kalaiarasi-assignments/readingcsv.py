import pandas
d=pandas.read_csv('student.csv')
#print(d)
#print(d.Name)
#print(d.head(n=2))
#print(d.tail(n=2))
print(d['Name'])
#print(d.describe())