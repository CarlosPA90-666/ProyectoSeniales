import requests
import matplotlib.pyplot as plt
import numpy as np

ListaValor=[]
ListaLocalidad=[]
Localidad=[]
Casos=[]
Tiempo=[]

urlDatos = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search_sql?'
urlDatosSQL = 'sql=SELECT "Localidad de residencia", count(*) as Cantidad from "b64ba3c4-9e41-41b8-b3fd-2da21d627558" GROUP BY "Localidad de residencia" ORDER BY "Localidad de residencia"'

req = requests.get(url=urlDatos+urlDatosSQL)
reqJson = req.json() #Organizar datos
Datos = reqJson['result']['records']
i=0


#Grafica de barras

for fila in Datos:
    ListaValor.append(int(fila["cantidad"]))
    ListaLocalidad.append(fila["Localidad de residencia"])
    i = i + 1

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(11, 5))

y_pos = np.arange(len(ListaLocalidad))

ax.barh(y_pos, ListaValor, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(ListaLocalidad)
ax.invert_yaxis()
ax.set_xlabel('Número de contagiados')
ax.set_ylabel('Localidades')
ax.set_title('Contagios Covid-19 Bogotá')

plt.grid()



#Graficas tortas

labels = ListaLocalidad
sizes = ListaValor

fig1, ax1 = plt.subplots(figsize=(10,7))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
ax.set_title("Contagios Covid-19 Bogotá")

fig, ax = plt.subplots(figsize=(15, 10), subplot_kw=dict(aspect="equal"))
recipe = ListaLocalidad
data = ListaValor
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("Contagios Covid-19 Bogotá")


#Grafica 2 dimensiones

t = np.arange(0, 22)
s = np.array(ListaValor)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.grid(True, linestyle='dashed')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
ax.set_title("Contagios Covid-19 Bogotá")
ax.set_xlabel('Numero de Localidades')
ax.set_ylabel('Contagiados')

plt.show()