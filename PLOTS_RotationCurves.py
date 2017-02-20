#importamos los paquetes necesarios para desarrollar el problema
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import *
#Leemos el archivo de datos que queremos y guardamos los datos en listas
data = open('RotationCurve_F571-8.txt','r')
lists = data.readlines()
#Ahora separamos los datos de cada columna en una lista separada transformandolos de tipo string a tipo float.
datos=[]
for i in range(len(lists)):
    datos.append(lists[i].split())
ARad = []
PRad = []
Vgas = []
Vdisk = []
VBul = []
Vel = []
e_Vel = []
for columna in datos:
    ARad.append(float(columna[1]))
    PRad.append(float(columna[2]))
    Vgas.append(float(columna[3]))
    Vdisk.append(float(columna[4]))
    VBul.append(float(columna[5]))
    Vel.append(float(columna[6]))
    e_Vel.append(float(columna[7]))
#Con las listas correspondientes a cada uno de los datos podemos realizar las graficasque queremos obtener
y = np.array(Vgas)+np.array(Vdisk)+np.array(VBul)
plt.plot(PRad, Vel, c='k', label='Velocidad Medida')
plt.plot(PRad, y, c='g', label='Suma de velocidad de bulbo, gas y disco')
plt.xlabel('Radio (kpc)')
plt.ylabel('Velocidad (km/s)')
plt.title('Velocidad de Roatcion en F571-8')
#Finalmente guardamos la grafica en un archivo pdf
plt.savefig('RotationCurvePlot.pdf')

