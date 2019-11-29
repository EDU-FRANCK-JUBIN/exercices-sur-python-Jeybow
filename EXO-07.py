# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:12:49 2019

@author: Jérémie
"""
from easygui import floatbox, integerbox

def maFonction(x):
    """Definition d'une fonction particuliere."""
    return 2*x**3 + x - 5

def tabuler(fonction, borneInf, borneSup, nbPas):
    h = (borneSup - borneInf) / float(nbPas)
    x = borneInf
    while x <= borneSup:
        y = fonction(x)
        print("f({:.2f}) = {:.3f}".format(x, y))
        x += h

# programme principal -----------------------------------------------
a = floatbox("Borne inferieure :", "", 0.0, -100.0, 100.0)
b = floatbox("Borne superieure :", "", a+.1, a)
n = integerbox("Nombre de pas :", "", 10, 0)

tabuler(maFonction, a, b, n)
