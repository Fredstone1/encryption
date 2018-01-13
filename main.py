import numpy as np
import random
import math
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


def relativPrime(phi):
    fundetPrime = False
    while fundetPrime == False:
        e = random.randint(1,phi)
        if sfd(phi,e) == 1:
            fundetPrime = True
            return e;

def EUA(a, b):
    r, s, t = [], [], []
    r.append(a), s.append(1), t.append(0)
    r.append(b), s.append(0), t.append(1)
    for k in range(2, 6):
        q = math.floor(r[k - 2] / r[k - 1])
        r.append(r[k - 2] - q * r[k - 1] ), s.append(s[k - 2] - q * s[k - 1] ), t.append(t[k - 2] - q * t[k - 1])
    return r, s, t;

# TODO
# vi burde fixe for loop sådan det kører det korrekte antal gange
# vi skal "løse" for resterne som i eksempel 6.4 for at få inverse modulære satan



# -------------------------------------------------------------------------------------------------------------#
# Det her virker men er ret langsomt...
def nyrelativP(phi):
    start_time = time.time()
    relativePrimes = []
    for i in range(2, phi):
        if sfd(phi, i) == 1:
            relativePrimes.append(i)
    print("--- %s seconds ---" % (time.time() - start_time))
    return relativePrimes


def d(a, b):  # det er denne funktion der er sygt langsom ....
    #resultD = b**(sum(nyrelativP(a)))%a  #<- dette er det samme som for loopet men ikke lige så optimeret
    e = sum(nyrelativP(a))
    resultD = 1
    for e in range(0, e):
        resultD = (b * resultD) % a
    return resultD;
# -------------------------------------------------------------------------------------------------------------#

# print(EUA(384,18))
print(EUA(264,17))
