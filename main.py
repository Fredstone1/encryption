import numpy as np
import random
import math
from fractions import gcd
import csv
import time


def sfd(prime1,prime2):
    while prime2 != 0:
        temp = prime2
        prime2 = prime1 % prime2
        prime1 = temp
    return prime1;


def phiCalc(prime1,prime2):
    phi = abs((prime1-1)*(prime2-1))/sfd(prime1-1,prime2-1)
    return phi;

def findPrime():



def relativPrime(phi):
    fundetPrime = False
    while fundetPrime == False:
        e = random.randint(100000000000000,1000000000000000000000)
        if sfd(phi,e) == 1:
            fundetPrime = True
            return e;

def EUA(phi, e):
    r, s, t = [], [], []
    r.append(phi), s.append(1), t.append(0)
    r.append(e), s.append(0), t.append(1)
    k = 2
    while r[-1] != 0:
        q = math.floor(r[k - 2] / r[k - 1])
        r.append(r[k - 2] - q * r[k - 1] ), s.append(s[k - 2] - q * s[k - 1] ), t.append(t[k - 2] - q * t[k - 1])
        k += 1
    d = t[-1]+t[-2]
    return d;

def check(phi, e, d):
    checking = False
    while checking == False:
        if d < 0 :
            e = relativPrime(phi)
            d = EUA(phi, e)
        else:
            checking = True

    return d, e;

def encrypt(n, e, plaintext):
    cipherText = plaintext**e % n
    return cipherText

def decrypt(n, d, ciphertext):
    #potens = cipherText**d
    #plainText = potens % n

#------------------------------------------------------------#
# Fundet algoritme på nettet, snak med Jacob og brugen af det.

    if n == 1:
        return 0;
    result = 1
    base = ciphertext % n
    while d > 0:
        if d % 2 == 1:
            result = (result * base) % n
        d = d >> 1
        base = (base * base) % n
    return result
#------------------------------------------------------------#



p = 671998030559713968361666935769
q = 282174488599599500573849980909
n = p*q
phi = phiCalc(p,q)
e = relativPrime(phi)
d = EUA(phi, e)
print("1")
#d, e = check(phi, e, d)
#print("1")
print(d,e)

print(encrypt(n, e, 2551252151251))

print(decrypt(n, d, encrypt(n, e, 2551252151251)))
