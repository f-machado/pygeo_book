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

# ## Sets
# 
# El tipo set en Python es la clase utilizada por el lenguaje para representar los conjuntos. Un conjunto es una colección desordenada de elementos únicos, es decir, que no se repiten.
# 
# Estas características hacen que los principales usos de esta clase sean conocer si un elemento pertenece o no a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).
# 
# Además, esta clase también implementa las típicas operaciones matemáticas sobre conjuntos: unión, intersección, diferencia.
# 
# Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {}, o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable (como una lista, una tupla, una cadena …).

# In[14]:


# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
nuevo_set = {1, 3, 2, 9, 3, 1}
nuevo_set


# In[15]:


# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan
set_a_partir_de_string = set('Oíd mortales, el grito sagrado')
set_a_partir_de_string


# In[16]:


# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan
set_a_partir_de_lista = set([3, 5, 6, 1, 5])
set_a_partir_de_lista


# ### Operaciones sobre conjuntos en Python (set operations)
# 
# Uno de los principales usos del tipo set es utilizarlo en operaciones del álgebra de conjuntos: unión, intersección, diferencia, diferencia simétrica, entre otros.
# 
# 
# ### Unión de conjuntos en Python
# La unión de dos conjuntos A y B es el conjunto A ∪ B que contiene todos los elementos de A y de B.
# 
# En Python se utiliza el operador | para realizar la unión de dos o más conjuntos.

# In[17]:


set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 4, 6, 8, 10}
set_1 | set_2
{1, 2, 3, 4, 6, 8}


# ### Intersección de conjuntos en Python
# La intersección de dos conjuntos A y B es el conjunto A ∩ B que contiene todos los elementos comunes de A y B.
# 
# En Python se utiliza el operador & para realizar la intersección de dos o más conjuntos.

# In[18]:


set_1 & set_2


# ### Diferencia de conjuntos en Python
# La diferencia entre dos conjuntos A y B es el conjunto A \ B que contiene todos los elementos de A que no pertenecen a B.
# 
# En Python se utiliza el operador - para realizar la diferencia de dos o más conjuntos.

# In[19]:


set_1 - set_2


# ### Diferencia simétrica de conjuntos en Python
# La diferencia simétrica entre dos conjuntos A y B es el conjunto que contiene los elementos de A y B que no son comunes.
# 
# En Python se utiliza el operador ^ para realizar la diferencia simétrica de dos o más conjuntos.

# In[20]:


set_1 ^ set_2


# ### Inclusión de conjuntos en Python
# Dado un conjunto A, subcolección del conjunto B o igual a este, sus elementos son un subconjunto de B. Es decir, A es un subconjunto de B y B es un superconjunto de A.
# 
# En Python se utiliza el operador <= para comprobar si un conjunto A es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.

# In[21]:


set_3 = {1, 2}
set_4 = {1, 2, 3, 4}
set_3 <= set_4


# In[22]:


set_3 >= set_4


# In[23]:


set_4 >= set_3


# ### Conjuntos disjuntos en Python
# Dos conjuntos A y B son disjuntos si no tienen elementos en común, es decir, la intersección de A y B es el conjunto vacío.
# 
# En Python se utiliza el método isdisjoint() de la clase set para comprobar si un conjunto es disjunto de otro.

# In[24]:


set_3.isdisjoint(set_4)


# In[25]:


set_5 = {1, 2}
set_6 = {3, 4}
set_5.isdisjoint(set_6)


# ### Igualdad de conjuntos en Python
# En Python dos conjuntos son iguales si y solo si todos los elementos de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto del otro.

# In[26]:


set_7 = {1, 2}
set_8 = {1, 2}

set_7 == set_8


