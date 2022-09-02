import math
def solution(i):
    primeNumbers =""
    n = 1
    while i+5 > len(primeNumbers):
        primeCheckNumber = 2
        
        if n > 1:
            isPrime = True
        else:
            isPrime = False
            
        while primeCheckNumber < n:
            if (n % primeCheckNumber == 0):
                isPrime = False
                break
            primeCheckNumber +=1  
    
        primeCheckNumber +=1
        if  isPrime:
            primeNumbers += str(n)
        n +=1
    print(primeNumbers[i:i+5])
    
    return primeNumbers[i:i+5]
