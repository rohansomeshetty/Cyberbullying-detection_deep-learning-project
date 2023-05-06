
import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class CNN:

    def detecting(stmt):
        int2label = {0: "not_cyberbullying", 1: "age", 2: "gender", 3: "religion", 4: "other_cyberbullying", 5: "ethnicity"}
        stmt=[stmt]
        filename = 'cnn_model.model'
        train = pickle.load(open(filename, 'rb'))
        predicted_class = train.predict(stmt)
        return int2label[predicted_class[0]]

if __name__ == "__main__":
    print(CNN.detecting("bye see you "))