# ### Métodos de la clase set en Python
# 
# <style type="text/css">
# .tg  {border-collapse:collapse;border-spacing:0;}
# .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg .tg-1eno{background-color:#FFF;color:#7A7A7A;text-align:left;vertical-align:top}
# .tg .tg-ujmt{background-color:#F7F7F9;border-color:inherit;color:#555;text-align:left;vertical-align:top}
# .tg .tg-irj4{background-color:#F7F7F9;color:#555;text-align:left;vertical-align:top}
# .tg .tg-hooj{background-color:#7A7A7A;border-color:inherit;color:#FFF;text-align:left;vertical-align:top}
# .tg .tg-izov{background-color:#FFF;border-color:inherit;color:#7A7A7A;text-align:left;vertical-align:top}
# </style>
# <table class="tg">
# <thead>
#   <tr>
#     <th class="tg-hooj"><span style="font-weight:400;color:#FFF;background-color:#7A7A7A">Método</span></th>
#     <th class="tg-hooj"><span style="font-weight:400;color:#FFF;background-color:#7A7A7A">Descripción</span></th>
#   </tr>
# </thead>
# <tbody>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">add(e)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Añade un elemento al conjunto.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">clear()</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Elimina todos los elementos del conjunto.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">copy()</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Devuelve una copia superficial del conjunto.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">difference(iterable)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Devuelve la diferencia del conjunto con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span> <span style="font-weight:400">como un conjunto nuevo.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">difference_update(iterable)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Actualiza el conjunto tras realizar la diferencia con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span><span style="font-weight:400">.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">discard(e)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Elimina, si existe, el elemento del conjunto.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">intersection(iterable)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Devuelve la intersección del conjunto con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span> <span style="font-weight:400">como un conjunto nuevo.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">intersection_update(iterable)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Actualiza el conjunto tras realizar la intersección con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span><span style="font-weight:400">.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">isdisjoint(iterable)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Devuelve</span> <span style="color:#555;background-color:#F7F7F9">True</span> <span style="font-weight:400">si dos conjuntos son disjuntos.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">issubset(iterable)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Devuelve</span> <span style="color:#555;background-color:#F7F7F9">True</span> <span style="font-weight:400">si el conjunto es subconjunto del</span> <span style="color:#555;background-color:#F7F7F9">iterable</span><span style="font-weight:400">.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">issuperset(iterable)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Devuelve</span> <span style="color:#555;background-color:#F7F7F9">True</span> <span style="font-weight:400">si el conjunto es superconjunto del</span> <span style="color:#555;background-color:#F7F7F9">iterable</span><span style="font-weight:400">.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-irj4"><span style="color:#555;background-color:#F7F7F9">pop()</span></td>
#     <td class="tg-1eno"><span style="font-weight:400">Obtiene y elimina un elemento de forma aleatoria del conjunto.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-irj4"><span style="color:#555;background-color:#F7F7F9">remove(e)</span></td>
#     <td class="tg-1eno"><span style="font-weight:400">Elimina el elemento del conjunto. Si no existe lanza un error.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-irj4"><span style="color:#555;background-color:#F7F7F9">symmetric_difference(iterable)</span></td>
#     <td class="tg-1eno"><span style="font-weight:400">Devuelve la diferencia simétrica del conjunto con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span> <span style="font-weight:400">como un conjunto nuevo.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-irj4"><span style="color:#555;background-color:#F7F7F9">symmetric_difference_update(iterable)</span></td>
#     <td class="tg-1eno"><span style="font-weight:400">Actualiza el conjunto tras realizar la diferencia simétrica con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span><span style="font-weight:400">.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-irj4"><span style="color:#555;background-color:#F7F7F9">union(iterable)</span></td>
#     <td class="tg-1eno"><span style="font-weight:400">Devuelve la unión del conjunto con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span> <span style="font-weight:400">como un conjunto nuevo.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-irj4"><span style="color:#555;background-color:#F7F7F9">update(iterable)</span></td>
#     <td class="tg-1eno"><span style="font-weight:400">Actualiza el conjunto tras realizar la unión con el</span> <span style="color:#555;background-color:#F7F7F9">iterable</span><span style="font-weight:400">.</span></td>
#   </tr>
# </tbody>
# </table>

