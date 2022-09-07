#!/usr/bin/env python
# coding: utf-8

# # Variables

# Una variable en Python es un nombre simbólico que sirve como un referencia o puntero a un objeto. Una vez que este objeto es asignado a la variables, se puede referir a este objeto almacenado en la memoria con este nombre. 
# 

# In[1]:


a = 5
vamos_boquita = False
otorrinolaringologia = 'especialidad médico-quirúrgica que se encarga del estudio de las enfermedades del oído, tanto auditivas como del equilibrio, de las vías respiratorias superiores y parte de las inferiores'
yrupe = 3.141516


# La elección del nombre de las variables queda a criterio del programador, donde cada variables puede contener cualquier letra entre la a-z, A-Z, guiones bajos _ y los dígitos 0-9, pero no puede empezar con un número. Asimismo los nombres de variables son sensible a su capitalización, así que `a` es distinto a `A`.

# In[2]:


A = 6

print('El valor de a es ', a)
print('El valor de A es ', A)
print('Es a igual a A?: ', a == A)


# Es importante como buena práctica de programación asignar variables con nombres descriptivos para dejar en claro para que son usadas. Hay distintas convenciones sobre como dar estilo a las variables, por ejemplo:
# 
# 
# - Estilo Camello: La segunda y subsiguientes palabras son capitalizadas, para hacer mas legible la variable. 
# Ejemplo: nombreLoteAMuestrear
# - Estilo Pascal: Idéntico al caso anterior, pero con la primer palabra capitalizada.
# Ejemplo: NombreLoteAMuestrear
# - Estilo Serpiente: Las palabras son separadas por guiones bajos.
# Ejemplo: nombre_lote_a_muestrear
# 
# La guía de estilo para código en Python, también conocida como [PEP 8](https://peps.python.org/pep-0008/), contiene una sección de Convenciones de nombramiento que sugiere estándares para nombrar diferentes tipos de objetos. Por ejemplo, recomienda:
# 
# - Estilo Serpiente para funciones y nombres de variables.
# - Estilo Pascal para nombres de Clases. (Denominado como "CapWords")
# 
# Lo importante es adoptar una convención y ser consistente a lo largo del desarrollo del programa, para lograr una mayor legibilidad y organización del código. 
# 

# ### Tipos de variables

# Existen diversos tipos de datos básicos en Python.
# 
# - Número Entero (int)
# 
# Este tipo de dato se corresponde con números enteros, es decir, sin parte decimal.
# 
# - Número Decimal (float)
# 
# Este tipo de dato se corresponde con números reales con parte decimal. Cabe destacar que el separador decimal en Python es el punto (.) y no la coma (,).
# 
# - Caracter (chr)
# 
# Este tipo de dato se corresponde con un símbolo tipográfico, es decir, una letra, número, coma, espacio, signo de punutación, etc.
# 
# - Cadena de Texto (str)
# 
# Este tipo de datos se corresponde con una cadena de caracteres.
# 
# - Booleano (bool)
# 
# Este tipo de dato reconoce solamente dos valores: Verdadero (True) y Falso (False)

# In[3]:


print('El valor de a es:', a) 
print('El tipo de variable de a es:', type(a))
print('\n') #Imprimir el caracter \n nos permite hacer un salto de línea

print('El valor de vamos_boquita es:', vamos_boquita) 
print('El tipo de variable de vamos_boquita es:', type(vamos_boquita))
print('\n')

print('El valor de otorrinolaringologia es:', otorrinolaringologia) 
print('El tipo de variable de otorrinolaringologia es:', type(otorrinolaringologia))
print('\n')

print('El valor de yrupe es:', yrupe) 
print('El tipo de variable de yrupe es:', type(yrupe))


# En muchos lenguasjes de progrmación las variables son estáticas con respecto al tipo con las fueron construídas. Sin embargo Python nos ofrece la posibilidad de reasignar el tipo de dato de una variable, cuestión útil para pasar números flotantes a enteros, números en general a caracteres, etc.
# 
# Para ello, Python ofrece las siguientes funciones:
# 
# - str(): Devuelve la representación en cadena de caracteres del objeto que se pasa como parámetro.
# - int(): Devuelve un int a partir de un número o secuencia de caracteres.
# - float(): Devuelve un float a partir de un número o secuencia de caracteres.
# 

# In[4]:


edad = '29'
edad = edad + 10


# In[14]:


edad = '29'
edad = int(edad) + 10
print(edad)


# ### Alcance de las variables

# 

# In[4]:


import os
import re
#import rasterio as rio


# In[ ]:





# In[2]:





# In[3]:





# In[4]:


archivo_tiff = r'Interferogram_flat.tif'


# In[ ]:




