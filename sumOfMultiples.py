import time


def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
def getlcm(n,m):
    return n * m /  gcd(n,m)

# Define the function to take three arguments.
def sumOfMultiples(p, q, n):
    list_p=[]
    list_q=[]
    intersection=[]
    total=0
    lcm=0

    n_p=int((n-1)/p)
    n_q=int((n-1)/q)
    Sn_p=3*n_p+(3*n_p*(n_p-1))/2
    Sn_q=5*n_q+(5*n_q*(n_q-1))/2
    lcm=getlcm(p,q)
    n_lcm=int((n-1)/lcm)
    Sn_lcm=15*n_lcm+(15*n_lcm*(n_lcm-1))/2
    total=Sn_p+Sn_q-Sn_lcm
    return int(total)

# Print the output of your function for p=3, q=5, n=10.
start_time = time.time()
print(sumOfMultiples(3, 5, 10))
print("Duration: %s seconds" % (time.time() - start_time))

# Print the output of your function for p=3, q=5, n=10000.
start_time = time.time()
print(sumOfMultiples(3, 5, 10000))
print("Duration: %s seconds" % (time.time() - start_time))

# Print the output of your function for p=3, q=5, n=10000000.
start_time = time.time()
print(sumOfMultiples(3, 5, 100000000))
print("Duration: %s seconds" % (time.time() - start_time))