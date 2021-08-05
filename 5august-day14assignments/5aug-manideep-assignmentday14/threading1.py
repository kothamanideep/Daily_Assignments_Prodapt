import threading,time
a=int(input("enter a number:"))
b=int(input("enter end number:"))
def prime():
    for i in range(a,b+1):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
                else:
                    print(i,end=" ") 
                    break
def palindrome():
    for n in range(a,b+1):
        temp = n
        rev = 0
    
        while(temp > 0):
            Remainder = temp % 10
            rev = (rev * 10) + Remainder
            temp = temp //10

        if(n == rev):
            print(n,end=" ")
            
t1=threading.Thread(target=prime)
t2=threading.Thread(target=palindrome)   #create a thread
t1.start()
t2.start()  

       

    
            


