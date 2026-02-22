# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 00:55:29 2026

@author: leina
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from matplotlib.animation import FuncAnimation
# from matplotlib.widgets import Slider, Button
import sys
import random

def proba_maths(k,n,nb_c,p) -> float:
    prob = 0
    if k <= n:
        for j in range(0,min(nb_c,k)):
            prob += math.comb(k-1,j)*p**j*(1-p)**(k-1-j)
        prob *= p/nb_c
    elif k == n+1:
        # Version directe
        for j in range(0,min(nb_c,n+1)):
            prob += math.comb(n,j)*p**j*(1-p)**(n-j)*(nb_c-j)
        prob /= nb_c
        #Alternativement, on peut calculer P(n+1)=1-somme(P(k))
        # for j in range(1,n+1):
        #     prob += proba_maths(j,n,nb_c,p)
        # prob = 1-prob
    else :
        print("invalid k")
    return prob

def esperance_maths(n_max:int,nb_c:int,p:float) -> float:
    esp = 0
    for k in range(1,n_max+2):
        esp += k*proba_maths(k,n_max,nb_c,p)
    return esp

# def repartition(k:int,n_max:int,nb_c:int,p:float) -> float:
#     repart = 0
#     for j in range(1,k+1):
#         repart += proba_maths(j,n_max,nb_c,p)
#     return repart

def repartition(k:int,lst_prob:list) -> float:    
    return sum(lst_prob[0:k]) # Attention, la première zone est la zone numéro 1 et non 0, donc les indices sont décalés

def checkprob(lst_prob) -> None:
    tolerance = 1e-6
    # lst_prob = [proba_maths(i,n_max,nb_c,p) for i in range(1,n_max+2)]
    somme = sum(lst_prob)
    if abs(somme-1) > tolerance:
        print(f"ATTENTION : la somme des probabilités ne vaut pas 1 mais {somme}")
    else:
        print(f"La somme des probabilités vaut bien 1 (à {tolerance} près)")


def single_experience(n_max,nb_c,p,carte_recherchee):
    lst_c = list(range(1,nb_c+1)) # Liste des arcanes, numérotées de 1 à nb_c
    # carte_recherchee = nb_c # On s'intéressera à la carte n°nb_c
    zone_obtenue = n_max+1 # Par défaut, la carte n'a pas été obtenue après n zones    
    
    for k in range(1,n_max+1): # on parcourt n_max zones  
        if not lst_c : # Tant que la liste des arcanes est non vide
            break            
        # On détermine aléatoirement si on tire une arcane ou non
        if random.random() < p:
             pbool = True
        else:
             pbool = False
        # pbool = random.choices([False,True],[1-p,p])
        
        if pbool: # s'il y a activation, on pioche une des arcanes au hasard
            indice_carte = random.randint(0,len(lst_c)-1)
            if lst_c[indice_carte] == carte_recherchee:
                zone_obtenue = k
                break
            lst_c.pop(indice_carte) # On retire l'arcane piochée de la liste

    return zone_obtenue

def simulation(nb_repet,n_max,nb_c,p) -> list:   
    carte_recherchee = nb_c # On s'intéressera à la carte n°nb_c   
    nb_occ = [0 for i in range(n_max+1)] # nombre d'occurrences : occ[i] contiendra le nombre de fois
    #où la carte qui nous intéresse a été obtenue lors de la zone n°i+1 (k commence à 1)

    for irepet in range(nb_repet): #On répète l'expérience nb_repet fois
        zone_obtenue = single_experience(n_max,nb_c,p,carte_recherchee)
        nb_occ[zone_obtenue-1] += 1        

    for i,el in enumerate(nb_occ): #On divise nb_occ par le nombre de répétitions pour avoir une proba statistique
        nb_occ[i] /= nb_repet

    return nb_occ

static_or_dynamic = "static"

