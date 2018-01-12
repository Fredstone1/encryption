import numpy as np
import random

def sfd(a,b):
    while b != 0:
        t = b;
        b = a % b;
        a = t;
    return a;

def relativP(phi):
    fundetPrime = False;
    while fundetPrime == False:
        e = random.randint(1,phi);
        if sfd(phi,e) == 1:
            fundetPrime = True;
            return e;

    