# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:49:21 2019

@author: Jérémie
"""

while True :
    try:
        n  = int(input ("Entrer une approximation n > 50 : "));
        assert (n > 50);
        break;
    except ValueError:
        print("Choisissez une approximation de type entier");
    except AssertionError:
        print("Le nombre doit être superieur à 50");

def factorielle(n):
    if n<2:
        return 1
    else:
        return n*factorielle(n-1)
    
e = 2,7182812845904523536;
r = 0.0;
tab = [];
for i in range(n):
    r = r + 1.0/factorielle(i);
    tab.append((i,r));
print(tab());