if static_or_dynamic == "static":

    n_max = 30 # nombre de zones parcourues
    n_max2 = 35
    nb_c = 20 # nombre de cartes
    p = 0.95 # paramètre d'activation
    
    lst_k = [i for i in range(1,n_max+2)]
    lst_n = [i for i in range(1,n_max2+2)]
    lst_prob = [proba_maths(i,n_max,nb_c,p) for i in lst_k]
    checkprob(lst_prob)
    lst_esp = [esperance_maths(i,nb_c,p) for i in lst_n]
    lst_repart = [repartition(k,lst_prob) for k in lst_k] 
    
    # print(lst_prob,'\n',lst_repart)
    # sys.exit()
    
    nb_repet = 1000000
    lst_prob_stat = simulation(nb_repet,n_max,nb_c,p)
    lst_repart_stat = [repartition(k,lst_prob_stat) for k in lst_k]
    
    # Crée une figure avec deux sous-graphes côte à côte
    fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    
    # Premier graphe
    ax1.plot(lst_k, lst_prob, marker='o', markersize=6, markerfacecolor='orange', 
             markeredgecolor='black', ls='', label='proba math')
    ax1.plot(lst_k, lst_prob_stat, marker='o', markersize=3, markerfacecolor='black', 
             markeredgecolor='black', ls='',label='proba stat')
    # ax1.set_xticks(lst_n)  # Ticks aux positions de lst_n
    ax1.set_xticks(range(min(lst_k), max(lst_k)+1, 2))  # Ticks tous les 2 entiers
    ax1.set_ylim(-0.005, max(lst_prob)*1.1)
    ax1.set_title('Probabilité d\'activation de la carte "Refus de Mort" (n fixé)')
    ax1.set_xlabel('k')
    ax1.set_ylabel('$P(X=k)$')
    ax1.legend()
    # ax1.legend(['Probabilité'])
    
    # Deuxième graphe
    ax2.plot(lst_n, lst_esp, marker='o', markersize=6, markerfacecolor='orange', 
             markeredgecolor='black', ls='')
    ax2.set_xticks(range(min(lst_n), max(lst_n)+1, 2))  # Ticks tous les 2 entiers
    ax2.set_ylim(0, max(lst_esp)*1.1) 
    # ax2.set_ylim(min(lst_esp)*0.9, max(lst_esp)*1.1)
    ax2.set_title('Espérance selon le nombre de zones parcourues')
    ax2.set_xlabel('n')
    ax2.set_ylabel('Espérance')
    # ax2.legend(['Espérance'])
    
    # 3è graphe
    ax3.plot(lst_k, lst_repart, marker='o', markersize=6, markerfacecolor='orange', 
             markeredgecolor='black', ls='', label='proba math')
    ax3.plot(lst_k, lst_repart_stat, marker='o', markersize=3, markerfacecolor='black', 
             markeredgecolor='black', ls='', label='proba stat')
    ax3.set_title('Probabilité d\'activation avant une zone donnée (n fixé)')
    ax3.set_xticks(range(min(lst_k[:-1]), max(lst_k[:-1])+1, 2))  # Ticks tous les 2 entiers
    ax3.set_yticks(np.linspace(min(lst_repart), max(lst_repart), 10))
    ax3.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))  # 2 chiffres après la virgule
    ax3.set_ylim(-0.005, max(lst_repart)*1.1)
    ax3.set_xlabel('Numéro de la zone')
    ax3.set_ylabel('$P(X\\leq k)$')
    
    # Affiche les graphes
    plt.tight_layout()
    plt.show()


##### Début animation avec p qui varie #####

# # Données initiales
# n_max = 40 # nombre de zones parcourues
# nb_c = 20 # nombre de cartes
# p = 0 # paramètre d'activation

# lst_k = [i for i in range(1,n_max+2)]
# lst_prob = [proba_maths(k,n_max,nb_c,p) for k in lst_k]
# checkprob(lst_prob)
# lst_esp = [esperance_maths(n,nb_c,p) for n in lst_n]
# lst_repart = [repartition(k,n_max,nb_c,p) for k in lst_k] 

# # Créer les subplots
# fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(12, 8))
# # plt.subplots_adjust(bottom=0.2)  # Laisse de la place pour le curseur

# # lst_prob = np.power(lst_prob, 0.1)  # 0.3 < 1 pour étirer les petites valeurs

# # 1er graphe
# line1, = ax1.plot(lst_k, lst_prob, marker='o', markersize=6, markerfacecolor='orange', 
#          markeredgecolor='black', ls='', label='proba math')
# ax1.set_title('Probabilité d\'activation de la carte "Refus de Mort" (n fixé)')
# ax1.set_xticks(range(min(lst_k), max(lst_k)+1, 2))  # Ticks tous les 2 entiers
# ax1.set_yticks(np.linspace(min(lst_prob), max(lst_prob), 10))
# ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.3f}'))  # 2 chiffres après la virgule
# ax1.set_ylim(-0.005, max(lst_prob)*1.1)
# ax1.set_xlabel('Numéro de la zone')
# ax1.set_ylabel('$P(X=k)$')

