from math import floor
import random
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
       e = random.randint(int(phi//2)+1,phi)
       if sfd(phi,e) == 1:
           fundetPrime = True
    return e;

def EUA(phi, e):
    r, s, t = [], [], []
    r.append(phi), s.append(1), t.append(0)
    r.append(e), s.append(0), t.append(1)
    k = 2
    while r[-1] != 0:
        q = floor(r[k - 2] // r[k - 1])
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

def Baillie_PSW():
    # laver først trial division med de første x antal primes
    primes = []
    while len(primes) < 2:
        txt = "er sandsynligvis primtal"
        txt2 = "er ikke primtal"

        N = pow(2,random.randint(5,50))-1
        fp = divide()
        for i in fp:
            if N % i == 0:
                txt = txt2
        t = 0
        d = N-1
        while True:
            q, r = divmod(d,2)
            if r == 1:
                break
            t += 1
            d = q
        assert(pow(2,t)*d == N-1)

        if pow(2,d,N) != 1:
            txt = txt2
        for i in range(1,t):
            if pow(2,pow(2,i)*d,N) != N-1:
                txt = txt2

        if txt != txt2:
            txt = str(N) + " " + txt
            primes.append(N)

    if primes[0] == primes[1]:
        print("hi")
        primes = []
        Baillie_PSW()
    # Sortere listen:

    if primes[0] < primes[1]:
        temp = primes[0]
        primes[0] = primes[1]
        primes[1] = temp

    return primes[0], primes[1]

def RSAcheck(prime1, prime2):
    plaintext = [17]
    n = prime1 * prime2
    phi = (prime1, prime2)
    e = relativPrime(phi)
    d = EUA(phi, e)
    d, e = check(phi, e, d)
    enc = encrypt(n, e, plaintext)
    dec = decrypt(n,d,enc)
    if dec == plaintext:
        return True
    else:
        Baillie_PSW()


def divide():
    fp = []
    for i in sympy.primerange(1,10000): # finder alle primtal mellem 1 og 1000 således vi kan tjekke om  N er prim
        fp.append(i)
    return fp

def primeGen():
    exp = random.randint(1000,1000000)
    prime = exp_by_squaring_iterative(2,exp)-1


# ----------------------------------------------------------------------------------------------------------------#
#p = 28911710017320205966167820725313234361535259163045867986277478145081076845846493521348693253530011243988160148063424837895971948244167867236923919506962312185829914482993478947657472351461336729641485069323635424692930278888923450060546465883490944265147851036817433970984747733020522259537
#q = 16471581891701794764704009719057349996270239948993452268812975037240586099924712715366967486587417803753916334331355573776945238871512026832810626226164346328807407669366029926221415383560814338828449642265377822759768011406757061063524768140567867350208554439342320410551341675119078050953
#plaintext = txt2ascii("Hej Magnus, hvis du læser dette, så synes jeg vi skal smutte. -Rander")
# ----------------------------------------------------------------------------------------------------------------#
#n = int(p * q)
#print(len(str(n)))
#print(n.bit_length())
#phi = int(phiCalc(p, q))
#e = relativPrime(phi)
#print(e)
#d = EUA(phi,e) #d er vores private key
#d, e = check(phi, e, d) # e er public key
#enc = encrypt(n,e,plaintext)
#dec = decrypt(n,d,enc)
#dec = ascii2txt(dec)
# ----------------------------------------------------------------------------------------------------------------#

#TODO
p, q = Baillie_PSW()
print('p = ',p)
print('q = ', q)
plaintext = [17]
n = int(p * q)
phi = int(phiCalc(p, q))
e = relativPrime(phi)
d = EUA(phi,e) #d er vores private key
d, e = check(phi, e, d) # e er public key
enc = encrypt(n,e,plaintext)
dec = decrypt(n,d,enc)
print(dec)

# primtal generation
# 1. generate uneven number ex 2^n -1
#
