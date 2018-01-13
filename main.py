import random

def sfd(prime1,prime2):
    while prime2 != 0:
        temp = prime2;
        prime2 = prime1 % prime2;
        prime = temp;
    return prime;


def phiCalc(prime1,prime2):
    phi = abs((prime1-1)*(prime2-1))/sfd(prime1-1,prime2-1)
    return phi;


def relativPrime(phi):
    fundetPrime = False;
    while fundetPrime == False:
        e = random.randint(1,phi);
        if sfd(phi,e) == 1:
            fundetPrime = True;
            return e;
