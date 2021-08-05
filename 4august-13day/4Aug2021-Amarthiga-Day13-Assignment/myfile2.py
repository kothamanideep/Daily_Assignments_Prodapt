#how to create a file and store it
import csv

header=["MovieName","ReleasedYear"]
MovieDetails = [
    {"MovieName":"Twilight", "ReleasedYear":2017},
    {"MovieName":"Avengers", "ReleasedYear":2019},
    {"MovieName":"Wonder Woman", "ReleasedYear":2020},
    {"MovieName":"Avatar", "ReleasedYear":2010}
]

with open("movie.csv","w+", encoding='UTF8',newline='')as s:         #UTF8 - typical character encoding method
    writer=csv.DictWriter(s,header)
    writer.writeheader()
    writer.writerows(MovieDetails)

