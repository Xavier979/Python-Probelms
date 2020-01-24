import sys
import time


# Define the function to take one arguments.
# In this problem you have to define the steps of the solution. 
def getprime(n):
        prime=[]
        for i in range(2, n+1):
            j = 2
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                prime.append(i)
        return prime

def countnumbers(n):
    count=0
    temp=(n)**0.5
    primes=getprime(int(temp))

    for x in primes:
        if pow(x,2)<n:
            for y in primes:
                if pow(x,2)+pow(y,3)<n:
                    for z in primes:
                        temp = pow(x,2) + pow(y,3) + pow(z,4)
                        if temp <= n:
                            count +=1
    return(count)


# Enter the input number from console
n = int(input("Enter number :"))

# Print the output of your function
start_time = time.time()
print(countnumbers(n))
print("Duration: %s seconds" % (time.time() - start_time))