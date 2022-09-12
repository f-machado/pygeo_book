#!/usr/bin/env python
# coding: utf-8

# # Colecciones - Listas, tuplas, sets y diccionarios. 

# La mayoría de los lenguajes de programación proveen objetos contenedores del tipo `array`, que permiten almacenar un gran número del mismo tipo y acceder a ellos a través de una indexación. Sin embargo Python no contiene en su lenguaje core, o base, el concepto de array. En cambio contiene objetos más generales que permiten el almacenamiento de distintos elementos con sus particularidades, entre ellos `listas`, `tuplas`, `strings o cadenas`, y `diccionarios`. 
# 
# Las listas en Python son un tipo **contenedor**, compuesto, que se usan para almacenar conjuntos de elementos relacionados del mismo tipo o de tipos distintos. Junto a las clases tuple, range y str, son uno de los tipos de **secuencia** en Python, con la particularidad de que son mutables. Esto último quiere decir que su contenido se puede modificar después de haber sido creada.
# 
# El uso de listas nos permite simular el uso de un array, y en un pasado esta era la forma de realizar cálculo numérico. Pero debido a la generalidad de las listas que dan gran flexibilidad al usuario, tales cálculos toman mucho más tiempo de ejecución que sus equivalentes en Fortran o C, otros lenguajes de programación. 
# 
# Para hacer frente a esta dificultad, los desarrolladores crearon una nueva librería, la famosa `numpy`, que permite la implementación de arrays en C y la vectorización de operaciones, que ayuda a disminuir significativamente pero no completamente eliminar la penalización de velocidad. 
# 
# Para usos genéricos, y en pequeña escala, estos tipos de objetos son útiles y eficientes por lo que serán desarrollados en las siguientes secciones. Es cuando se empieza a escalar en cantidad de datos que `numpy` empieza a tomar escena, situación que es la norma en el uso del procesamiento de imágenes satelitales. 
# 

# ## Listas
# 
# Una `lista` es un objeto Python que consiste en un conjunto ordenado de elementos, encerrados por corchetes y separados por coma. Pueden agruparse valores de distintos tipos de datos básicos, hasta listas pueden ser un elemento de una lista. 
# 
# Además este tipo de datos se consideran `mutables`, es decir se pueden agregar, eliminar o modificar elementos de las listas en cualquier momento.
# 
# Para los propósitos de indexación, el orden comienza con el índice `0` para el primer lugar de la lista, y termina con el índice `n-1`, donde n es el número de elementos en la lista.
# 
# ### Inicializar una lista vacía
# 
# 
# A veces es útil inicializar una lista vacía, donde a lo largo de un programa vayamos agregando distintos elementos a ella. Para ello, existen dos formas de realizarlo:

# In[1]:


lista_vacia = []
otra_lista_vacia = list()


# 

# ### Inicializar una lista con elementos
# 
# Para inicializar una lista con elementos, podemos agregar los datos y/o variables compatibles separados por comas y entre corchetes.

# In[2]:


lista_con_elementos_varios = [1, 'b', lista_vacia, 7.56, True]

lista_con_elementos_varios


# 

# 
# ### Determinar el tamaño de la lista
# 
# Usaremos la función `help` para imprimir que realiza la función `len`, y que argumentos tiene como entrada. 
# 

# In[3]:


help(len)


# In[4]:


len(lista_con_elementos_varios)


# 

# ### Agregar elemento a la lista
# 
# Para agregar un elemento a la lista, usaremos el método `append`:

# In[5]:


help(list.append)


# In[6]:


nuevo_elemento_a_agregar = 'SentinelMNDWI_marzo_norm.tif'
lista_con_elementos_varios.append(nuevo_elemento_a_agregar)

lista_con_elementos_varios


# 

# ### Acceder a un elemento de la lista
# 
# Como se dijo al principio de esta sección, los elementos de una lista (y en general para todas las secuencias), pueden accederse a través de un índice el cual va de `0` a `n-1`, siendo n el tamaño de la lista.

# In[7]:


print(lista_con_elementos_varios)

print('El primer elemento de la lista es: ', lista_con_elementos_varios[0])

print('El último elemento de la lista es: ', lista_con_elementos_varios[len(lista_con_elementos_varios) - 1])


# Las listas, y en general las secuencias, también permiten la indexación a partir del último elemento usando indexación negativa, accediendo al último elemento con el índice `-1`, y al primer elemento con `n`, donde `n` es el número de elementos totales de la lista.
# 
# Por lo tanto para acceder al último elemento se puede ejecutar la siguiente sentencia:

# In[8]:


print(lista_con_elementos_varios)

print('El último elemento de la lista es: ', lista_con_elementos_varios[-1])



# In[9]:


print('El primer elemento de la lista usando indexación negativa es: ', lista_con_elementos_varios[-len(lista_con_elementos_varios)])



# 

# ### Acceso a un subconjunto de elementos
# 
# Dada un lista cualquiera, podemos formar listas a partir de ella usando la operación de slicing. La forma más básica de realizarla es, dada una lista llamada `l`, podemos acceder a un subconjunto dado por por `l`[`principio`:`final`], utilizado el operador `[:]`.
# 
# <img src="../images/list_slicing.png" class="align-center"/>
# 
# Notemos que el subconjunto extraído mediante esta notación va desde `principio` hasta `final-1`. También los argumentos de principio y final son opcionales, si no se especifican se toma por defecto el primer elemento de la lista, o el último.
# 
# 

# In[10]:


#Inicialiar la lista de esta forma con un string, nos crea una lista con cada elemento ocupando un lugar en la lista.
lista_ejemplo = list('abcdefgh') 

print('Esta es la lista de ejemplo usada como base para extraer subsecciones: ', lista_ejemplo)

