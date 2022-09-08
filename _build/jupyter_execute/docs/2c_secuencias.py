#!/usr/bin/env python
# coding: utf-8

# # Colecciones - Listas, tuplas, sets y diccionarios. 

# 

# La mayoría de los lenguajes de programación proveen objetos contenedores del tipo array, que permiten almacenar un gran número del mismo tipo y acceder a ellos a través de una indexación. Sin embargo Python no contiene en su lenguaje core, o base, el concepto de array. En cambio contiene objetos más generales que permiten el almacenamiento de distintos elementos con sus particularidades, entre ellos listas, tuplas, strings o cadenas, y diccionarios. 
# 
# El uso de listas nos permite simular el uso de un array, y en un pasado esta era la forma de realizar cálculo numperico. Pero debido a la generalidad de las listas que dan gran flexibilidad al usuario, tales cálculos toman mucho más tiempo de ejecución que sus equivalentes en Fortran o C, otros lenguajes de programación. 
# 
# Para hacer frente a esta dificultad, los desarrolladores crearon una nueva librería, la famosa numpy, que permite la implementación de arrays en C y la vectorización de operaciones, que ayuda a disminuir significativamente pero no completamente eliminar la penalización de velocidad. 
# 
# Para usos genéricos, y en pequeña escala, estos tipos de objetos son útiles y eficientes por lo que serán desarrollados en las siguientes secciones. Es cuando se empieza a escalar en cantidad de datos que numpy empieza a tomar escena, situación que es la norma en el uso del procesamiento de imágenes satelitales. 
# 

# ## Listas

# ## Sets

# ## Tuplas

# ## Diccionarios

#  Hay tres tipos básicos de secuencia: listas, tuplas y objetos de tipo rango. Existen tipos de secuencia especiales usados para el procesado de datos binarios y cadenas de caracteres que se describirán en secciones específicas.
# 
#  Operaciones comunes de las secuencias
# Las operaciones de la siguiente tabla están soportadas por la mayoría de los tipos secuencia, tanto mutables como inmutables. La clase ABC collections.abc.Sequence se incluye para facilitar la implementación correcta de estas operaciones en nuestros propios tipos de secuencias.
# 
# La tabla lista las operaciones ordenadas de menor a mayor prioridad. En la tabla, s y t representan secuencias del mismo tipo, n, i, j y k son números enteros y x es un objeto arbitrario que cumple con cualquier restricción de tipo o valor impuesta por s.
# 
# Las operaciones in y not in tienen la misma prioridad que los operadores de comparación. Las operaciones + (Concatenación) y * (Repetición) tienen la misma prioridad que sus equivalentes numéricos 3
