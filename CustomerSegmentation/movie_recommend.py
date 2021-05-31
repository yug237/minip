###########################################################################
# Variables: genre_user_likes and movie_genre_likes
###########################################################################

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
##########################################################################
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]
    
def get_director_from_title(title):
	return df[df.title == title]["director"].values[0]

def get_genre_from_title(title):
    return df[df.title == title]["genres"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

def get_index_from_genre(genre):
    return df4[df4.genres == genre]["index"].values[0]

def clean_string(text):
    text=text.lower()
    return text
#########################################################################

##Step 1: Read CSV File
df = pd.read_excel("movie_dataset.xlsx",engine="openpyxl")

##Step 2: Select Features
features = ['keywords','genres','director']

##Step 3: Create a column in DF which combines all selected features
for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	return row['keywords'] +" "+row["genres"]+" "+row["director"]
	
#Apply function on all rows
df["combined_features"] = df.apply(combine_features,axis=1)

##Step 4: Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

##Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix) 

#Name of the movie that the user likes



## Step 6: Get index of this movie from its title
movie_index = get_index_from_title(movie_user_likes)

## Convert into a list with index and cosine_score
similar_movies =  list(enumerate(cosine_sim[movie_index]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

## Step 8: Print titles of first 50 movies
df1 = pd.DataFrame(columns=['Title','Director'])
print("---------------------------------------------------------------------------------------")
##---------------------------------------------------------------------------------------##

#################################################################################################
# Based on Fav movie of user
print("BASED ON YOUR CHOICE OF "+movie_user_likes+": ")
#################################################################################################
i=0
for element in sorted_similar_movies:
    ## Don't print the name of the same movie
    if(get_title_from_index(element[0])!=movie_user_likes):
        title_name = get_title_from_index(element[0])
        ## df1 prints movie names based on director, genre
        df1 = df1.append({'Title':title_name,'Director':get_director_from_title(title_name)}, ignore_index=True)
        i=i+1
        if i>10:
            break
dict1 = df1.to_dict()
print(dict1)

print("---------------------------------------------------------------------------------------")
#################################################################################################
# Based on Famous movies
print("TRENDING NOW WORLDWIDE: ")
#################################################################################################

df2 = pd.DataFrame(df,columns= ['title','popularity'])

## Sort by popularity index - Descending order
df2.sort_values(by=['popularity'], inplace=True,ascending=False)
dict2=df2[:10].to_dict()
print(dict2)

print("---------------------------------------------------------------------------------------")

#################################################################################################
# Based on release date
print("Latest Releases: ")
#################################################################################################

df3 = pd.DataFrame(df,columns=['title','release_date'])
df3=df3.sort_values(by=['release_date'],ascending=False)

dict3=df3[:10].to_dict()
print(dict3)

print("---------------------------------------------------------------------------------------")
#################################################################################################
# Based on genre of user
print("Based on your genre selection- "+genre_user_likes+":")
#################################################################################################
## User- liked genre goes here

print("Based on your genre selection- "+genre_user_likes+":")

## cosine_similarity
df4=pd.DataFrame(df,columns=['index','title','genres'])
df4 = df4.append({'index':4802,'title':'','genres': genre_user_likes}, ignore_index=True)
cv1 = CountVectorizer()
count_matrix1 = cv1.fit_transform(df4["genres"])

##Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix1)
movie_index1 = get_index_from_genre(genre_user_likes)
similar_genre =  list(enumerate(cosine_sim[movie_index1]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_genre = sorted(similar_genre,key=lambda x:x[1],reverse=True)
df5 = pd.DataFrame(columns=['Title','Genres'])
i=0
for element in sorted_similar_genre:
        title_name = get_title_from_index(element[0])
        df5 = df5.append({'Title':title_name,'Genres':get_genre_from_title(title_name)}, ignore_index=True)
        i=i+1
        if i>10:
            break

dict5=df5[:10].to_dict()
print(dict5)

print("---------------------------------------------------------------------------------------")




