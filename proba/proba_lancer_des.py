# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 13:37:23 2026

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

def proba_maths(k:int,n:int,p:float) -> float:
    prob = 0
    if k <= n and k>=0:
        prob = math.comb(n,k)*p**k*(1-p)**(n-k)
    else:
        pass
        # print("invalid k")
    return prob

def esperance_maths(n_max:int,p:float) -> float:
    esp = 0
    for k in range(0,n_max+1):
        esp += k*proba_maths(k,n_max,p)
    return esp

def repartition(k:int,n_max:int,p:float) -> float:
    repart = 0
    for j in range(0,k+1): # ATTENTION BORNE FINALE SELON <= ou <
        repart += proba_maths(j,n_max,p)
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
# Préparation du graphe

n_max = 15 # nombre de fois où on lance le dé
n_max2 = 25 # utilisé pour les graphes où on fait varier le nombre max de lancers
lst_k = [i for i in range(0,n_max+1)]
lst_n = [i for i in range(0,n_max2+1)]

plt.close('all')  # Ferme toutes les figures éventuellement encore ouvertes

# Créer les subplots
fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(12, 8))

ax1.set_title(f'Probabilité d\'obtenir k fois le chiffre 6 en {n_max} lancers')
ax1.set_xlabel('k (nombre de succès)')
ax1.set_ylabel('$P(X=k)$')
ax1.set_xticks(range(min(lst_k), max(lst_k)+1, 2))  # Ticks tous les 2 entiers
ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.3f}'))  #3 chiffres après la virgule

ax2.set_title('Nombre moyen de 6 obtenus en n lancers')
ax2.set_xlabel('n (nombre de lancers)')
ax2.set_ylabel('Espérance')
ax2.set_xticks(range(min(lst_n), max(lst_n)+1, 2))
ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))  # affiche des entiers

ax3.set_title(f'Probabilité d\'obtenir au moins k fois le chiffre 6 en {n_max} lancers')
ax3.set_xlabel('k (nombre de succès)')
ax3.set_ylabel('$P(X\\geq k)$')
ax3.set_xticks(range(min(lst_k), max(lst_k)+1, 2))

ax4.set_title('Probabilité d\'obtenir au moins 3 fois le chiffre 6 en n lancers')
ax4.set_xlabel('n (nombre de lancers)')
ax4.set_ylabel('$P(X\\geq3)$')
ax4.set_xticks(range(min(lst_n), max(lst_n)+1, 2))

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)  

plt.tight_layout()


# static_or_dynamic = "dynamic"
static_or_dynamic = "static"

if(static_or_dynamic=="static"):
    lst_p = [1/6,2/6,3/6,4/6,5/6] # Pour un dé à 6 faces non truqué, p=1/6
    
    ax2.set_ylim(-0.5, n_max2*max(lst_p)+1)
    
    couleurs = plt.cm.Paired(np.linspace(0, 1, 5))  # 5 couleurs de la palette Paired
    # couleurs2 = plt.cm.Accent(np.linspace(0, 1, 5))  # 5 couleurs de la palette tab10
    for i,p in enumerate(lst_p):
        lst_prob = [proba_maths(k,n_max,p) for k in lst_k]
        checkprob(lst_prob)

        lst_esp = [esperance_maths(n,p) for n in lst_n]
        lst_repart = [1-repartition(k,n_max,p)+proba_maths(k,n_max,p) for k in lst_k]        
        lst4 = [1-repartition(3,n,p)+proba_maths(3,n,p) for n in lst_n]
        
        line1, = ax1.plot(lst_k, lst_prob, marker='o', markersize=6, markerfacecolor=couleurs[i], 
                 markeredgecolor='black', ls='--',color=couleurs[i])
        line2, = ax2.plot(lst_n, lst_esp, marker='o', markersize=6, markerfacecolor=couleurs[i], 
                 markeredgecolor='black', ls='--',color=couleurs[i],label=f'p={i+1}/6')
        line3, = ax3.plot(lst_k, lst_repart, marker='o', markersize=6, markerfacecolor=couleurs[i], 
                 markeredgecolor='black', ls='--', color=couleurs[i])
        line4, = ax4.plot(lst_n, lst4, marker='o', markersize=6, markerfacecolor=couleurs[i], 
                 markeredgecolor='black', ls='--', color=couleurs[i])
    
    ax2.legend()

