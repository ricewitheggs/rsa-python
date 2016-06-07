import random

__all__=['getPrime','are_relativelyPrime']

def gcd(p,q):
    """Returns the greatest common divisor of p and q"""
    while q!=0:
        (p,q)=(q,p%q)
    return p

def egcd(p,q):
    if q==0:
        return p,1,0
    else:
        g,x,y=egcd(q,p%q)
        return g,y,x-p/q*y

def are_relativelyPrime(p,q):
    """Returns True if p and q are relatively prime,and False if not"""
    result=gcd(p,q)
    return result==1

def getPrime():
    """Generate enough big prime"""
    maxsize=pow(2,64)
    minsize=pow(10,10)
    while True:
        integer=random.randrange(minsize,maxsize,1)
        if is_prime(integer):
            return integer


def millerRabinPrimaltyTesting(n,k):
    """Test n for primalty with Miller-Rabin algorithm in k rounds"""
    if n<2:
        return False
    d=n-1
    r=0
    while not (d & 1):
        r+=1
        d>>=1
    for _ in range(k):
        a=random.randint(2,n-1)
        x=pow(a,d,n)
        if x==1 or x==n-1:
            continue
        for _ in range(r-1):
            x=pow(x,2,n)
            if x==1:
                return False
            if x==n-1:
                break
        else:
            return False
    return True

def is_prime(number):
    """Test number for primalty"""
    if number<10:
        return number in [2,3,5,7]
    if not (number & 1):
        return False
    return millerRabinPrimaltyTesting(number,16)
