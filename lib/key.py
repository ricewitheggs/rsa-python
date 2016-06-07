from prime import getPrime,are_relativelyPrime,egcd
import random

def genKey(efile,dfile,nfile):
    if not efile:
        efile='keys/e.txt'
    if not dfile:
        dfile='keys/d.txt'
    if not nfile:
        nfile='keys/n.txt'
    (p,q)=genPAndQ()
    n=p*q
    with open(nfile,'w') as f:
        f.write(str(hex(n))[2:-1])
    phiN=(p-1)*(q-1)
    while True:
        e=random.randint(2,phiN)
        if are_relativelyPrime(e,phiN):
            break
    with open(efile,'w') as f:
        f.write(str(hex(e))[2:-1])
    d=egcd(e,phiN)[1]%phiN
    with open(dfile,'w') as f:
        f.write(str(hex(d))[2:-1])
    print 'Generating keys...'
    print 'Private key:'
    print '	d:',d,'\n	n:',n
    print 'Public key:'
    print '	e:',e,'\n	n:',n
    return {'p':p,'q':q,'n':n,'e':e,'d':d}

def genPAndQ():
    p=getPrime()
    while True:
        q=getPrime()
        if p!=q:
            with open('keys/p.txt','w') as f:
                f.write(str(hex(p))[2:-1])
            with open('keys/q.txt','w') as f:
                f.write(str(hex(q))[2:-1])
            return (p,q)