# ## Tuplas
# 
# Las tuplas pertenecen a la categoría de tipos secuenciales y, a diferencia del tipo list, las tuplas son un tipo de secuencia inmutable. Esto quiere decir que una tupla no puede ser modificada (no se pueden añadir ni eliminar elementos a una tupla). Sintácticamente solo difiere de las listas por el uso de paréntesis () en vez de corchetes [] como delimitadores, con los métodos de índexado y de acceso análogo a las listas. 
# 
# El uso de tuplas inmutables tiene la ventaja de que nos garantiza que el valor no puede ser modificado por error, y una vez definido ya es mantenido durante toda su definición.
#  
# ### Crear una tupla vacía
# 
# 
# 
# 

# In[27]:


tupla_vacia_1 = ()
tupla_vacia_2 = tuple()

print('La tupla 1 es:', tupla_vacia_1, ' y el tipo: ', type(tupla_vacia_1), 'y su tamaño es: ', len(tupla_vacia_1))
print('La tupla 2 es:', tupla_vacia_2, ' y el tipo: ', type(tupla_vacia_2), 'y su tamaño es: ', len(tupla_vacia_2))


# ### Incializar tupla con uno o más elementos
# 
# Para crear una tupla con un único elemento: elem, o (elem, ). Observa que siempre se añade una coma.
# 
# Para crear una tupla de varios elementos, sepáralos con comas: a, b, c o (a, b, c).
# 
# Las tuplas también se pueden crear usando el constructor de la clase, tuple(iterable). En este caso, el constructor crea una tupla cuyos elementos son los mismos y están en el mismo orden que los ítems del iterable. El objeto iterable puede ser una secuencia, un contenedor que soporte la iteración o un objeto iterador.
# 
# 

# In[28]:


tupla_1 = 1,
tupla_2 = ([1, 2, 3], )

tupla_3 = tuple([1, 2, 3])

print('La tupla 1 es:', tupla_1, ' y el tipo: ', type(tupla_1), 'y su tamaño es: ', len(tupla_1))
print('La tupla 2 es:', tupla_2, ' y el tipo: ', type(tupla_2), 'y su tamaño es: ', len(tupla_2))
print('La tupla 3 es:', tupla_3, ' y el tipo: ', type(tupla_3), 'y su tamaño es: ', len(tupla_3))


# ### Indexado y particionado de tuplas
# 
# Para acceder y particionar las tuplas, el procedimiento es análogo a las listas.

# In[29]:


tupla = (6, 7, 8,9)
print(tupla)
print(tupla[0])
print(tupla[3])


# In[30]:


subtupla = tupla[1:3]
print(tupla)
print(subtupla)
print(tupla[:-1])
print(tupla[:])


# ### Métodos de la clase set en Python
# 
# <style type="text/css">
# .tg  {border-collapse:collapse;border-spacing:0;}
# .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg .tg-ujmt{background-color:#F7F7F9;border-color:inherit;color:#555;text-align:left;vertical-align:top}
# .tg .tg-hooj{background-color:#7A7A7A;border-color:inherit;color:#FFF;text-align:left;vertical-align:top}
# .tg .tg-izov{background-color:#FFF;border-color:inherit;color:#7A7A7A;text-align:left;vertical-align:top}
# </style>
# <table class="tg">
# <thead>
#   <tr>
#     <th class="tg-hooj"><span style="font-weight:400;color:#FFF;background-color:#7A7A7A">Método</span></th>
#     <th class="tg-hooj"><span style="font-weight:400;color:#FFF;background-color:#7A7A7A">Descripción</span></th>
#   </tr>
# </thead>
# <tbody>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">index(elemento)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Obtiene el índice de la primera ocurrencia del elemento en la tupla. Si el elemento no se encuentra, se lanza la excepción</span> <span style="color:#555;background-color:#F7F7F9">ValueError</span><span style="font-weight:400">.</span></td>
#   </tr>
#   <tr>
#     <td class="tg-ujmt"><span style="color:#555;background-color:#F7F7F9">count(elemento)</span></td>
#     <td class="tg-izov"><span style="font-weight:400">Devuelve el número de ocurrencias del elemento en la tupla.</span></td>
#   </tr>
# </tbody>
# </table>

