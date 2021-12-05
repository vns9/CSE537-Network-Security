from Crypto.PublicKey import RSA
from random import randint

new_key = RSA.generate(1024)
n=new_key.n
#n=5555555555555555555555555555555555555555555555555555555555555555
g=randint(1,n)
x=randint(1,n)
p=new_key.p

y=pow(g,x,p)
known=False

ra=randint(0,1)
c=0
def peg(r):
    global c
    if known:
        c=pow(g,r,p)
        r1=vic1(c)
        if r1==0:
            return vic2(r)
        else:
            return vic2((x+r)%(p-1))
    else:
        rin=randint(0,1)
        if rin==0:
            yin=modInverse(y,p)
            cfac=pow(g,r,p)
            yin=pow(yin,1,p)
            c=(cfac*yin)%p

        else:
            c=pow(g,r,p)
        r1 = vic1(c)
        return vic2(r)


def vic1(c):
    return ra


def vic2(r2):
    ck = pow(g, r2, p)
    print(ck)
    print(c)
    if ra==0:
        if c==ck:
            return 1
        else:
            return 0
    else:
        if (c*y)%p==ck%p:
            return 1
        else:
            return 0


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

i=0
while 1:
    r = randint(1, n)
    if peg(r)==0:
        break
    i+=1
    if   i==100:
        break
print("No. of successful rounds =" + str(i))
