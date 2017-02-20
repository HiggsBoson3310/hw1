import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate 

def derivacion(x,y):
    s = []
    for i in range(1,len(x)-1):
        der = (y[i+1]-y[i-1])/(x[i+1]-x[i-1])
        s.append(der)
    return s

data = open('dat.txt')
lists = data.readlines()

datos = []
for i in range(len(lists)):
    datos.append(lists[i].split())
    
H = []
T = []

for i in range(len(datos)):
    if (len(datos[i])>2):
        try:
            p = float(datos[i][0])
            H.append(float(datos[i][1]))
            T.append(float(datos[i][2]))
        except ValueError:
            continue
plt.title('Temperatura vs Altura')
plt.ylabel('Temperatura(C)')
plt.xlabel('Altura(m)')
plt.plot(H,T,color='r',label="Datos Medidos")
plt.legend(loc=0)
plt.savefig("TemperaturePlot.pdf")

t = np.linspace(2500,25000,int((25000-2500)/150))
tck = interpolate.splrep(H,T)
T_spline = interpolate.splev(t,tck)
plt.plot(t, T_spline,label="Interpolacion")
plt.legend(loc=0)
plt.xlim(2500,25000)

d = derivacion(t, T_spline)

x_p = []
y_p = []

for i in range(len(d)):
    if ((abs(d[i])*1000)>9.8):
        x_p.append(t[i+1])
        y_p.append(T_spline[i+1])
plt.scatter(x_p,y_p,color='g',label='Puntos de atmosfera estable',s=10)
plt.legend(loc=0)
plt.show()

