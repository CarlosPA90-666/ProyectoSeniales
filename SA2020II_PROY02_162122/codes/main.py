import seaborn as sb
import requests
import matplotlib.pyplot as plt
import numpy as np

ListaValor=[]
ListaLocalidad=[]
Localidad=[]
Casos=[]
Tiempo=[]

urlDatos = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search_sql?'
urlDatosSQL = 'sql=SELECT "LOCALIDAD_ASIS", count(*) as Cantidad from "b64ba3c4-9e41-41b8-b3fd-2da21d627558" GROUP BY "LOCALIDAD_ASIS" ORDER BY "LOCALIDAD_ASIS"'

req = requests.get(url=urlDatos+urlDatosSQL)
reqJson = req.json() #Organizar datos
Datos = reqJson['result']['records']
i=0


#Grafica de barras

for fila in Datos:
    ListaValor.append(int(fila["cantidad"]))
    ListaLocalidad.append(fila["LOCALIDAD_ASIS"])
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


#SEGUNDO CORTE

#EVOLUCION COVID 19

Fallecidos=[]
Fallecidos2=[]
Graves=[]
Leves=[]
Moderados=[]
Recuperados=[]

urlDatos2 = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search_sql?'
urlDatosSQL2 = 'sql=SELECT "ESTADO" ,"LOCALIDAD_ASIS", count(*) as Cantidad  from "b64ba3c4-9e41-41b8-b3fd-2da21d627558"  GROUP BY "ESTADO","LOCALIDAD_ASIS" ORDER BY "ESTADO","LOCALIDAD_ASIS"'

req2 = requests.get(url=urlDatos2+urlDatosSQL2)
reqJson2 = req2.json() #Organizar datos
Datos2 = reqJson2['result']['records']


#Grafica de barras
auxDict2=[]
for x in range(int(len(Datos2)/6)):

    auxDict2.append(Datos2[x]["LOCALIDAD_ASIS"])


for I in auxDict2:
    for J in range(len(Datos2)):
        if(Datos2[J]["LOCALIDAD_ASIS"]==I):
            if(Datos2[J]["ESTADO"]=='Fallecido'):
                Fallecidos.append(int(Datos2[J]["cantidad"]))

            elif(Datos2[J]["ESTADO"]=='Fallecido No aplica No causa Directa'):
                Fallecidos2.append(int(Datos2[J]["cantidad"]))
            elif (Datos2[J]["ESTADO"] == 'Grave'):
                Graves.append(int(Datos2[J]["cantidad"]))
            elif (Datos2[J]["ESTADO"] == 'Leve'):
                Leves.append(int(Datos2[J]["cantidad"]))
            elif (Datos2[J]["ESTADO"] == 'Moderado'):
                Moderados.append(int(Datos2[J]["cantidad"]))
            elif (Datos2[J]["ESTADO"] == 'Recuperado'):
                Recuperados.append(int(Datos2[J]["cantidad"]))

fig2= plt.figure("Evolución Casos Covid-19 Bogotá", figsize=(17.5, 8.5))
fig2.suptitle("Evolución Casos Covid-19 Bogotá")

FallecidosG = fig2.add_subplot(231)
FallecidosNCDG = fig2.add_subplot(232)
GravesG = fig2.add_subplot(233)
ModeradosG = fig2.add_subplot(234)
RecuperadosG = fig2.add_subplot(235)

Localidad1 = [15 , 12, 7 , 2, 19, 10, 9, 20, 8 , 17, 14, 16, 18, 4, 3, 21, 11, 13, 6, 1 , 5]
FallecidosGG = np.array(Fallecidos)

Localidad2 = [15 , 12, 7 , 2, 19, 10, 9, 20, 8 , 17, 14, 16, 18, 4, 3, 21, 11, 13, 6, 1 , 5]
FallecidosNCDGG = np.array(Fallecidos2)

Localidad3 = [15 , 12, 7 , 2, 19, 10, 9, 20, 8 , 14, 16, 18, 4, 3, 21, 11, 13, 6, 1 , 5]
GravesGG = np.array(Graves)