# ## Diccionarios
# 
# Un objeto dicciones es un objeto tipo mapeable, que a diferencia de los tipos secuianciales (list, tuple, range o str) indexados por su posición mediante un índice numérico, los diccionarios son indexados por claves. Por esto se puede definir a un diccionario como una colección de pares de objetos clave:valor, donde se puede acceder a los distintos valores mediantes claves, que deben ser un tipo inmutable (generalmente un int, float o string). 
# 
# A pesar de que las claves son de tipo inmutable, el objeto diccionario en sí es un objeto mutable, es decir su contenido puede modificarse después de creado; y ordenado, es decir que preserva el orden en el que se insertan los pares clave:valor
# 
#  
# 
# ### Inicializar un diccionario vacio
# 
# Los delimitadores de un diccionario son las llaves { }, mediante ellos o el constructor dict es posible iniciar diccionarios vacíos:

# In[31]:


dict_vacio_1 = {}
dict_vacio_2 = dict()

print('El diccionario vacío 1 es:', dict_vacio_1, ' y el tipo: ', type(dict_vacio_1), 'y su tamaño es: ', len(dict_vacio_1))
print('El diccionario vacío 2 es:', dict_vacio_2, ' y el tipo: ', type(dict_vacio_2), 'y su tamaño es: ', len(dict_vacio_2))


# ### Inicializar un diccionario con valores
# 
# Con pares clave: valor encerrados entre llaves.
# Con argumentos con nombre. El nombre del argumento será la clave en el diccionario. En este caso, las claves solo pueden ser identificadores válidos y mantienen el orden en el que se indican. No se podría, por ejemplo, tener números enteros como claves.
# Pasando un iterable. En este caso, cada elemento del iterable debe ser también un iterable con solo dos elementos. El primero se toma como clave del diccionario y el segundo como valor. Si la clave aparece varias veces, el valor que prevalece es el último.

# In[32]:


# 1. Pares clave: valor encerrados entre llaves
dict_1 = {'B1': 1, 'B2': 2, 'B3': 3}

# 2. Argumentos con nombre
dict_2 = dict(modo_S1 = 1, modo_S2 = 2, modo_S3=3)

# 3. Pares clave: valor encerrados entre llaves
dict_3= dict({'mv_sitio_1': 1, 'mv_sitio_2': 2, 'mv_sitio_3': 3})

# 4. Iterable que contiene iterables con dos elementos
dict_4 = dict([(1, 'uno'), (2, 'dos'), (3, 'tres')])

print('El diccionario 1 es:', dict_1, ' y el tipo: ', type(dict_1), 'y su tamaño es: ', len(dict_1))
print('El diccionario 2 es:', dict_2, ' y el tipo: ', type(dict_2), 'y su tamaño es: ', len(dict_2))
print('El diccionario 2 es:', dict_3, ' y el tipo: ', type(dict_3), 'y su tamaño es: ', len(dict_3))
print('El diccionario 2 es:', dict_4, ' y el tipo: ', type(dict_4), 'y su tamaño es: ', len(dict_4))


# ### 

# 
# 
# ##  Operaciones comunes de las secuencias
# 
# Las operaciones de la siguiente tabla están soportadas por la mayoría de los tipos secuencia, tanto mutables como inmutables. La clase ABC collections.abc.Sequence se incluye para facilitar la implementación correcta de estas operaciones en nuestros propios tipos de secuencias.
# 
# La tabla lista las operaciones ordenadas de menor a mayor prioridad. En la tabla, s y t representan secuencias del mismo tipo, n, i, j y k son números enteros y x es un objeto arbitrario que cumple con cualquier restricción de tipo o valor impuesta por s.
# 
# 

# https://wiki.physics.udel.edu/wiki_qttg/images/3/31/BOOK=python_for_scientists.pdf
# 
# https://link.springer.com/content/pdf/10.1007/978-3-030-50356-7.pdf
# 
# https://j2logo.com/python
# 
# https://ingsosa.com/
