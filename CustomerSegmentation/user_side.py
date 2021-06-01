# Variables are: cust_age and cust_amount

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


warnings.filterwarnings("ignore")
cols=[0,1,2,3]
cols1=[0]
df=pd.read_excel('cust_choices.xlsx',engine='openpyxl',usecols=cols)
df1=pd.read_excel('cust_choices.xlsx',engine='openpyxl',usecols=cols1)

#Elbow-method
from sklearn.cluster import KMeans
wcss = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k, init="k-means++")
    kmeans.fit(df.iloc[:,1:])
    wcss.append(kmeans.inertia_)
#plt.show()

#Final Scatter Plot
km = KMeans(n_clusters=3)
clusters = km.fit_predict(df.iloc[:,1:])
df["label"] = clusters

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df["Age"][df.label == 0], df["Mode"][df.label == 0], df["Amount"][df.label == 0], c='blue', s=60)
ax.scatter(df["Age"][df.label == 1], df["Mode"][df.label == 1], df["Amount"][df.label == 1], c='yellow', s=60)
ax.scatter(df["Age"][df.label == 2], df["Mode"][df.label == 2], df["Amount"][df.label == 2], c='red', s=60)


groups=df.groupby(['label'])

dict1=df.to_dict()
print(dict1)

df.loc[(df.label == 0),'label']='Electronics'
df.loc[(df.label == 1),'label']='Clothing'
df.loc[(df.label == 2),'label']='Essentials'

cust_age=18
cust_amount=1000
categories=['Electronics','Clothing','Essentials']
choices=[]
for i in categories:
	if(cust_age >= int(df['Age'][df["label"]==i].mean())-2 and cust_age <= int(df['Age'][df["label"]==i].mean())+2):
		choices.append(i)
for i in categories:
	if(cust_amount >= int(df['Amount'][df["label"]==i].mean())-500 and cust_amount <= int(df['Amount'][df["label"]==i].mean())+500):
		choices.append(i)
# Choices contains categories in array form
		
choices=list(set(choices))                    # Product Category
my_dict = dict() 
for index,value in enumerate(choices):
  my_dict[index] = value
print(my_dict)