# # 2è graphe
# line2, = ax2.plot(lst_k[:-1], lst_esp, marker='o', markersize=6, markerfacecolor='orange', 
#          markeredgecolor='black', ls='')
# ax2.set_title('Espérance selon le nombre de zones parcourues')
# ax2.set_xticks(range(min(lst_k[:-1]), max(lst_k[:-1])+1, 2))  # Ticks tous les 2 entiers
# ax2.set_yticks(range(int(min(lst_esp)), int(max(lst_esp))+1, 2))  # Ticks tous les 2 entiers
# ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))  # 2 chiffres après la virgule
# ax2.set_ylim(0, max(lst_esp)*1.1)
# ax2.set_xlabel('Nombre de zones')
# ax2.set_ylabel('Espérance')
# # ax1.legend()
# # ax2.legend()

# # 3è graphe
# line3, = ax3.plot(lst_k[:-1], lst_repart, marker='o', markersize=6, markerfacecolor='orange', 
#          markeredgecolor='black', ls='', label='proba math')
# ax3.set_title('Probabilité d\'activation avant une zone donnée (n fixé)')
# ax3.set_xticks(range(min(lst_k[:-1]), max(lst_k[:-1])+1, 2))  # Ticks tous les 2 entiers
# ax3.set_yticks(np.linspace(min(lst_repart), max(lst_repart), 10))
# ax3.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))  # 2 chiffres après la virgule
# ax3.set_ylim(-0.005, max(lst_repart)*1.1)
# ax3.set_xlabel('Numéro de la zone')
# ax3.set_ylabel('$P(X\\leq k)$')


# # Ajouter un texte dynamique
# text_p = ax1.text(0.8, 0.95, '', transform=ax1.transAxes, fontsize=10,
#                 verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
# text_nbc = ax1.text(0.8, 0.85, '', transform=ax1.transAxes, fontsize=10,
#                 verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# # Fonction d'initialisation (optionnelle)
# def init():
#     line1.set_ydata(lst_prob)
#     # ax1.set_ylim(-0.005, max(lst_prob)*1.1)
#     # ax1.set_ylim(-0.005, 1)
#     # ax1.set_yscale('log')
#     line2.set_ydata(lst_esp)
#     line3.set_ydata(lst_repart)
#     text_p.set_text(f'p = {p:.2f}')
#     text_nbc.set_text(f'{nb_c} cartes')
#     return line1, line2, line3, text_p, text_nbc

# # Fonction d'animation
# def update(p): # Met à jour les données pour chaque sous-graphe
#     if p<=1:
#         lst_prob = [proba_maths(k,n_max,nb_c,p) for k in lst_k]
#         # lst_prob = np.power(lst_prob, 0.5)  # 0.3 < 1 pour étirer les petites valeurs    
#         line1.set_ydata(lst_prob)
#         ax1.set_ylim(min(-0.002,min(lst_prob)*0.9), max(lst_prob)*1.1)
#         ax1.set_yticks(np.linspace(min(lst_prob), max(lst_prob), 10))
#         # ax1.set_title('Probabilité d\'activation de la carte "Mort" (n fixé)')
        
#         lst_esp = [esperance_maths(n,nb_c,p) for n in lst_n]
#         line2.set_ydata(lst_esp)
#         ax2.set_ylim(0, max(lst_esp)*1.1)
#         # ax2.set_yticks(range(int(min(lst_esp)), int(max(lst_esp))+1, 2))  # Ticks tous les 2 entiers
#         # ax2.set_yticks(np.linspace(int(min(lst_esp)),int(max(lst_esp)),10))  # Ticks tous les 2 entiers
        
#         lst_repart = [repartition(k,lst_prob) for k in lst_k]
#         line3.set_ydata(lst_repart)
#         # ax3.set_ylim(-0.005, max(lst_repart)*1.1)
#         ax3.set_ylim(0,1.1)
#         # ax3.set_yticks(np.linspace(min(lst_repart), max(lst_repart), 10))
#         ax3.set_yticks(np.linspace(0, 1, 11))
        
#         text_p.set_text(f'p = {p:.3f}')  # Met à jour le texte
#         # fig.canvas.draw_idle()
#     else:
#         pass
#     return line1, line2, line3, text_p


