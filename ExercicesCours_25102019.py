# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:55:26 2019

@author: Jérémie
"""

def conversionTemps(seconde):
    minutes = seconde/60;
    heure = minutes/60;
    jour = heure/24;
    mois = jour/31;
    annee = mois/12;
    liste = [seconde,minutes,heure,jour,mois,annee];
    listeStr = [' Secondes',' Minutes',' Heures',' Jours',' Mois',' Annee'];
    for i in range(0,len(liste)):
        print(" Cela fait : " + str(liste[i]) + listeStr[i])
conversionTemps(12345678912)


def nombrePairsImpaires(liste):
    newListePaire = [];
    newListeImpaire = [];
    for i in range (0,len(liste)):
        if liste[i] %2 == 0:
            newListePaire.append(liste[i]);
        else:
            newListeImpaire.append(liste[i])
    print("Nombres paires : " + str(len(newListeImpaire)))
    print("Nombres impaires : " + str(len(newListePaire)))
    
listeNombres = [32,5,12,8,3,75,2,15];
nombrePairsImpaires(listeNombres);

def max2Nombres(a,b):
    if a > b:
        print(a);
    else:
        if a == b:
            print ("égalité : " + a)
        else:
            print(b);
max2Nombres(4,6)

def max3Nombres(a,b,c):
    print(max(a,b,c))
max3Nombres(4,1,8)

def newMaxXNombres(liste):
    liste.sort()
    print(liste[-1])
listeNb = [32,5,12,8,3,75,2,15];
newMaxXNombres(listeNb);

import matplotlib as plt
plt.plot([1,2,3,4])