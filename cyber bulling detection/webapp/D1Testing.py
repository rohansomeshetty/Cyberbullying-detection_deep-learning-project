import matplotlib.pyplot as plt;
import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

class D1Testing:

    def detecting(test_file, model):

        ##train_news = pd.read_csv(train_file)
        test_ = pd.read_csv(test_file, engine='python')
        
        testdata=test_['cyberbullying_type']
        
        train = pickle.load(open(model, 'rb'))
        predicted_class = train.predict(test_['tweet_text'])
        print('start')

        r=D1Testing.model_assessment(testdata,predicted_class)

        print(r)

        return r

    def model_assessment(y_test, predicted_class):
        l=[]
        
        #Accuracy = (TP + TN) / ALL
        accuracy=((accuracy_score(y_test, predicted_class)))
        accuracy=accuracy*100
       
        accuracy=round(float(accuracy),2)

        l=accuracy
        
        return l



    def main():
        lr=D1Testing.detecting('Testing.csv','lr_model.model')
        rf=D1Testing.detecting('Testing.csv','rf_model.model')
        dt=D1Testing.detecting('Testing.csv','dt_model.model')
        nn=D1Testing.detecting('Testing.csv','nn_model.model')
        cnn=D1Testing.detecting('Testing.csv','cnn_model.model')
        algos = ['Logistic Regression',"Random Forest", "Decision Tree","Neural Network","CNN" ]
        d={}

        from .DBConnection import DBConnection
        mydb = DBConnection.getConnection()
        cursor = mydb.cursor()
        query = "delete from webapp_performance "
        cursor.execute(query)
        mydb.commit()


        query = "insert into webapp_performance( algo, acc)  values(%s,%s)"
        values=(algos[0], str(lr))
        cursor.execute(query, values)

        query = "insert into webapp_performance( algo, acc)  values(%s,%s)"
        values=(algos[1], str(rf))
        cursor.execute(query, values)

        query = "insert into webapp_performance( algo, acc)  values(%s,%s)"
        values=(algos[2], str(dt))
        cursor.execute(query, values)

        query = "insert into webapp_performance( algo, acc)  values(%s,%s)"
        values=(algos[3], str(nn))
        cursor.execute(query, values)

        query = "insert into webapp_performance( algo, acc)  values(%s,%s)"
        values=(algos[4], str(cnn))
        cursor.execute(query, values)

        mydb.commit()

          
    
if __name__ == '__main__':
    D1Testing.main()

	