# # Créer l'animation
# lst_frames = np.linspace(0, 1, 101)
# empty_frames = np.full(10,2)
# lst_frames = np.concatenate((lst_frames,empty_frames),axis=None)

# ani = FuncAnimation(
#     fig,
#     update,
#     frames=lst_frames,  # Nombre de frames
#     init_func=init,
#     interval=100,  # Délai entre les frames (ms)
#     blit=False,  # Optimisation pour éviter de redessiner tout
#     repeat=True
# )

# plt.tight_layout()

# plt.show()

# ani.save('animation.mp4', writer='ffmpeg')  # Nécessite ffmpeg
# ani.save(filename="proba_hades.gif", writer="pillow",fps=10,dpi=100)
    
    ##### fin animation avec p qui varie #####

elif static_or_dynamic == "dynamic":

    ##### Debut animation de la simulation avec nb_repet répétitions #####
    
    n_max = 30 # nombre de zones parcourues
    n_max2 = 35
    nb_c = 20 # nombre de cartes
    p = 0.95 # paramètre d'activation
    nb_repet = 100000
    
    lst_k = [i for i in range(1,n_max+2)]
    lst_n = [i for i in range(1,n_max2+2)]
    lst_prob = [proba_maths(i,n_max,nb_c,p) for i in lst_k]
    checkprob(lst_prob)
    
    lst_prob_stat = [0 for k in lst_k]
    
    carte_recherchee = nb_c # On s'intéressera à la carte n°nb_c 
    nb_occ = [0 for i in range(n_max+1)] # nombre d'occurrences : occ[i] contiendra le nombre de fois 
     #où la carte qui nous intéresse a été obtenue lors de la zone n°i+1 (k commence à 1)
     
    fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(12, 8))
     
    line1, = ax1.plot(lst_k, lst_prob, marker='o', markersize=6, markerfacecolor='orange', 
              markeredgecolor='black', ls='', label='proba math')
    line1bis, = ax1.plot(lst_k, lst_prob_stat, marker='o', markersize=3, markerfacecolor='black', 
              markeredgecolor='black', ls='', label='proba stat')
    ax1.set_title('Probabilité d\'activation de la carte "Refus de Mort" (n fixé)')
    ax1.set_xticks(range(min(lst_k), max(lst_k)+1, 2))  # Ticks tous les 2 entiers
    # ax1.set_yticks(np.linspace(min(lst_prob), max(lst_prob), 10))
    # ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.3f}'))  # 2 chiffres après la virgule
    ax1.set_ylim(-0.003,0.06)
    ax1.set_xlabel('Numéro de la zone')
    ax1.set_ylabel('$P(X=k)$')
    ax1.legend(loc="lower left")
    
    
    text_repet = ax1.text(0.8, 0.95, '', transform=ax1.transAxes, fontsize=10,
                    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    def init2():
        line1.set_ydata(lst_prob)
        line1bis.set_ydata(lst_prob_stat)
        # ax1.set_ylim(-0.005, max(lst_prob)*1.1)
        # ax1.set_ylim(-0.005, 1)
        # ax1.set_yscale('log')
        # line2.set_ydata(lst_esp)
        # line3.set_ydata(lst_repart)
        text_repet.set_text('exp n°')
        # text_nbc.set_text(f'{nb_c} cartes')
        return line1,line1bis#, line2, line3, text_p, text_nbc
    
    def update2(irepet):  
        # print(irepet)
        # sys.exit()
        
        zone_obtenue = single_experience(n_max,nb_c,p,carte_recherchee)
        nb_occ[zone_obtenue-1] += 1   
    
        for i,el in enumerate(nb_occ): #On divise nb_occ par le nombre de répétitions pour avoir une proba statistique
            lst_prob_stat[i] = nb_occ[i]/(irepet+1)        
        
        #Mise à jour du graphe
        # line1.set_ydata(lst_prob)
        line1bis.set_ydata(lst_prob_stat)        
        text_repet.set_text(f'exp n° {irepet+1:.0f}')
        return line1, line1bis, text_repet
    
    
    ani = FuncAnimation(
        fig,
        update2,
        frames=nb_repet,  # Nombre de frames
        init_func=init2,
        interval=1,  # Délai entre les frames (ms)
        blit=True,  # Optimisation pour éviter de redessiner tout
        repeat=False
    )
    
    plt.tight_layout()
    
    plt.show()
        
    
    
    ##### Fin de l'animation de la simulation #####









    
                
            
