from Crypto.PublicKey import RSA
import random


def genRSA(bits=1024):

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
    return privKeyObj, pubKeyObj, n, e, d

m0 = 11111111
m1 = 22222222
priv,pub,n,e,d=genRSA()
priv2,pub2,n,e,d=genRSA()
x0 = random.randint(15000, 150000)
x1 = random.randint(15000, 150000)
x=[x0,x1]
k = random.randint(0, n)

def Rob(x, pub, n, e):
    b = random.randint(0, 1)
    k1=pub.encrypt(k,'x')[0]
    v=(x[b]+ k1)%n
    Arya2(v)

def Arya1():
    Rob(x,pub,n,e)

def Arya2(v):
    k0=priv.decrypt(v-x[0])
    k1=priv.decrypt(v-x[1])
    m00=k0+m0
    m11=k1+m1
    Rob2(m00,m11)

def Rob2(m00,m11):
    print(m00-k)
    print(m11-k)

Arya1()
