# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
 
def func(x,mu):
  return mu*x*(1-x)
 
def convergence_simple(mu,u0,N):
    lst_n = [0]
    lst_u = [u0]
    un = u0
    for n in range(1,N+1):
      un = func(un,mu)
      lst_n.append(n)
      lst_u.append(un)
     
    plt.plot(lst_n,lst_u,'-o')
    plt.xticks(range(0,N+1,N//5)) #pour avoir des entiers en abscisses, et toujours en avoir le même nombre affiché quel que soit N
    plt.xlabel(r'$n$')
    plt.ylabel(r'$u_n$')
    plt.title(r'$\mu$= {}, $u_0$= {}, $N$= {}'.format(mu,u0,N))
    plt.show()

convergence_simple(1.8,0.9,15)

 
def escalier(mu,u0,N):
    xlst = []
    ylst = []
    npts = 40 #nb of points to draw the function
    delta = 1/(npts-1)
    for i in range(npts):
      x = i*delta
      xlst.append(x)
      ylst.append(func(x,mu))
     
    xlst2 = [u0]
    ylst2 = [0]
    un = u0
    for n in range(1,N+1):
      xlst2.append(xlst2[-1])
      un = func(un,mu)
      ylst2.append(un)
      xlst2.append(un)
      ylst2.append(un)
     
    plt.plot(xlst,ylst) #Draw f
    plt.plot([0,1],[0,1]) #Draw y=x
    plt.plot(xlst2,ylst2)
    plt.ylim(0,1.2*mu/4)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title(r'$\mu$= {}, $u_0$= {}, $N$= {}'.format(round(mu,2),u0,N))
    plt.show()

escalier(1.8,0.9,15)

def bifurcation():
    adherence = []
    mus = []
    u0s = []
    nb_mu = 1000
    n_skip = 200
    N = 300
    u0 = 0.9
    for i in range(nb_mu):
        mu = 2+2*i/nb_mu
        un = u0    
        for _ in range(n_skip):
            un = func(un,mu)
        for _ in range(N):
            un = func(un,mu)
            mus.append(mu)
            u0s.append(u0)
            adherence.append(un)    
    plt.plot(mus,adherence,ls='',marker=',', markersize=1)
    plt.xlabel(r'$\mu$')
    plt.ylabel('Adhérence')
    plt.title('Diagramme de bifurcation')
    plt.show()

bifurcation()

# def bifurcation_3d():
#     adherence = []
#     mus = []
#     u0s = []
#     nb_mu = 100
#     n_skip = 30
#     N = 100
#     nb_u0 = 20
#     for j in range(1,nb_u0): #  On fait varier la valeur de u0
#         u0 = j/nb_u0 #u0
#         for i in range(nb_mu):
#             mu = 2+2*i/nb_mu
#             un = u0
#             #un = 0.9    
#             for _ in range(n_skip):
#                 un = func(un,mu)
#             for _ in range(N):
#                 un = func(un,mu)
#                 mus.append(mu)
#                 u0s.append(u0)
#                 adherence.append(un)

#     # Création de la figure et de l'axe 3D
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.scatter3D(mus, u0s, adherence, c=adherence, s=5, cmap='viridis',marker=',');
#     # ax.plot_trisurf(mus, u0s, adherence, cmap='viridis',edgecolor='none');
#     ax.set_xlabel(r'$\mu$')
#     ax.set_ylabel(r'$u_0$')
#     ax.set_zlabel('Adhérence')
#     plt.title('Diagramme de bifurcation')
#     ax.view_init(5, -85)
#     plt.show()

# bifurcation_3d()
        