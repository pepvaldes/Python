#!/usr/bin/env python
# coding: utf-8

# # Geolocalización
# Python Científico versión 6 - https://github.com/badillosoft/python-scig#geolocalizaci%C3%B3n-2pt

# In[3]:


latA = float(raw_input("Dame latitud A: "))   #Solicita latitud y longitud, punto A
longA = float(raw_input("Dame longitud A: "))

latB = float(raw_input("Dame latitud B: "))   #Solicita latitud y longitud, punto B
longB = float(raw_input("Dame longitud B: "))


# In[4]:


from math import sin, cos, asin, pi

#Formula de Haversine

r = 6371000 #radio de la tierra 

c = (pi/180) #convertir radianes

d_m = 2 * r * asin(( sin( c * ( latB - latA ) / 2 ) **2 + cos(c * latA) * cos(c * latB) * sin( c * (longB - longA) / 2 ) **2 ) ** 0.5)


#Conversiones de KM, M, CM para la distancia entre dos puntos.
d_km = d_m/1000
d_cm = d_m * 100

d_m = round(d_m, 2)
d_km = round(d_km, 2)
d_cm = round(d_cm, 2)

#Conversiones de tiempo para peatón y auto

p_h = d_km / 2
p_min = p_h * 60
p_seg = p_min * 60

p_h = round(p_h, 2)
p_min = round(p_min, 2)
p_seg = round(p_seg, 2)

a_h = d_km / 60
a_min = a_h * 60
a_seg = a_min * 60


a_h = round(a_h, 2)
a_min = round(a_min, 2)
a_seg = round(a_seg, 2)





# In[5]:


# Impresión de datos

print("Coordenada A: ({},{})".format(latA,longA))
print("Coordenada B: ({},{})".format(latB,longB))
print("Distancia ({}cm, {}m, {}km)".format(d_cm,d_m,d_km))
print("Tiempo: ")
print("Peatón: ({}seg, {}min, {}h)".format(p_seg,p_min,p_h))
print("Auto: ({}seg, {}min, {}h)".format(a_seg,a_min,a_h))


# In[ ]:




