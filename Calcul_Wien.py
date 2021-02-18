#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:25:32 2021

@author: Saadia Bayou
"""

from convert import *

evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  
lambdas=[] # Initalisation liste longueurs d'onde
Energies=[] # Initialisation liste Energies

# Constante 
 
Cte=2.898*1e-3 # m.K -> unité en métre Kelvin

# Liste des deux paramètres d'entrées pour le calcul 

# longeur d'onde du maximum d'intensité `
# Temppérature de rayonnement du corps noir -> étoile 


num_param=[1,2] # 1 -> température ; 2 -> longueur d'onde 

# Autes données
#data=["température","longueur d'onde"]
#u_T=["K","deg"]
#u_l=["m","nm"]


# Fonctions Loi de Wien

def Wien_lambda(T):
    """ Cette fonction calcul la longueur d'onde à partir de la température """
    lambda_max=Cte/T    
    return lambda_max
     
def Wien_T(lambda_max):
    """Cette fonction calcul la température à partir la longueur d'onde """
    T=Cte/lambda_max
    return T



def resolve_Wien():
    """Cette fonction calcul la température ou la longeur d'onde maximale émise par copsr noir """
    
    print("\nEntrer la donnée d'entrée connue : \n")
    
    d=int(input(" \nEntrer 1 pour la température ou entrer 2 pour la longueur d'onde : "))
    
    
    
    if d==num_param[0]:
        
       
        print("\nSaisies des données :")
        
        T=float(input("\nEntrer la valeur de la température : T= "))
        
        u_T=input("\nEntrer l'unité de la température -> K pour Kelvin ou deg pour degré : ")
        
        if u_T=="deg":
            print("\nConversion de T °C en Kelvin\n")
            T=convert_deg_K(T)
            print("T_K =",T, "Kelvin")
        
        elif u_T=="K":
            print("\nT est dans la bonne unité pour le calcul : le Kelvin")
        
        else :
            print("\nunité inconnue")
            
    
        print("\nCalcul de lambda max :")
            
        lambda_max=(Wien_lambda(T))
        print("\nLa longeur d'onde maximale émise est : lambda_max=",lambda_max, "metre\n")
        
        lambda_max_nm=(convert_m_nm (lambda_max))
        print("\nCette longeur d'onde exprimée en nanomètre est : lambda_max = ",lambda_max_nm, "nanomètre")
    
    elif d==num_param[1]:
        
        print("\nCalcul de la température :")
        
        lambda_max=float(input("\nEntrer la valeur de la longeur d'onde : lambda_max = "))
        
        u_l=input("\nEntrer l'unité de lambda_max -> m pour mètre ou nm pour nanomètre : ")
        
        if u_l=="nm":
            
            print("\nConversion de lambda en métre\n")
            lambda_max=convert_nm_m(lambda_max)
            print("lambda_max_m =",lambda_max, "mètre")
            
        elif u_l=="m":
            print("\nlambda est dans la bonne unité pour le calcul : le mètre")
        
        else :
            print("\nunité inconnue")
        
        
        T=(Wien_T(lambda_max))
        print("\n\nLa température en Kelvin est : \n \nT = ",T, "K\n")
            
        T_deg=(convert_K_deg (T))
        print("\n\nLa température exprimée en degrée Celsius est : \n \nT° = ",T_deg, "° C")
        
    else :
        return print("Donnée inconnue")

resultat=resolve_Wien()    
print(resultat)


