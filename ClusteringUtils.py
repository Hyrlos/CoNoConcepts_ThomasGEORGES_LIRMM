#!/usr/bin/env python
# coding: utf-8

# # Topic Modeling

# ## import

# In[1]:


from gensim.models import KeyedVectors
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import gensim.downloader as api


# ## Vectorisation

# In[2]:


def document_vector(word2vec_model, doc):
    """
    calculer la moyenne des vecteurs des mots pour chaque fonctionnalité
    """
    # supprimer les mots qui ne sont pas dans le vocabulaire du modèle Word2Vec
    doc = [word for word in doc if word in word2vec_model.key_to_index]
    return np.mean(word2vec_model[doc], axis=0)


# ## Elbow

# In[3]:


def getOptimalClusterNumber(features, feature_vectors):
    # Déterminez le nombre optimal de clusters
    distortions = []
    indexdistortions = []
    sizeMax = len(features)
    for i in range(1, sizeMax):
        km = KMeans(n_clusters=i, init='k-means++', max_iter=100, n_init=1, verbose=0)
        km.fit(feature_vectors)
        indexdistortions.append((i,km.inertia_))
        distortions.append(km.inertia_)

    optimal_k = 0
    minDistor = 10000000000000
    for i, distor in indexdistortions:
        if (minDistor>distor):
            optimal_k = i
            minDistor = distor
    return(optimal_k)   

    


# ## Clustering

# In[4]:


def clustering(feature_vectors, features, n_clusters=5):
    km = KMeans(n_clusters)
    km.fit(feature_vectors)
    clusterList = []
    # afficher les fonctionnalités dans chaque cluster
    for i in range(n_clusters):
        print("Cluster ", i)
        cluster_features = []
        for j in range(len(features)):
            if km.labels_[j] == i:
                cluster_features.append(" ".join(features[j]))
        clusterList.append(cluster_features)
    return clusterList


# ## Naming clusters

# In[5]:


import collections
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def generate_cluster_names(clusters, num_keywords=3):
    """
    Generate cluster names automatically based on the most frequent keywords found in each cluster.
    :param clusters: a list of clusters, where each cluster is a list of documents
    :param num_keywords: the number of keywords to include in each cluster name
    :return: a list of cluster names
    """
    cluster_names = []
    for cluster in clusters:
        # Combine all documents in the cluster into a single string
        cluster_text = ' '.join(cluster)
        # Tokenize the cluster text into words
        words = nltk.word_tokenize(cluster_text) 
        # Remove stop words and punctuation
        words = [word.lower() for word in words 
                 if len(word) > 1 and word.isalpha() and word.lower() not in stopwords.words('english')]

        # Count the frequency of each word
        word_counts = collections.Counter(words)
        # Select the most frequent keywords
        top_keywords = [keyword for keyword, count in word_counts.most_common(num_keywords)]
        # Generate the cluster name
        cluster_name = ' '.join(top_keywords)
        cluster_names.append((cluster_name, cluster))
    return cluster_names


# In[7]:


def loadModel(modelName='word2vec-google-news-300'):
    return api.load(modelName)
    
def getClusterNamed(model, features, n_clusters=5):

    # vectoriser chaque fonctionnalité
    feature_vectors = [document_vector(model, feature) for feature in features]

    clusterList = clustering(feature_vectors, features, n_clusters)

    return generate_cluster_names(clusterList)

