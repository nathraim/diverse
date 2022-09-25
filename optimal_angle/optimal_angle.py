import numpy as np
import matplotlib.pyplot as plt

g = 10 # m/s^2
v0 = 10 # m/s

def opt_angle(g,v0,h):
    return np.arcsin(np.sqrt(1/(2*(1+g*h/v0**2))))


h = np.linspace(-5,100,101) # Set of different initial heights
opt = opt_angle(g,v0,h) # Array of optimal angle for a given h

plt.plot(h,np.degrees(opt))
plt.xlabel("hauteur (m)")
plt.ylabel("angle optimal (°)")
plt.grid()
plt.show()

# Si on lance toujours avec l'angle optimal, quelle est la distance parcourue ?
def func_xmax(g,v0,h,angle):
    return v0**2*np.sin(2*angle)/(2*g) + (v0/g)*np.cos(angle)*np.sqrt((v0*np.sin(angle))**2 + 2*g*h)

xmax = func_xmax(g,v0,h,opt) # Calcultes xmax for a given height

plt.plot(h,xmax)
plt.show()


h = 10
opt = opt_angle(g,v0,h)
xmax = func_xmax(g,v0,h,opt)
xmax_alt = (v0/g)*np.sqrt(v0**2 + 2*g*h)
print("comp", xmax, xmax_alt)

#def opt_angle2(ratio):
#    return np.degrees(np.arcsin(np.sqrt(1/(2*(1+ratio)))))

#ratio = np.linspace(0,100,101)
#opt2 = opt_angle2(ratio)
#plt.plot(ratio,opt2)
#plt.show()
