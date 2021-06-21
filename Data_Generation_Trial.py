#!/usr/bin/env python
# coding: utf-8

# In[1]:


from DataGeneratorTransformer import TransformerDataGenerator


# In[2]:


import requests
import time
import pandas as pd
import numpy as np
# NEW URl 
REST_API_URL = 'https://api.powerbi.com/beta/e4e34038-ea1f-4882-b6e8-ccd776459ca0/datasets/ba060660-19a2-4d65-b367-ac9ce692a673/rows?key=u%2Bzz9JHhONuwE4xzlH5T6GLhws6S3xrJ6B3k7pAD%2FgtkIT3bDYWUwiCPVGZAYlF%2B27yo5MdOmg9KqECg%2BqX42Q%3D%3D'
tf=TransformerDataGenerator()
while True:
    data_raw = []
    for i in range(1):
        tf_json = tf.data_generator()[0]
    data_json = bytes(tf_json, encoding='utf-8')
    print(data_json)
    #print("JSON dataset", data_json)

    # Post the data on the Power BI API
    req = requests.post(REST_API_URL, data_json)

    print("Data posted in Power BI API")
    time.sleep(2)


# In[ ]:





# In[ ]:




