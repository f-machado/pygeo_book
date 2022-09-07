#!/usr/bin/env python
# coding: utf-8

# # Colecciones - Listas, tuplas, sets y diccionarios. 

# Hay tres tipos básicos de secuencia: listas, tuplas y objetos de tipo rango. Existen tipos de secuencia especiales usados para el procesado de datos binarios y cadenas de caracteres que se describirán en secciones específicas.
# 
# Operaciones comunes de las secuencias
# Las operaciones de la siguiente tabla están soportadas por la mayoría de los tipos secuencia, tanto mutables como inmutables. La clase ABC collections.abc.Sequence se incluye para facilitar la implementación correcta de estas operaciones en nuestros propios tipos de secuencias.
# 
# La tabla lista las operaciones ordenadas de menor a mayor prioridad. En la tabla, s y t representan secuencias del mismo tipo, n, i, j y k son números enteros y x es un objeto arbitrario que cumple con cualquier restricción de tipo o valor impuesta por s.
# 
# Las operaciones in y not in tienen la misma prioridad que los operadores de comparación. Las operaciones + (Concatenación) y * (Repetición) tienen la misma prioridad que sus equivalentes numéricos 3
