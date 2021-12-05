from Crypto.PublicKey import RSA
import random


def generate_RSA(bits=1024):

    new_key = RSA.generate(bits)
    p=new_key.p
    q=new_key.q
    n=p*q
    e= new_key.e
    d= new_key.d
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    pubKeyObj = RSA.importKey(public_key)
    privKeyObj = RSA.importKey(private_key)
    return privKeyObj, pubKeyObj, n, e, d, p,q

priv,pub,n,e,d,p,q=generate_RSA()
# p=7
# q=11
# n=77
# e=11

xr = random.randint(1, n-1)

m=2345
me=pub.encrypt(m, 'x')[0]


def modInverse(a, m1):
    m0 = m1
    y = 0
    x = 1

    if (m1 == 1):
        return 0

    while (a > 1):
        # q is quotient
        q1 = a // m1

        t = m1

        # m is remainder now, process
        # same as Euclid's algo
        m1 = a % m1
        a = t
        t = y

        # Update x and y
        y = x - q1 * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x

def gcdExtended(a, b):
    # Base Case
    if a == 0:
        x = 0
        y = 1
        return b,x,y

    # To store results of recursive call
    gcd,x1,y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b / a) * x1
    y = x1

    return gcd,x,y

def send():

    rec(n,e,me)

def rec(n,e,me):

    x1=pow(xr,2,n)
    print(x1)
    #print xr
    send2(x1)

def send2(x1):
    p1=p//4
    q1=q//4
    mp = pow(x1, p1+1, p)
    mp=p-mp
    mq = pow(x1, q1+1, q)
    gcd, yp,yq=gcdExtended(p, q)
    print(gcd,mp,yp,mq,yq)
    r=(yp*p*mq+yq*q*mp)%n
    r1=n-r
    s = (yp * p * mq - yq * q * mp) % n
    s1=n-s
    ro=[r,r1,s,s1]

    ri=random.randint(0,3)
    #rec2(ro[ri])
    print(r)
    #print(r1)
    #print(s)
    #print(s1)
    #print xr

def rec2(r):
    if r==xr or r==-1*xr:
        print("CBD")
        return
    xa=abs(r-xr)
    p1,a1,a2=gcdExtended(xa,n)
    q1=n/p1
    ph=(p1-1)*(q1-1)
    print(p1)
    print(p)
    print(q1)
    print(q)
    d1=modInverse(e,ph)
    md=pow(me,d1,n)
    print(md)
send()