Localidad4 = [15 , 12, 7 , 2, 19, 10, 9, 20, 8 , 17, 14, 16, 18, 4, 3, 21, 11, 13, 6, 1 , 5]
ModeradosGG = np.array(Moderados)

Localidad5 = [15 , 12, 7 , 2, 19, 10, 9, 20, 8 , 17, 14, 16, 18, 4, 3, 21, 11, 13, 6, 1 , 5]
RecuperadosGG = np.array(Recuperados)


FallecidosG.bar(Localidad1, FallecidosGG, align="center")
FallecidosG.set_xticks(Localidad1)
FallecidosG.set_xticklabels(Localidad1)
FallecidosG.set_ylabel("Fallecidos")
FallecidosG.set_xlabel("Número de Localidad")

FallecidosNCDG.bar(Localidad2, FallecidosNCDGG, align="center")
FallecidosNCDG.set_xticks(Localidad2)
FallecidosNCDG.set_xticklabels(Localidad2)
FallecidosNCDG.set_ylabel("Fallecidos No Causa Directa")
FallecidosNCDG.set_xlabel("Número de Localidad")

GravesG.bar(Localidad3, GravesGG, align="center")
GravesG.set_xticks(Localidad3)
GravesG.set_xticklabels(Localidad3)
GravesG.set_ylabel("Graves")
GravesG.set_xlabel("Número de Localidad")

ModeradosG.bar(Localidad4, ModeradosGG, align="center")
ModeradosG.set_xticks(Localidad4)
ModeradosG.set_xticklabels(Localidad4)
ModeradosG.set_ylabel("Moderados")
ModeradosG.set_xlabel("Número de Localidad")

RecuperadosG.bar(Localidad5, RecuperadosGG, align="center")
RecuperadosG.set_xticks(Localidad4)
RecuperadosG.set_xticklabels(Localidad4)
RecuperadosG.set_ylabel("Recuperados")
RecuperadosG.set_xlabel("Número de Localidad")

#SEXO

ListaValor=[]
ListaLocalidad=[]
Localidad=[]
Casos=[]
Tiempo=[]
Edades=[]
SexoH=[]
SexoM=[]


#LOCALIDAD
urlDatos3 = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search_sql?'
urlDatosSQL3 = 'sql=SELECT "LOCALIDAD_ASIS" , count(*) as Cantidad from "b64ba3c4-9e41-41b8-b3fd-2da21d627558" GROUP BY "LOCALIDAD_ASIS" ORDER BY "LOCALIDAD_ASIS"'

req3 = requests.get(url=urlDatos3+urlDatosSQL3)
reqJson3 = req3.json() #Organizar datos

Datos3 = reqJson3['result']['records']
i=0
#LOCALIDAD

#SEXO
urlDatos4 = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search_sql?'
urlDatosSQL4 = 'sql=SELECT "SEXO" ,"LOCALIDAD_ASIS", count(*) as Cantidad  from "b64ba3c4-9e41-41b8-b3fd-2da21d627558"  GROUP BY "SEXO","LOCALIDAD_ASIS" ORDER BY "SEXO","LOCALIDAD_ASIS"'

req4 = requests.get(url=urlDatos4+urlDatosSQL4)
reqJson4 = req4.json() #Organizar datos
Datos4 = reqJson4['result']['records']

#Grafica de barras
auxDict3=[]
#print(int(len(Datos2)/2))
for x in range(int(len(Datos4)/2)):

    auxDict3.append(Datos4[x]["LOCALIDAD_ASIS"])

#print(auxDict)

for I in auxDict3:
    for J in range(len(Datos4)):
        if(Datos4[J]["LOCALIDAD_ASIS"]==I):
            if(Datos4[J]["SEXO"]=='M'):
                SexoH.append(int(Datos4[J]["cantidad"]))
            else:
                SexoM.append(int(Datos4[J]["cantidad"]))



plt.rcdefaults()

X=np.arange(len(auxDict3))
width=0.25

fig4, ax4 = plt.subplots(figsize=(18, 7))
rects1= ax4.bar(X - (width/2), SexoM, width, label='Hombres')
rects2= ax4.bar(X + (width/2), SexoH, width, label='Mujeres')

ax4.set_ylabel('Contagios')

ax4.set_title('Contagios Covid-19 ')
ax4.set_xticks(X)
ax4.set_xticklabels(auxDict3)
ax4.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax4.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig4.tight_layout()


#MAPA DE CALOR

ListaValor=[]
ListaLocalidad=[]
Localidad=[]
Casos=[]
Tiempo=[]


urlDatos5 = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search_sql?'
urlDatosSQL5 = 'sql=SELECT "LOCALIDAD_ASIS", count(*) as Cantidad from "b64ba3c4-9e41-41b8-b3fd-2da21d627558" GROUP BY "LOCALIDAD_ASIS" ORDER BY "LOCALIDAD_ASIS"'

req5 = requests.get(url=urlDatos+urlDatosSQL)
reqJson5 = req5.json() #Organizar datos
Datos5 = reqJson5['result']['records']
i=0

for fila in Datos5:
    ListaValor.append(int(fila["cantidad"]))
    ListaLocalidad.append(fila["LOCALIDAD_ASIS"])
    i = i + 1

DatosMapa = np.asarray(ListaValor).reshape(22,1)
text = np.asarray(ListaLocalidad)

labels = (np.asarray(["{0}\n{1:.0f}".format(text,DatosMapa) for text, DatosMapa in zip(text.flatten(), DatosMapa.flatten())])).reshape(22,1)

fig5, ax5 = plt.subplots(figsize=(15.5,9))
heat_map = sb.heatmap(DatosMapa, annot=labels,xticklabels=False, fmt='', cbar_kws={'label': 'Numero de contagios', 'orientation': 'vertical'}, )
heat_map.set_title("MAPA DE CALOR COVID-19 POR LOCALIDADES")



#EDADES


ListaValor=[]
ListaLocalidad=[]
Localidad=[]
Casos=[]
Tiempo=[]
Edades=[]
Edades=[]

urlDatos6 = 'https://datosabiertos.bogota.gov.co/api/3/action/datastore_search_sql?'
urlDatosSQL6 = 'sql=SELECT "EDAD","LOCALIDAD_ASIS", count(*) as Cantidad from "b64ba3c4-9e41-41b8-b3fd-2da21d627558"  GROUP BY "EDAD","LOCALIDAD_ASIS" ORDER BY "EDAD","LOCALIDAD_ASIS"'

req6 = requests.get(url=urlDatos6+urlDatosSQL6)
reqJson6 = req6.json() #Organizar datos
Datos6 = reqJson6['result']['records']
auxDict6=[]

for x in range(int(len(Datos6)/96)):

    auxDict6.append(Datos6[x]["LOCALIDAD_ASIS"])


Edad1=[]
Edad2=[]
Edad3=[]
Edad4=[]
Edad5=[]
Edad6=[]
Edad7=[]
Edad8=[]
Edad9=[]
Edad10=[]
Edad11=[]
Edad12=[]
Edad13=[]
Edad14=[]
Edad15=[]
Edad16=[]
Edad17=[]
Edad18=[]
Edad19=[]
Edad20=[]
Edad21=[]
Edad22=[]
Edad23=[]
Edad24=[]
Edad25=[]
Edad26=[]
Edad27=[]
Edad28=[]
Edad29=[]
Edad30=[]
Edad31=[]
Edad32=[]
Edad33=[]
Edad34=[]
Edad35=[]
Edad36=[]
Edad37=[]
Edad38=[]
Edad39=[]
Edad40=[]
Edad41=[]
Edad42=[]
Edad43=[]
Edad44=[]
Edad45=[]
Edad46=[]
Edad47=[]
Edad48=[]
Edad49=[]
Edad50=[]
Edad51=[]
Edad52=[]
Edad53=[]
Edad54=[]
Edad55=[]
Edad56=[]
Edad57=[]
Edad58=[]
Edad59=[]
Edad60=[]
Edad61=[]
Edad62=[]
Edad63=[]
Edad64=[]
EdadV=[]

