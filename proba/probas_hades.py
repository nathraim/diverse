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
from matplotlib.widgets import Slider, Button
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


# def esperance_maths_direct(n,nb_c,p): #Version directe, sans réutiliser la fonction proba
#     esp1 = 0
#     esp2 = 0
#     for k in range(1,n+1): #correspond à la partie P(X<=k)
#         for j in range(0,min(nb_c,k)):
#             esp1 += k*math.comb(k-1,j)*p**j*(1-p)**(k-1-j)
#     esp1 *= p/nb_c
#     for j in range(0,min(nb_c,n+1)): #correspond à la partie P(X=n+1)
#         esp2 += math.comb(n,j)*p**j*(1-p)**(n-j)*(nb_c-j)/nb_c
#     esp2 *= n+1
#     return esp1 + esp2

def esperance_maths(n_max:int,nb_c:int,p:float) -> float:
    esp = 0
    for k in range(1,n_max+2):
        esp += k*proba_maths(k,n_max,nb_c,p)
    return esp

def repartition(k:int,n_max:int,nb_c:int,p:float) -> float:
    repart = 0
    for j in range(1,k+1):
        repart += proba_maths(j,n_max,nb_c,p)
    return repart

def checkprob(lst_prob) -> None:
    tolerance = 1e-6
    # lst_prob = [proba_maths(i,n_max,nb_c,p) for i in range(1,n_max+2)]
    somme = sum(lst_prob)
    if abs(somme-1) > tolerance:
        print(f"ATTENTION : la somme des probabilités ne vaut pas 1 mais {somme}")
    else:
        print(f"La somme des probabilités vaut bien 1 (à {tolerance} près)")


def simulation(nb_repet,n_max,nb_c,p) -> list:
    lst_c_orig = list(range(1,nb_c+1)) # Liste des cartes.
    carte_recherchee = nb_c # On s'intéressera à la carte n°nb_c
    # lst_proba = []
    # lst_n = [n for n in range(1,n_max+1)]
    # for n in range(1,n_max+1):
    # zone_obtenue = n_max+1 # Par défaut, la carte n'a pas été obtenue après n zones
    # moyenne_zone = 0
    nb_occ = [0 for i in range(n_max+1)] #nombre d'occurrences : occ[i] contiendra le nombre de fois
    #où la carte qui nous intéresse a été obtenue lors de la zone n°i+1 (k commence à 1)
    # print(nb_occ)
    for irepet in range(nb_repet):
        # print("REPET",irepet)
        lst_c = lst_c_orig.copy()
        # print("lst_c orig",lst_c)
        zone_obtenue = n_max+1 # Par défaut, la carte n'a pas été obtenue après n zones
        for k in range(1,n_max+1): # on parcourt n_max zones  
            if not lst_c :#Tant que la liste des cartes est non vide
                # print("BREAK")
                break            

            if random.random() < p:
                 pbool = True
            else:
                 pbool = False
            # pbool = random.choices([False,True],[1-p,p])
            
            # print("activation dans zone n°",k,pbool)
            if pbool: #s'il y a activation 
                indice_carte = random.randint(0,len(lst_c)-1)
                # print("indice_carte",indice_carte)
                # print("indice carte", indice_carte,lst_c)
                if lst_c[indice_carte] == carte_recherchee:
                    zone_obtenue = k
                lst_c.pop(indice_carte)
                # print("lst_c",lst_c)
        # moyenne_zone += zone_obtenue
        # print("ZONE",zone_obtenue)
        nb_occ[zone_obtenue-1] += 1        
        # print("nb_occ",nb_occ)
        # moyenne_zone /= nb_repet
        # lst_proba.append(moyenne_zone)
    for i,el in enumerate(nb_occ):
        nb_occ[i] /= nb_repet
    # return lst_proba
    # print(nb_occ)
    return nb_occ


# n_max = 30 # nombre de zones parcourues
# nb_c = 10 # nombre de cartes
# p = 1 # paramètre d'activation

# lst_k = [i for i in range(1,n_max+2)]
# lst_prob = [proba_maths(i,n_max,nb_c,p) for i in range(1,n_max+2)]
# checkprob(lst_prob)
# lst_esp = [esperance_maths(i,nb_c,p) for i in range(1,n_max+2)]

