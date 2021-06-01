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

print('------------------------------------------------------------')
print('\nDetails of customers in cluster: \n')
dict3=df[df['label']==product_desc].to_dict()
print(dict3)
print('------------------------------------------------------------')
print('\nPrinting Cluster related Information: \n')
print('Age analysis:')
age_dict=df['Age'][df['label']==product_desc].describe().to_dict()
print(age_dict)
print('------------------------------------------------------------')

print('AMOUNT analysis:')
amount_dict=df['Amount'][df['label']==product_desc].describe().to_dict()
print(amount_dict)
print('------------------------------------------------------------')

print("OFFLINE SHOPPING: ")
# empty dictionary
mode_dict = {}
mode_dict = {'Offline':df['Mode'][df['label']==product_desc][df['Mode']==0].count(), 'Online':df['Mode'][df['label']==product_desc][df['Mode']==1].count()}
print(mode_dict)
print('------------------------------------------------------------')
print('Analysis of Cluster:')
dict4=df[df['label']==product_desc].describe().to_dict()
print(df[df['label']==product_desc].describe())
print('------------------------------------------------------------')
#print("MAXIMUM VALUES: \n")
#print(df["label"==1].max())