for I in auxDict6:
    for J in range(len(Datos6)):
        if(Datos6[J]["LOCALIDAD_ASIS"]==I):
            if(Datos6[J]["EDAD"]) == "1":
                Edad1.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "2":
                Edad2.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "3":
                Edad3.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "4":
                Edad4.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "5":
                Edad5.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "6":
                Edad6.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "7":
                Edad7.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "8":
                Edad8.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "9":
                Edad9.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "10":
                Edad10.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "11":
                Edad11.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "12":
                Edad12.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "13":
                Edad13.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "14":
                Edad14.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "15":
                Edad15.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "16":
                Edad16.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "17":
                Edad17.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "18":
                Edad18.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "19":
                Edad19.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "20":
                Edad20.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "21":
                Edad21.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "22":
                Edad22.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "23":
                Edad23.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "24":
                Edad24.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "25":
                Edad25.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "26":
                Edad26.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "27":
                Edad27.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "28":
                Edad28.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "29":
                Edad29.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "30":
                Edad30.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "31":
                Edad31.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "32":
                Edad32.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "33":
                Edad33.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "34":
                Edad34.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "35":
                Edad35.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "36":
                Edad36.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "37":
                Edad37.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "38":
                Edad38.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "39":
                Edad39.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "40":
                Edad40.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "41":
                Edad41.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "42":
                Edad42.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "43":
                Edad43.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "44":
                Edad44.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "45":
                Edad45.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "46":
                Edad46.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "47":
                Edad47.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "48":
                Edad48.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "49":
                Edad49.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "50":
                Edad50.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "51":
                Edad51.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "52":
                Edad52.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "53":
                Edad53.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "54":
                Edad54.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "55":
                Edad55.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "56":
                Edad56.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "57":
                Edad57.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "58":
                Edad58.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "59":
                Edad59.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "60":
                Edad60.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "61":
                Edad61.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "62":
                Edad62.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "63":
                Edad63.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) == "64":
                Edad64.append(int(Datos6[J]["cantidad"]))
            elif(Datos6[J]["EDAD"]) > "64":
                EdadV.append(int(Datos6[J]["cantidad"]))

niños = (sum(Edad1)+sum(Edad2)+sum(Edad3)+sum(Edad4)+sum(Edad5)+sum(Edad6)+sum(Edad7)+sum(Edad8)+sum(Edad9)+sum(Edad10)+sum(Edad11)+sum(Edad12)+sum(Edad13))
Adolecentes = (sum(Edad14)+sum(Edad15)+sum(Edad16)+sum(Edad17))
AdultosJ = (sum(Edad19)+sum(Edad20)+sum(Edad21)+sum(Edad22)+sum(Edad23)+sum(Edad24)+sum(Edad25)+sum(Edad26)+sum(Edad27)+sum(Edad28)+sum(Edad29)+sum(Edad30)+sum(Edad31)+sum(Edad32)+sum(Edad33)+sum(Edad34)+sum(Edad35))
Adultos = (sum(Edad36)+sum(Edad37)+sum(Edad38)+sum(Edad39)+sum(Edad40)+sum(Edad41)+sum(Edad42)+sum(Edad43)+sum(Edad44)+sum(Edad45)+sum(Edad46)+sum(Edad47)+sum(Edad48)+sum(Edad49)+sum(Edad50)+sum(Edad51)+sum(Edad52)+sum(Edad53)+sum(Edad54)+sum(Edad55)+sum(Edad56)+sum(Edad57)+sum(Edad58)+sum(Edad59)+sum(Edad60)+sum(Edad61)+sum(Edad62)+sum(Edad63)+sum(Edad64))
TerceraEdad = (sum(Edad36))

labels = 'Niños (1-13) ', 'Adolecentes (14-17)', 'Adultos (36-64)', 'Adultos jovenes (18-35)', 'Tercera Edad (65 en adelante)'
sizes = [niños, Adolecentes, Adultos, AdultosJ, TerceraEdad]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)


fig6, ax6 = plt.subplots(figsize=(15, 7))
ax6.pie(sizes,explode=explode, autopct='%1.1f %%', shadow=True, startangle=90)
ax6.set_title("Discriminacion por edades Covid-19 Bogotá")
ax6.legend(labels,title="EDADES",loc="lower left",bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()