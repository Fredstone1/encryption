import math
import random

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
       e = random.randint((phi/2)+1,phi)
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
    ciphertext = pow(plaintext, e, n)
    return ciphertext;

def decrypt(n, d, ciphertext):
    plaintext = pow(ciphertext, d, n)
    return plaintext;

# ------------------------------------------------------------#
p = 5915587277
q = 1500450271
# ------------------------------------------------------------#
n = int(p * q)
phi = int(phiCalc(p, q))
e = relativPrime(phi)
d = EUA(phi,e)
d, e = check(phi, e, d)
enc = encrypt(n,e,17)
dec = decrypt(n,d,enc)
print(dec)
# ------------------------------------------------------------#

#TODO
# gør dette