# nb_repet = 100000
# lst_prob_stat = simulation(nb_repet,n_max,nb_c,p)

# # Crée une figure avec deux sous-graphes côte à côte
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# # Premier graphe
# ax1.plot(lst_k, lst_prob, marker='o', markersize=6, markerfacecolor='orange', 
#          markeredgecolor='black', ls='', label='proba math')
# # ax1.plot(lst_k, lst_prob_stat, marker='x', markersize=3, markerfacecolor='black', 
#          # markeredgecolor='black', ls='',label='proba stat')
# # ax1.set_xticks(lst_n)  # Ticks aux positions de lst_n
# ax1.set_xticks(range(min(lst_k), max(lst_k)+1, 2))  # Ticks tous les 2 entiers
# ax1.set_ylim(-0.005, max(lst_prob)*1.1)
# ax1.set_title('Probabilité d\'activation de la carte "Mort" (n fixé)')
# ax1.set_xlabel('k')
# ax1.set_ylabel('Probabilité')
# ax1.legend()
# # ax1.legend(['Probabilité'])

# # Deuxième graphe
# ax2.plot(lst_k, lst_esp, marker='o', markersize=6, markerfacecolor='orange', 
#          markeredgecolor='black', ls='')
# ax2.set_xticks(range(min(lst_k), max(lst_k)+1, 2))  # Ticks tous les 2 entiers
# ax2.set_ylim(0, max(lst_esp)*1.1) 
# # ax2.set_ylim(min(lst_esp)*0.9, max(lst_esp)*1.1)
# ax2.set_title('Espérance selon le nombre de zones parcourues')
# ax2.set_xlabel('n')
# ax2.set_ylabel('Espérance')
# # ax2.legend(['Espérance'])

# # Affiche les graphes
# plt.tight_layout()
# plt.show()


########

# Données initiales
n_max = 40 # nombre de zones parcourues
nb_c = 20 # nombre de cartes
p = 0 # paramètre d'activation

lst_k = [i for i in range(1,n_max+2)]
lst_prob = [proba_maths(k,n_max,nb_c,p) for k in range(1,n_max+2)]
checkprob(lst_prob)
lst_esp = [esperance_maths(n,nb_c,p) for n in range(1,n_max+1)]
lst_repart = [repartition(k,n_max,nb_c,p) for k in range(1,n_max+1)] #On ne prend pas en compte P(X=n+1)

# Créer les subplots
fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(12, 8))
# plt.subplots_adjust(bottom=0.2)  # Laisse de la place pour le curseur

# lst_prob = np.power(lst_prob, 0.1)  # 0.3 < 1 pour étirer les petites valeurs

# 1er graphe
line1, = ax1.plot(lst_k, lst_prob, marker='o', markersize=6, markerfacecolor='orange', 
         markeredgecolor='black', ls='', label='proba math')
ax1.set_title('Probabilité d\'activation de la carte "Mort" (n fixé)')
ax1.set_xticks(range(min(lst_k), max(lst_k)+1, 2))  # Ticks tous les 2 entiers
ax1.set_yticks(np.linspace(min(lst_prob), max(lst_prob), 10))
ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.3f}'))  # 2 chiffres après la virgule
ax1.set_ylim(-0.005, max(lst_prob)*1.1)
ax1.set_xlabel('Numéro de la zone')
ax1.set_ylabel('Probabilité')

# 2è graphe
line2, = ax2.plot(lst_k[:-1], lst_esp, marker='o', markersize=6, markerfacecolor='orange', 
         markeredgecolor='black', ls='')
ax2.set_title('Espérance selon le nombre de zones parcourues')
ax2.set_xticks(range(min(lst_k[:-1]), max(lst_k[:-1])+1, 2))  # Ticks tous les 2 entiers
ax2.set_yticks(range(int(min(lst_esp)), int(max(lst_esp))+1, 2))  # Ticks tous les 2 entiers
ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))  # 2 chiffres après la virgule
ax2.set_ylim(0, max(lst_esp)*1.1)
ax2.set_xlabel('Nombre de zones')
ax2.set_ylabel('Espérance')
# ax1.legend()
# ax2.legend()

