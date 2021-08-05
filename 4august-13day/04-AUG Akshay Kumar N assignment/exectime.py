import timeit
list1 = [28,98,6,32,51,48,22,16,82,19,44,8,91,77,15,36,79,72,64,25]

def sort():
    sorted(list1)

def iSort():
    length=len(list1)
    for i in range(1,length):              
        item=list1[i]
        j=i-1
        while(j>=0 and list1[j]>item):
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=item
    pass    



print(timeit.timeit(sort,number=100000))
print(timeit.timeit(iSort,number=100000))
