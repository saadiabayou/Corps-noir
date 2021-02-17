#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:36:32 2021

@author: Saadia Bayou
"""

""" Ce programme permet de déterminer la température d'une étoile (corps noir) ou la longeur d'onde du maximum d'intensité 
    de cette étoile en appliquant la loi de Wien , selon la donnée d'entrée connue :
    température ou longeur d'onde maximale """

# Constante 
C=2.898e10-3 # m.K -> unité en métre Kelvin

# Liste des deux paramètres d'entrées pour le calcul 

# longeur d'onde du maximum d'intensité 
# Temppérature de rayonnement du corps noir -> étoile 

data=["température","longueur d'onde"]

    
def Wien_lambda(T):
    """ Cette fonction calcul la longueur d'onde à partir de la température """
    lambda_max=C/T
    return print("La longueur d'onde max vaut : \n lambda_max = ",lambda_max, "métre")
     
def Wien_T(lambda_max):
    """Cette fonction calcul la température à partir la longueur d'onde """
    T=C/lambda_max   
    return print("La température vaut T= :",T , "Kelvin") 

    
def resolve():
    d=input("Entrer le type de donnée d'entrée : \n Taper température ou longueur d'onde : \n")
    if d==data[0]:
        print("Calcul de lambda max :")
        T=float(input("Entrer la valeur de la température en Kelvin : T= "))
        return Wien_lambda(T)
    elif d==data[1]:
        print("Calcul de la température :")
        lambda_max=float(input("Entrer la valeur de la longeur d'onde max émise en mètre : lambda_max = "))
        return Wien_T(lambda_max)
    else: 
        return print("Donnée inconnue")
        
 
print(resolve())
 




 
   

