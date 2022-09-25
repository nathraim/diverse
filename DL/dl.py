# -*- coding: utf-8 -*-
# Initial code from https://moonbooks.org/Articles/Ecrire-un-code-en-python-pour-illustrer-le-d%C3%A9veloppement-limit%C3%A9-en-0-de-cosinus/
import matplotlib.pyplot as plt
import numpy as np
import math

#----------------------------------------------------------------------------------------#
# Part I:  Plot cosinus function

xmin = -2.0*np.pi
xmax =  2.0*np.pi

x = np.arange(xmin,xmax,0.1)
y = np.cos(x)

plt.plot(x,y)

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.grid()
plt.xlim(xmin,xmax)
plt.ylim(-1.2,1.2)

#plt.savefig("cosinus.png", bbox_inches='tight')
plt.show()

#----------------------------------------------------------------------------------------#
# Part II:  Cosinus Taylor series Function

def dl0_cosinus(x,n):
    f = 0
    for i in range(n+1):
        f = f + ( (-1.0)**i / math.factorial(2.0*i) ) * x**(2.0*i)
    return f


#----------------------------------------------------------------------------------------#
# Plot with order 2n = 4

n = 2

y = dl0_cosinus(x,n)

plt.plot(x,y)
#plt.savefig("test_dl0_cosinus.png", bbox_inches='tight')

plt.show()
#plt.close()

#----------------------------------------------------------------------------------------#
# Part III:  Create a loop over n

for n in range(1,10):

    x = np.arange(xmin,xmax,0.1)
    y = np.cos(x)

    plt.plot(x,y)

    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    plt.grid()
    plt.xlim(xmin,xmax)
    plt.ylim(-1.2,1.2)

    y = dl0_cosinus(x,n)
    plt.plot(x,y)
    plt.title(u"Développement limité de la fonction cosinus ( n =  "+str(n) +")")
    #plt.savefig("dl0_cosinus_"+str(n)+".png", bbox_inches='tight')
    #plt.close()
    plt.show()

