#!/usr/bin/env python
# coding: utf-8

# (file-types:notebooks)=

# # Probando notebooks

# In[1]:


import os
import re
#import rasterio as rio


# In[2]:


def listar_tiff(path, recursive = False):
    lista = []
    for file_name in glob.iglob(path+'**\*.tif', recursive = recursive):
        #print(file_name)
        lista.append(file_name)
    return lista


# In[3]:


os.chdir(r'..')
current_work_directory = os.path.abspath(os.getcwd())
print(current_work_directory)


# In[4]:


archivo_tiff = r'Interferogram_flat.tif'


# In[ ]:




