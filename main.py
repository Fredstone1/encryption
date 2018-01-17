from math import floor
import math
import random
import time
import sympy

def txt2ascii(txt):
    converted = [ord(i) for i in txt]
    return converted;

def ascii2txt(converted):
    txt = ''.join(chr(i) for i in converted)
    return txt;

def sfd(prime1, prime2):
    while prime2 != 0:
        temp = prime2
        prime2 = prime1 % prime2
        prime1 = temp
    return prime1;

def phiCalc(prime1, prime2):
    phi = (prime1 - 1) * (prime2 - 1)
    return phi;

def relativPrime(phi):
    fundetPrime = False
    while fundetPrime == False:
       e = random.randint((phi//2)+1,phi)
       if sfd(phi,e) == 1:
           fundetPrime = True
    return e;

def EUA(phi, e):
    r, s, t = [], [], []
    r.append(phi), s.append(1), t.append(0)
    r.append(e), s.append(0), t.append(1)
    k = 2
    while r[-1] != 0:
        q = floor(r[k - 2] / r[k - 1])
        r.append(r[k - 2] - q * r[k - 1]), s.append(s[k - 2] - q * s[k - 1]), t.append(t[k - 2] - q * t[k - 1])
        k += 1
    d = t[-1] + t[-2]
    return d;

def check(phi, e, d):
    checking = False
    while checking == False:
        if d < 0:
            e = relativPrime(phi)
            d = EUA(phi, e)
        else:
            checking = True
    return d, e;

def encrypt(n, e, plaintext):
    ciphertext = []
    for i in plaintext:
        ciphertext.append(pow(i, e, n))
    return ciphertext;

def decrypt(n, d, ciphertext):
    plaintext = []
    for i in ciphertext:
        plaintext.append(pow(i, d, n))
    return plaintext;

def MillerRabin(n, t):
    #Two interation factors
    s = 0
    r = n-1
    run = True
    while run:
        if r % 2 == 0:
            s += 1
            r //= 2
        else:
            run = False
    for i in range(1,t):
        a = random.randint(2,n-2)
        y = pow(a,r,n)
        if y != 1 and y != n-1:
            j = 1
            while j <= s-1 and y != n-1:
                y = pow(y,2,n)
                if y == 1:
                    return False
                j += 1
            if y != n-1:
                return False
    return True


def expBySqua(number, exponent):
    if exponent < 0:
        number = 1 // exponent
    if exponent == 0:
        return 0
    temp = 1
    while exponent > 1:
        if exponent%2 == 0:
            number = number * number
            exponent = exponent // 2
        else:
            temp = number * temp
            number = number * number
            exponent = (exponent - 1) // 2
    return number * temp


def primeGenerator():
    primeArr = []
    while len(primeArr) < 2:
        prime = random.randint(expBySqua(2, 300), expBySqua(2, 800))
        if MillerRabin(prime, 10) == True:
            primeArr.append(prime)

    p = primeArr[0]
    q = primeArr[1]
    if primeArr[1] > primeArr[0]:
        p = primeArr[1]
        q = primeArr[0]
    return p, q

#----------------------------------------------------------------------------#

p, q = primeGenerator()
plaintext = [17]
n = p*q
phi = phiCalc(p,q)
e = relativPrime(phi)
d = EUA(phi,e)
d, e = check(phi, e, d)
print("Plaintext = ", plaintext)
print("PublicKey = ", e)
print("PrivateKey = ", d)
enc = encrypt(n,e, plaintext)
print("Encryption = ", enc)
print("Decryption = ", decrypt(n,d,enc))

