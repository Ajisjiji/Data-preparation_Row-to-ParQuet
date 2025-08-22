#!/usr/bin/env python
# coding: utf-8

# The following notebook example will allow you to test DPK, without cloning the repo. You can run it either on Google Colab or you can use your local environment (by downloading just the notebook). We use a temporary folder for input and output, but users are encouraged to use their own input folder.

# In[1]:


#from google.colab import drive
#drive.mount('/content/drive')


# In[2]:


get_ipython().run_cell_magic('capture', '', '!pip install "data-prep-toolkit-transforms[pdf2parquet]==1.0.0a2"\n!pip install pandas\nimport urllib.request\nimport shutil\n')


# In[3]:


shutil.os.makedirs("tmp/input", exist_ok=True)
urllib.request.urlretrieve("https://raw.githubusercontent.com/data-prep-kit/data-prep-kit/dev/transforms/language/docling2parquet/test-data/input/archive1.zip", "tmp/input/archive1.zip")
urllib.request.urlretrieve("https://raw.githubusercontent.com/data-prep-kit/data-prep-kit/dev/transforms/language/docling2parquet/test-data/input/redp5110-ch1.pdf", "tmp/input/redp5110-ch1.pdf")


# In[4]:


get_ipython().system('pip install --upgrade numpy')
get_ipython().system('pip install --upgrade pandas')


# In[5]:


get_ipython().system('pip install virtualenv')
get_ipython().system('virtualenv venv')
get_ipython().system('source venv/bin/activate')
get_ipython().system('pip install "data-prep-toolkit-transforms[pdf2parquet]==1.0.0a2" pandas')
#Continue with your notebook from here, but ensure you run all installations within the created virtual environment.


# In[6]:


from dpk_pdf2parquet.transform_python import Pdf2Parquet
from dpk_pdf2parquet.transform import pdf2parquet_contents_types


# In[7]:


Pdf2Parquet(input_folder= "tmp/input",
               output_folder= "tmp/output",
               data_files_to_use=['.pdf', '.zip'],
               pdf2parquet_contents_type=pdf2parquet_contents_types.JSON).transform()


# In[8]:


import pyarrow.parquet as pq
import pandas as pd
table = pq.read_table('tmp/output/archive1.parquet')
table.to_pandas()


# In[9]:


table = pq.read_table('tmp/output/redp5110-ch1.parquet')
table.to_pandas()


# In[10]:


import os

# Print current working directory
print("Current working directory:", os.getcwd())


# In[11]:


# List folders in the current directory
print(os.listdir('.'))

# Check if 'tmp' is in the current directory
if 'tmp' in os.listdir('.'):
    print("Contents of tmp:")
    print(os.listdir('tmp'))
    if 'output' in os.listdir('tmp'):
        print("Contents of tmp/output:")
        print(os.listdir('tmp/output'))


# In[12]:


# Search for the parquet file recursively
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('archive1.parquet'):
            print("Found:", os.path.join(root, file))


# In[13]:


#Use Shell Commands to Search(optional)
get_ipython().system('find . -name "archive1.parquet"')


# In[ ]:




