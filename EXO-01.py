# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:21:19 2019

@author: Jérémie
"""
from math import pi
while True :
    try:
        hauteur  = int(input ("Entrer une hauteur  : "));
        assert (hauteur > 0);
        break;
    except ValueError:
        print("Choisissez une hauteur de type entier");
    except AssertionError:
        print("Le nombre doit être superieur à zéro");
while True :
    try:
        rayon  = int(input ("Entrer un rayon : "));
        assert(rayon > 0);
        break;
    except ValueError:
        print("Choisissez un rayon de type entier");
    except AssertionError:
        print("Le nombre doit être superieur à zéro");

try:
    aire = pi * rayon**2;
    volume = (aire * hauteur) / 3;
    print("Le volume du cone droit est  : ", volume);
except ValueError:
    print("une des deux entrée n'est pas bonne");