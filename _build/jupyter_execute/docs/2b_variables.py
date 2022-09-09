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
# - `Estilo Camello`: La segunda y subsiguientes palabras son capitalizadas, para hacer mas legible la variable. 
# Ejemplo: nombreLoteAMuestrear
# - `Estilo Pascal`: Idéntico al caso anterior, pero con la primer palabra capitalizada.
# Ejemplo: NombreLoteAMuestrear
# - `Estilo Serpiente`: Las palabras son separadas por guiones bajos.
# Ejemplo: nombre_lote_a_muestrear
# 
# La guía de estilo para código en Python, también conocida como [PEP 8](https://peps.python.org/pep-0008/), contiene una sección de Convenciones de nombramiento que sugiere estándares para nombrar diferentes tipos de objetos. Por ejemplo, recomienda:
# 
# - Estilo Serpiente para funciones y nombres de variables.
# - Estilo Pascal para nombres de Clases. (Denominado como "CapWords")
# 
# Lo importante es adoptar una convención y ser consistente a lo largo del desarrollo del programa, para lograr una mayor legibilidad y organización del código. 
# 

# ## Tipos de variables

# Existen diversos tipos de datos básicos en Python.
# 
# - Número Entero (`int`)
# 
# Este tipo de dato se corresponde con números enteros, es decir, sin parte decimal.
# 
# - Número Decimal (`float`)
# 
# Este tipo de dato se corresponde con números reales con parte decimal. Cabe destacar que el separador decimal en Python es el punto (.) y no la coma (,).
# 
# - Caracter (`chr`)
# 
# Este tipo de dato se corresponde con un símbolo tipográfico, es decir, una letra, número, coma, espacio, signo de punutación, etc.
# 
# - Cadena de Texto (`str`)
# 
# Este tipo de datos se corresponde con una cadena de caracteres.
# 
# - Booleano (`bool`)
# 
# Este tipo de dato reconoce solamente dos valores: Verdadero (`True`) y Falso (`False`)

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


# ## Conversión entre tipos de datos
# 

# En muchos lenguajes de programación las variables son estáticas con respecto al tipo con las fueron construídas. Sin embargo Python nos ofrece la posibilidad de reasignar el tipo de dato de una variable, cuestión útil para pasar números flotantes a enteros, números en general a caracteres, etc.
# 
# Para ello, Python ofrece las siguientes funciones:
# 
# - `str()`: Devuelve la representación en cadena de caracteres del objeto que se pasa como parámetro.
# - `int()`: Devuelve un int a partir de un número o secuencia de caracteres.
# - `float()`: Devuelve un float a partir de un número o secuencia de caracteres.
# 

# In[4]:


entero = 33
decimal = 2.8182
caracter = 'F'
cadena = 'P Sherman, calle Wallaby, 42, Sydney'
booleano = True


# Tanto los valores Decimales como los Booleanos pueden ser convertidos en Enteros con la función int():

# In[5]:


print(int(decimal))
print(int(True))
print(int(False))


# Algo similar ocurre al intentar convertir Enteros o Booleanos en Decimales con la función float():

# In[6]:


print(float(entero))
print(float(True))
print(float(False))


# Es posible también, a partir de la tabla de caracteres ASCII, obtener el caracter correspondiente a un entero con chr() o viceversa con ord():
# 

# In[7]:


print(chr(entero))
print(ord(caracter))


# Mucho más interesante que esto último resulta la conversión de cualquiera de los tipos de datos presentados en cadenas de texto, algo de vital importancia a la hora de presentar resultados combinándolos con texto (o al revés, al querer sumar variables string con variables numéricas).
# 

# In[8]:


print(str(entero))
print(type(str(entero)))

print(str(decimal))
print(type(str(decimal)))


print(str(booleano))
print(type(str(booleano)))


# ### Error al sumar una variable string con un variable int

# In[9]:


edad = '29'
edad = edad + 10


# ### Conversión de string a int para permitir la operación de suma

# In[14]:


edad = '29'
edad = int(edad) + 10
print(edad)


# ## Variables reservadas
# 
# Existen ciertas palabras que tienen significado especial para el intérprete de Python. Estas no pueden utilizarse para ningún otro fin (como ser nombrar valores) excepto para el que han sido creadas. Estas son:
# 
# - and.
# - as.
# - assert.
# - break.
# - class.
# - continue.
# - def.
# - del.
# - elif.
# - else.
# - except.
# - exec.
# - finally.
# - for.
# - from.
# - global.
# - if.
# - import.
# - in.
# - is.
# - lambda.
# - not.
# - or.
# - pass.
# - print.
# - raise.
# - return.
# - try.
# - while.
# - with.
# - yield.
