# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:28:17 2019

@author: Jérémie
"""

while True :
    try:
        nbLignes  = int(input ("Entrer un nombre de lignes  : "));
        assert (nbLignes > 0);
        break;
    except ValueError:
        print("Choisissez un nombre de type entier");
    except AssertionError:
        print("Le nombre doit être superieur à zéro");
try:
    branche="^"
    espace =" " 
    i = 0
    for i in range(nbLignes):
        print((espace*(nbLignes-i)),branche+(branche*i*2))
except Exception as e:
    print(str(e))

