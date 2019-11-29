# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:03:10 2019

@author: Jérémie
"""

while True :
    try:
        nbEntier  = int(input ("Entrer un nombre entier > 1  : "));
        assert (nbEntier > 1);
        break;
    except ValueError:
        print("Choisissez un nombre entier ");
    except AssertionError:
        print("Le nombre doit être superieur à un");
        
print("Diviseurs propres de ", nbEntier, " : ")
tmp=0;
for i in range(2, nbEntier):
    if nbEntier%i == 0:
        print(i);
        tmp +=1;            
    i += 1;
if tmp == 0:
    print("C'est un nombre premier");
print("Nombre de diviseurs propres  :" , tmp);