#Observamos que se imprimen los elementos de la lista de la posición 0 hasta la 3. 
print('Resultado de [0:4]: ', lista_ejemplo[0:4])

# Los argumentos de principio y final son opcionales en el operador :
# Vemos que el 0 se puede obviar en esta ocasión para obtener un ressultado equivalente:
print('Resultado de [:4]: ', lista_ejemplo[:4])

# También se pueden usar subíndices negativos
print('Resultado de [-4:-1]: ', lista_ejemplo[-4:-1])

print('Resultado de [-4:]: ', lista_ejemplo[-4:])

# Y combinación de índices positivos y negativos

print('Resultado de [1:-3]: ', lista_ejemplo[1:-3])




# También es posible acceder a los elementos de una lista indicando un paso con el operador `[::]`, es decir [`principio`:`final`:`paso`].

# In[11]:


print('Esta es la lista de ejemplo usada como base para extraer subsecciones: ', lista_ejemplo)

#Observamos que se imprimen los elementos de la lista de la posición 0 hasta la 4, con un paso de 2. 
print('Resultado de [0:4:2]: ', lista_ejemplo[0:4:2])

# Imprimimos todos los elementos de la lista pero en orden reverso
print('Resultado de [::-1]: ', lista_ejemplo[::-1])

print('Resultado de [-6:-4:-2]: ', lista_ejemplo[-4:-7:-2])



# 

# ### Modificar elementos de una lista
# 
# Es posible modificar un elemento de una lista en Python con el operador de asignación `=`. Para ello, lo único que se necesita es el índice del elemento que se quiere modificar o el rango de índices:

# In[12]:


lista_ejemplo[0:4] = ['alpha', 'beta', 'gamma']
lista_ejemplo[-1] = 'El saldo de tu tarjeta es insuficiente'

lista_ejemplo


# ###

# ### Operadores de pertenencia en listas
# 
# Se pueden utilizar los operadores de pertinencia `in` y `not in` para determinar si un elemento en particular se encuentra dentro de una lista, y en general en cualquier secuencia. 
# 
# Si el elemento se encuentra en la lista, el operador `in` dará `True` y `False` si no se encuentra. Asimismo `not in` es la operación complemento. 

# In[13]:


print('Los valores de los elementos de la lista son: ', lista_ejemplo)
print('') #Imprimimos un cadena vacía para hacer un renglón, es puramente estético.

print('Se encuentra e en lista_ejemplo?: ', 'e' in lista_ejemplo)
print('Se encuentra a en lista_ejemplo?: ', 'a' in lista_ejemplo)
print('No se encuentra a en lista_ejemplo?: ', 'a' not in lista_ejemplo)


# 

# ### Tabla resumen de otras operaciones

# <style type="text/css">
# .tg  {border-collapse:collapse;border-color:#ccc;border-spacing:0;}
# .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
#   font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
#   font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg .tg-64ey{background-color:#dae8fc;border-color:#c0c0c0;font-family:inherit;text-align:center;vertical-align:top}
# .tg .tg-35ak{background-color:#dae8fc;border-color:#c0c0c0;font-family:inherit;text-align:left;vertical-align:top}
# .tg .tg-ow7q{border-color:#c0c0c0;font-family:inherit;text-align:left;vertical-align:top}
# </style>
# <table class="tg">
# <thead>
#   <tr>
#     <th class="tg-64ey">Método</th>
#     <th class="tg-35ak">Descripción</th>
#   </tr>
# </thead>
# <tbody>
#   <tr>
#     <td class="tg-ow7q">append()</td>
#     <td class="tg-ow7q">Añade un nuevo elemento al final de la lista.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">extend()</td>
#     <td class="tg-ow7q">Añade un grupo de elementos (iterables) al final de la lista.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">insert(indice, elemento)</td>
#     <td class="tg-ow7q">Inserta un elemento en una posición concreta de la lista.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">remove(elemento)</td>
#     <td class="tg-ow7q">Elimina la primera ocurrencia del elemento en la lista.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">pop([i])</td>
#     <td class="tg-ow7q">Obtiene y elimina el elemento de la lista en la posición i. Si no se especifica, obtiene y elimina el último elemento.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">clear()</td>
#     <td class="tg-ow7q">Borra todos los elementos de la lista.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">index(elemento)</td>
#     <td class="tg-ow7q">Obtiene el índice de la primera ocurrencia del elemento en la lista. Si el elemento no se encuentra, se lanza la excepción ValueError.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">count(elemento)</td>
#     <td class="tg-ow7q">Devuelve el número de ocurrencias del elemento en la lista.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">sort()</td>
#     <td class="tg-ow7q">Ordena los elementos de la lista utilizando el operador &lt;.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">reverse()</td>
#     <td class="tg-ow7q">Obtiene los elementos de la lista en orden inverso.</td>
#   </tr>
#   <tr>
#     <td class="tg-ow7q">copy()</td>
#     <td class="tg-ow7q">Devuelve una copia poco profunda de la lista.</td>
#   </tr>
# </tbody>
# </table>

# 

# ## Sets

# ## Tuplas

# ## Diccionarios

# 
# 
# ##  Operaciones comunes de las secuencias
# 
# Las operaciones de la siguiente tabla están soportadas por la mayoría de los tipos secuencia, tanto mutables como inmutables. La clase ABC collections.abc.Sequence se incluye para facilitar la implementación correcta de estas operaciones en nuestros propios tipos de secuencias.
# 
# La tabla lista las operaciones ordenadas de menor a mayor prioridad. En la tabla, s y t representan secuencias del mismo tipo, n, i, j y k son números enteros y x es un objeto arbitrario que cumple con cualquier restricción de tipo o valor impuesta por s.
# 
# 
