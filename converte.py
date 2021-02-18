#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:15:28 2021

@author: Saadia Bayou
"""


evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  
lambdas=[] # Initalisation liste longueurs d'onde
Energies=[] # Initialisation liste Energies

def convert_m_nm (l):
    """Convertit une grandeur en mètre en nanomètre"""
    L=l*(1e+9)
    return L

def convert_nm_m(l):
    """ Convertit une grandeur en nanomètre en mètre """
    L=l/(1e+9)
    return L
#
def convert_J_ev (EJ):
    """ Convertit une grandeur en  Joule en electronvolt """
    return EJ/evJ 


def convert_ev_J(Eev):
    """ Convertit une grandeur en electronvolt en  Joule """
    
    print("\nLa grandeur en ev convertie en Joules vaut :\n ")
    return str(Eev*evJ) + " Joules" 
    
def convert_deg_K(T):
    """ Convertit une température de degrés en Kelvin """
    T= 273.15 + T
    return T
    
def convert_K_deg(T):
    """ Convertit une température de Kelvin en degrés"""
    T=T-273.15
    return T
    