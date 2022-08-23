## Environments

Un *environment*, o entorno virtual, es una copia de Python que tiene como características estar aislada y operativa bajo un nombre específico. Este entorno matiene sus propios archivos, directorios y rutas de modo tal que se puede trabajar con específicas versiones de librerías de Python, o con el mismo Python, sin interferir sobre los demás proyectos. 

El principal uso de estos entornos se basa en la separación de distintos proyectos y evitar así problemas de compatibilidad y de dependencias de paquetes a lo largo del desarrollo de productos. 

El uso de estas herramientas no se evidencia a simple vista, y solo tiene sentido práctico si se tienen diferentes proyectos en la misma máquina. Por ejemplo, la ejecución de un script que hace uso de Python 2.8 puede dificultar a posteriori el uso de proyectos con Python 3.8, o ciertas librerías necesitan una versión específica para correr de la forma que están programadas debido a que cambian el nombre de funciones, o por obsolencia de ciertas características. 

Es aquí que los entornos virtuales nos dejan crear ambientes separados para cada proyecto, donde especificamos tanto la versión de Python como los de los paquetes a usar, sin que ello tenga repercusiones en los demás entornos creados o usados. 

Dentro de estos entornos, los más populares para Python son: 

1. Virtualenv
2. Conda
3. pipenv
4. venv

Conda es popular entre la comunidad científica y de datos, mientras que pipenv entre los ingenieros de software.

### El entorno conda y su uso dentro de la distribución Anaconda

Before we dive into learning commands for managing virtual environments, it may be helpful to familiarise with a few common terms regarding Conda.

 1.1. Conda vs Miniconda vs Anaconda
Conda is a language-agnostic tool for package management and environment management. As a package manager, Conda can install, update and remove packages. As an environment manager, it can manage virtual environments.

Anaconda is the most popular Python distribution (i.e way of distributing Python to end users like you and me). By installing Anaconda, you get Miniconda, Anaconda Navigator (i.e. a graphical user interface) and curated selection of packages installed.

Miniconda is a mini-scale version of Anaconda. It is also a Python distribution. By installing Miniconda, you get Conda, Python and a small number of packages installed.

As we can see, Conda is included in both Anaconda and Miniconda.


<img src="../images/conda-vs-miniconda-vs-anaconda.png" class="align-center"/>


https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
https://towardsdatascience.com/introduction-to-conda-virtual-environments-eaea4ac84e28
