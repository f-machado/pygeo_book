## Distribución Anaconda

El [paquete core de Python](https://www.python.org/downloads/) es fácil de instalar con un instalador *standalone* en nuestra máquina, sin embargo para estos tutoriales vamos a usar la distribución Anaconda. 

[Anaconda](https://www.anaconda.com/what-is-anaconda/) es una distribución que contiene: 

1.  El paquete core de Python **y además**
2.  las versiones compartibles de las librerias más populares para la programación científica.


Anaconda provee un manejo muy útil de instalación de paquete, permitiendonos crear *environments* como una forma de compartimentalizar las distintas versiones de Python, con sus paquetes y versiones asociadas para un determinado proyecto.

En particular estos tutoriales fueron creados mediante la libreria [Jupyter Book](https://jupyterbook.org/en/stable/intro.html), para el cual se creó un *environment* específico con Python 3.7 y los respectivos paquetes que veremos a continuación a lo largo del tutorial. 


### Instalar Anaconda

Para instalar Anaconda, [descargar el binario correspondiente](https://www.anaconda.com/download/) y seguir las instrucciones.


### Actualizar Anaconda

Anaconda utiliza una herramienta denominada `conda` para permitir el manejo de paquetes y *environments* y actualización de los paquetes pertinentes. 

Un comando `conda` que se debería ejecutar regularmente es el comando que actualiza la totalidad de la distribución Anaconda, para ello:

1.  Abrir una terminal (`Anaconda Prompt` en Windows)
2.  Ejecutar `conda update anaconda`

Para más información sobre `conda`, tambien se puede ejecutar `conda help` en la terminal.