elif(static_or_dynamic=="dynamic"):
    p = 0
    # lst_k = [i for i in range(0,n_max+1)]
    lst_prob = [proba_maths(k,n_max,p) for k in lst_k]
    # lst_prob = np.power(lst_prob, 0.1)  # 0.3 < 1 pour étirer les petites valeurs
    # checkprob(lst_prob)
    # lst_n = [i for i in range(0,n_max+1)]
    lst_esp = [esperance_maths(n,p) for n in lst_n]
    lst_repart = [1-repartition(k,n_max,p)+proba_maths(k,n_max,p) for k in lst_k]    
    lst4 = [1-repartition(3,n,p)+proba_maths(3,n,p) for n in lst_n]
    
    # 1er graphe
    line1, = ax1.plot(lst_k, lst_prob, marker='o', markersize=6, markerfacecolor='orange', 
             markeredgecolor='black', ls='', color='black')
    ax1.set_yticks(np.linspace(min(lst_prob), max(lst_prob), 10))
    ax1.set_ylim(-0.005, 0.3)        
    
    # 2è graphe
    line2, = ax2.plot(lst_n, lst_esp, marker='o', markersize=6, markerfacecolor='orange', 
             markeredgecolor='black', ls='', color='black')
    ax2.set_yticks(range(0,n_max2+1,2))  # Ticks tous les 2 entiers
    # ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))  # 0 chiffre après la virgule
    ax2.set_ylim(-0.5, n_max2+1)

    # 3è graphe
    line3, = ax3.plot(lst_k, lst_repart, marker='o', markersize=6, markerfacecolor='orange', 
             markeredgecolor='black', ls='', color='black')
    ax3.set_yticks(np.linspace(min(lst_repart), max(lst_repart), 10))
    ax3.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))  # 2 chiffres après la virgule
    ax3.set_ylim(-0.03,1.1)
    ax3.set_yticks(np.linspace(0, 1, 11))

    # 4è graphe
    line4, = ax4.plot(lst_n, lst4, marker='o', markersize=6, markerfacecolor='orange', 
             markeredgecolor='black', ls='', color='black')
    ax4.set_yticks(np.linspace(min(lst4), max(lst4), 10))
    ax4.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))  # 2 chiffres après la virgule
    ax4.set_ylim(-0.03,1.1)
    ax4.set_yticks(np.linspace(0, 1, 11))

    # Ajouter un texte dynamique
    text_p = ax1.text(0.8, 0.95, '', transform=ax1.transAxes, fontsize=10,
                    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


    # Fonction d'initialisation (optionnelle)
    def init():
        # Données initiales
        p = 0 # proba de tomber sur un 6
    
        lst_prob = [proba_maths(k,n_max,p) for k in lst_k]
        lst_esp = [esperance_maths(n,p) for n in lst_n]
        lst_repart = [1-repartition(k,n_max,p)+proba_maths(k,n_max,p) for k in lst_k]
    
        lst4 = [1-repartition(3,n,p)+proba_maths(3,n,p) for n in lst_n]
        
        line1.set_ydata(lst_prob)
        line2.set_ydata(lst_esp)
        line3.set_ydata(lst_repart)
        line4.set_ydata(lst4)
        
        text_p.set_text(f'p = {p:.2f}')
        return line1, line2, line3, line4, text_p

    # Fonction d'animation
    def update(p): # Met à jour les données pour chaque sous-graphe
        if p<=1:
            lst_prob = [proba_maths(k,n_max,p) for k in lst_k]
            # lst_prob = np.power(lst_prob, 0.5)  # 0.3 < 1 pour étirer les petites valeurs    
            line1.set_ydata(lst_prob)
            ax1.set_ylim(min(-0.01,min(lst_prob)*0.9), max(lst_prob)*1.1)
            ax1.set_yticks(np.linspace(min(lst_prob), max(lst_prob), 10))
            
            lst_esp = [esperance_maths(n,p) for n in lst_n]
            line2.set_ydata(lst_esp)
           
            lst_repart = [1-repartition(k,n_max,p)+proba_maths(k,n_max,p) for k in lst_k]
            line3.set_ydata(lst_repart)
            
            lst4 = [1-repartition(3,n,p)+proba_maths(3,n,p) for n in lst_n]
            line4.set_ydata(lst4)
            
            text_p.set_text(f'p = {p:.3f}')  # Met à jour le texte
        else:
            pass # Permet de figer l'animation grâce aux derniers frames artificiels
        return line1, line2, line3, line4, text_p

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

    # plt.show()

    # ani.save('animation.mp4', writer='ffmpeg')  # Nécessite ffmpeg
    # ani.save(filename="proba_lancer_des.gif", writer="pillow",fps=10,dpi=100)
    
    # return ani

# create_plot("static")
# create_plot("dynamic")




    
                
            
