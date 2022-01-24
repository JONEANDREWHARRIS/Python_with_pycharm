# x = 29
# for i in range(2,x):
#     if x % i ==0:
#          print('not prime')
#          break
# else:
#         print("prime")
import time #the Googled way
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p]== True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1
    c =0
    for p in range(2,n):
        if prime[p]:
            c +=1
    return c
t0 = time.time()
c = SieveOfEratosthenes(100000)
print("total prime nuumbers in range:", c)
t1 =time.time()
print('time required: ', t1 -t0)
