#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

display(data.head(15))


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.scatter(data['City'], data['Quantity'])

plt.title("Scatter Plot")

plt.xlabel('City')
plt.ylabel('Quantity')

# Simpan plot sebagai file JPG
plt.savefig('scatter.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.plot(data['City'])
plt.plot(data['Quantity'])

plt.title('Line Chart')

plt.xlabel('Quantity')
plt.ylabel('City')

# Simpan plot sebagai file JPG
plt.savefig('line.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.bar(data['City'], data['Quantity'])

plt.title("Bar Chart")

plt.xlabel('City')
plt.ylabel('Quantity')

# Simpan plot sebagai file JPG
plt.savefig('bar.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

plt.hist(data['Year'])
    
plt.title("Histogram")

# Simpan plot sebagai file JPG
plt.savefig('histogram.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[12]:


import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data Sales3.csv", delimiter = ";")

sales = ['Category', 'City']
datasales = [23, 15]

plt.pie(datasales, labels=sales)

plt.title("Pie Chart")

# Simpan plot sebagai file JPG
plt.savefig('pie.jpg', dpi=300, bbox_inches='tight')

plt.show()


# In[ ]:




