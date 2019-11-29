# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:58:38 2019

@author: Jérémie
"""

def valide(seq):
    """Retourne VRAI si la sequence est valide, FAUX sinon."""
    ret = len(seq) != 0
    for c in seq:
        ret = (ret and True) \
            if (c == 'a') or (c == 't') or (c == 'g') or (c == 'c') \
            else False
    return ret

def proportion(a, s):
    """Retourne la proportion de la sequence <s> dans la chaine <a>."""
    n = len(a)
    k = a.count(s)
    return 100.0*k/n

def saisie(c):
    s = input("{} : ".format(c))
    while not valide(s):
        print('"{}" ne peut contenir que les chainons {}'.format(c,"'a', 't', 'g' ou 'c'"))
        s = input("{} : ".format(c))
    return s

# programme principal -----------------------------------------------
adn = saisie("chaine")
seq = saisie("sequence")

print('Il y a {:.1f} % de "{}" dans "{}".'.format(proportion(adn, seq),seq, adn))