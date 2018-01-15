from math import floor
import random

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

# ------------------------------------------------------------#
p = 2367495770217142995264827948666809233066409497699870112003149352380375124855230068487109373226251983
q = 1814159566819970307982681716822107016038920170504391457462563485198126916735167260215619523429714031
plaintext = txt2ascii("hemmelig besked 123")
# ------------------------------------------------------------#
n = int(p * q)
phi = int(phiCalc(p, q))
e = relativPrime(phi)
d = EUA(phi,e)
d, e = check(phi, e, d)
enc = encrypt(n,e,plaintext)
dec = decrypt(n,d,enc)
dec = ascii2txt(dec)
print(dec)
# ------------------------------------------------------------#

#TODO
# primtal eller billedkodning
