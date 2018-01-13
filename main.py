import math
from sympy import nextprime
import random

def sfd(prime1, prime2):
    while prime2 != 0:
        temp = prime2
        prime2 = prime1 % prime2
        prime1 = temp
    return prime1;

def phiCalc(prime1, prime2):
    phi = abs((prime1 - 1) * (prime2 - 1)) / sfd(prime1 - 1, prime2 - 1)
    return phi;

# def findPrime():

def relativPrime(phi):
    fundetPrime = False
    while fundetPrime == False:
       e = random.randint(1,phi)
       if sfd(phi,e) == 1:
           fundetPrime = True
    #        return e;
    # e = pyprimes.primes_above(phi/2)
    #e = 1
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
    # cipherText = plaintext**e % n
    # return cipherText
    if n == 1:
        return 0;
    result = 1
    base = plaintext % n
    while e > 0:
        if e % 2 == 1:
            result = (result * base) % n
        e = e >> 1
        base = (base * base) % n
    return result

def decrypt(n, d, ciphertext):
    # potens = cipherText**d
    # plainText = potens % n
    # ------------------------------------------------------------#
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

# ------------------------------------------------------------#
p = 1272833
q = 1271971
n = int(p * q)
# ------------------------------------------------------------#
# Du skal ikke slette det, det er nice og nemt at holde styr på
print('n = ', n, ' nLength = ', len(str(int(n))))
phi = int(phiCalc(p, q))
print('phi = ', phi, ' phiLength = ', len(str(int(phi))), ' phiHalfed = ', phi / 2)
e = nextprime(phi/2)
print('e = ', e)
# e = relativPrime(phi)
#d = pow(phi, e, n)
d = EUA(phi,e)
d, e = check(phi, e, d)
print('d = ', d, 'e = ', e)

enc = pow(17,e,n)
dec = pow(enc,d,n)
print(dec)
#print('encryption = ', encrypt(n, e, 17))
#ciphertext = encrypt(n, e, 17)

#print('decryption = ', decrypt(n, d, ciphertext))
# ------------------------------------------------------------#

#TODO
# gør dette