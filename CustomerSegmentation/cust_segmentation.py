import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
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
plt.figure(figsize=(12,6))    
plt.grid()
plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")
plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")
#plt.show()

#Final Scatter Plot
km = KMeans(n_clusters=3)
clusters = km.fit_predict(df.iloc[:,1:])
df["label"] = clusters

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df["Age"][df.label == 0], df["Mode"][df.label == 0], df["Amount"][df.label == 0], c='blue', s=60)
ax.scatter(df["Age"][df.label == 1], df["Mode"][df.label == 1], df["Amount"][df.label == 1], c='yellow', s=60)
ax.scatter(df["Age"][df.label == 2], df["Mode"][df.label == 2], df["Amount"][df.label == 2], c='red', s=60)
ax.view_init(30, 185)
plt.xlabel("Age")
plt.ylabel("Mode")
ax.set_zlabel('Amount')
#plt.show()
#print(df)

df.loc[(df.label == 0),'label']='Electronics'
df.loc[(df.label == 1),'label']='Clothing'
df.loc[(df.label == 2),'label']='Essentials'
#df.loc[(df.label == 3),'label']='Stationary'
#df.loc[(df.label == 4),'label']='Beverages'

groups=df.groupby(['label'])

dict1=df.to_dict()
print(dict1)
print('------------------------------------------------------------')
print('Analysis of data:')
dict2=df.describe().to_dict()
print(dict2)
print('------------------------------------------------------------')