# 3è graphe
line3, = ax3.plot(lst_k[:-1], lst_repart, marker='o', markersize=6, markerfacecolor='orange', 
         markeredgecolor='black', ls='', label='proba math')
ax3.set_title('Probabilité d\'activation avant une zone donnée (n fixé)')
ax3.set_xticks(range(min(lst_k[:-1]), max(lst_k[:-1])+1, 2))  # Ticks tous les 2 entiers
ax3.set_yticks(np.linspace(min(lst_repart), max(lst_repart), 10))
ax3.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))  # 2 chiffres après la virgule
ax3.set_ylim(-0.005, max(lst_repart)*1.1)
ax3.set_xlabel('Numéro de la zone')
ax3.set_ylabel('Fonction de répartition')


# Ajouter un texte dynamique
text_p = ax1.text(0.8, 0.95, '', transform=ax1.transAxes, fontsize=10,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
text_nbc = ax1.text(0.8, 0.85, '', transform=ax1.transAxes, fontsize=10,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Fonction d'initialisation (optionnelle)
def init():
    line1.set_ydata(lst_prob)
    # ax1.set_ylim(-0.005, max(lst_prob)*1.1)
    # ax1.set_ylim(-0.005, 1)
    # ax1.set_yscale('log')
    line2.set_ydata(lst_esp)
    line3.set_ydata(lst_repart)
    text_p.set_text(f'p = {p:.2f}')
    text_nbc.set_text(f'{nb_c} cartes')
    return line1, line2, line3, text_p, text_nbc

# Fonction d'animation
def update(p): # Met à jour les données pour chaque sous-graphe
    if p<=1:
        lst_prob = [proba_maths(k,n_max,nb_c,p) for k in range(1,n_max+2)]
        # lst_prob = np.power(lst_prob, 0.5)  # 0.3 < 1 pour étirer les petites valeurs    
        line1.set_ydata(lst_prob)
        ax1.set_ylim(min(-0.002,min(lst_prob)*0.9), max(lst_prob)*1.1)
        ax1.set_yticks(np.linspace(min(lst_prob), max(lst_prob), 10))
        # ax1.set_title('Probabilité d\'activation de la carte "Mort" (n fixé)')
        
        lst_esp = [esperance_maths(n,nb_c,p) for n in range(1,n_max+1)]
        line2.set_ydata(lst_esp)
        ax2.set_ylim(0, max(lst_esp)*1.1)
        # ax2.set_yticks(range(int(min(lst_esp)), int(max(lst_esp))+1, 2))  # Ticks tous les 2 entiers
        # ax2.set_yticks(np.linspace(int(min(lst_esp)),int(max(lst_esp)),10))  # Ticks tous les 2 entiers
        
        lst_repart = [repartition(k,n_max,nb_c,p) for k in range(1,n_max+1)]
        line3.set_ydata(lst_repart)
        # ax3.set_ylim(-0.005, max(lst_repart)*1.1)
        ax3.set_ylim(0,1.1)
        # ax3.set_yticks(np.linspace(min(lst_repart), max(lst_repart), 10))
        ax3.set_yticks(np.linspace(0, 1, 11))
        
        text_p.set_text(f'p = {p:.3f}')  # Met à jour le texte
        # fig.canvas.draw_idle()
    else:
        pass
    return line1, line2, line3, text_p

# Créer l'animation
lst_frames = np.linspace(0, 1, 101)
empty_frames = np.full(10,2)
lst_frames = np.concatenate((lst_frames,empty_frames),axis=None)

ani = FuncAnimation(
    fig,
    update,
    frames=lst_frames,  # Nombre de frames
    init_func=init,
    interval=100,  # Délai entre les frames (ms)
    blit=False,  # Optimisation pour éviter de redessiner tout
    repeat=True
)

plt.tight_layout()

plt.show()

# ani.save('animation.mp4', writer='ffmpeg')  # Nécessite ffmpeg
ani.save(filename="proba_hades.gif", writer="pillow",fps=10,dpi=100)





    
                
            
