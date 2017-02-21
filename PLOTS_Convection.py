#Importamos los paquetes necesarios para resolver la situacion problema
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate 
#Definimos una funcion "derivacion" que, dados un conjunto de pares ordenados en forma de dos listas separadas, calcula su primera derivada de forma numerica al primer orden de exactitud. Retorna un array con los valores de la derivada correspondientes al valor i+1 de la lista de los valores de la absisa.
def derivacion(x,y):
    s = []
    for i in range(1,len(x)-1):
        der = (y[i+1]-y[i-1])/(x[i+1]-x[i-1])
        s.append(der)
    return s
#Leemos el archivo de los datos experimentales que queremos estudiar.
data = open('TempHeight.txt')
lists = data.readlines()
#Organizamos los datos en una lista, y los separamos tal que nos queden los datos sin espacios entre ellos
datos = []
for i in range(len(lists)):
    datos.append(lists[i].split())
#Definimos las listas de las variables altura(H) y temperatura(T)
H = []
T = []
#Guardamos los datos en las listas correspondientes. Hay que tener en cuenta un par de aspectos: (1) la fila que estamos evaluando debe estar completa, (2) todos los datos almacenados deben ser convertibles a tipo float, (3) los datos que nos interesan estan en las dos primeras columnas. 
for i in range(len(datos)):
    #Verficamos que este completo
    if (len(datos[i])>2):
        try:
	    #Verificamos que se pueda convertir a float.		
            p = float(datos[i][0])
            H.append(float(datos[i][1]))
            T.append(float(datos[i][2]))
        except ValueError:
            continue
#Graficamos los datos extraidos del archivo de texto
plt.title('Temperatura vs Altura')
plt.ylabel('Temperatura(C)')
plt.xlabel('Altura(m)')
plt.plot(H,T,color='r',label="Datos Medidos")
plt.legend(loc=0)
plt.savefig("TemperaturePlot.pdf")
#Definimos el intervalo real sobre el que se va a realizar la interpolacion de los datos. Y se procede a realizar la interpolacion usando spline
t = np.linspace(2500,25000,int((25000-2500)/150))
tck = interpolate.splrep(H,T)
T_spline = interpolate.splev(t,tck)
#Generamos las graficas de la interpolacion para compararlas con los datos recogidos
plt.plot(t, T_spline,label="Interpolacion")
plt.legend(loc=0)
plt.xlim(2500,25000)
#Calculamos la derivada en cada uno de los puntos del intervalo real sobre el que hicimos la interpolacion con los valores imagen que se obtienen. Definimos a demas las listas donde se guardaran los puntos estables. 
d = derivacion(t, T_spline)
x_p = []
y_p = []
#Buscamos los datos estables segun el parametro indicado. Teniendo en cuenta la asignacion antes comentada de los datos de la funcion "derivada". 
for i in range(len(d)):
    if ((abs(d[i])*1000)>9.8):
        x_p.append(t[i+1])
        y_p.append(T_spline[i+1])
#Generamos una serie de puntos sobre el grafico de los datos interpolados y obtenidos con los puntos obtenidos. 
plt.scatter(x_p,y_p,color='g',label='Puntos de atmosfera estable',s=10)
plt.legend(loc=0)
plt.savefig("ConvectionPLOT.pdf")
plt.close()
#Graficamos ahora el valor del Gradiente comparado con el gradiente adiabatico calculado
g = np.ones(len(t))
plt.plot(t/1000,9.8*g,color='b',label="Gradiente adiabatico seco")
plt.plot(t/1000,-9.8*g,color='b')
plt.plot(t[1:len(t)-1]/1000,np.array(d)*1000,color='g',label="Gradiente Interpolacion")
plt.title("Comparacion de Gradientes de Temperatura")
plt.ylabel("Gradiente de temperatura (C/km)")
plt.xlabel("Altura (km)")
plt.legend(loc=0)
plt.savefig("GradientsPLOT.pdf")
