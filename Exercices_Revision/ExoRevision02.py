# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:46:19 2019

@author: Jérémie
"""

import turtle as t

# mise en place du tracé
stylo = t.Turtle()
stylo.shape("classic")
t.width(2)

# Tracé de la maison
# Base de la maison : Le carré
for i in range(4):
    t.forward(80) # On avance de 80
    t.left(90) # On tourne l'aiguille de 90 degrés vers la gauche

# Dessin de la porte
t.goto(20,0) # On se place à une distance de 20 de l'axe de x
t.left(90) # On réoriente l'aiguille
t.color('red')
for e in range(4): # On trace la porte
    t.forward(40)
    t.right(90)

# Dessin du toit
t.color('green')
t.up() # On leve le stylo
t.goto(80,80) # On se place à x=80, y=80
t.down() # On repose le stylo
t.left(30) # On souhaite un anlge à 60 degrés vers la gauche donc 90-60 vu que l'on est déja à 90
t.forward(80)
t.left(120) # + 90 degrés
t.forward(80)

t.done()

