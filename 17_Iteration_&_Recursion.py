
import time

def fact_iterative(n):
    facto=1
    if(n==0):
        # print("Factorial of 0 is 1")
        return 1
    else:
        for i in range(1,n+1):
            facto=facto*i
        return facto
        # print("Factorial of ",n," is :",facto )
        
def fact_recursive(n):
    
    if(n==0):
        # print("Factorial of 0 is 1")
        return 1
    else:
         
        return n*fact_recursive(n-1)
        # print("Factorial of ",n," is :",facto )


start_time1=time.time()

for i in range(5,1000,5):
    f1=fact_iterative(i)

end_time1=time.time()

time1=end_time1-start_time1
print("Time for iterative :",time1)


start_time2=time.time()

for i in range(5,1000,5):
    f1=fact_recursive(i)

end_time2=time.time()

time2=end_time2-start_time2
print("\nTime for recurtion :",time2)

time1=str(time1)
time2=str(time2)

f=open("Myfirstfile.txt",'w')
f.write("Execution time for Iterative method "+time1)
f.write("Execution time for recurtion method "+time2)
f.close()