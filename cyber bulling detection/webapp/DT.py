
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.linear_model import  LogisticRegression

from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

import sys
def model():


    try:


        train_data = pd.read_csv("cyberbullying_tweets.csv")
        

        tfidf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True,)


        model = Pipeline([('tfidf', tfidf), ('rf',  DecisionTreeClassifier())])
        model.fit(train_data['tweet_text'], train_data['cyberbullying_type'])
        with open('dt_model.model', 'wb') as f:
            pickle.dump(model, f)
            print("Completed")

    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    model()
