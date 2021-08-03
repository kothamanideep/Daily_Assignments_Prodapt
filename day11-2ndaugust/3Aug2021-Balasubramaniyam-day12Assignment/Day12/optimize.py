import timeit
# print(timeit.timeit(stmt="a=10; b=5; c=a+b"))
# def printnum():
#     for n in range (1000):
#         pass
# def printwhile():
#     n=0 
#     while(n<=1000):
#         n=n+1
#         pass

# print(timeit.timeit(printnum, number=10000))
# print (timeit.timeit (printwhile, number=10000))
mylist=[23,56,3,4,7,8,63,45,9,11,23,45,5]

def f1():

    filter(9,mylist)

def f2():
    for i in mylist:
        if (i==9):
            pass

print(timeit.timeit(f1, number=10000))

print (timeit.timeit(f2, number=10000))
