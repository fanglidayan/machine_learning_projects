# Serve model as a flask application

import numpy as np
from flask import Flask, request
# from keras.models import load_model
# import keras
import tensorflow
import pandas as pd
import h5py
import pickle

model = None
bert_dic = None
filtered_rank_dic=None
app = Flask(__name__)


def load_model():
    global model, bert_dic, filtered_rank_dic
    # model variable refers to the global variable
    # with open('hybrid.h5', 'rb') as f:
    model = tensorflow.keras.models.load_model('hybrid.h5')
    with open('bert_dic_list.txt', 'rb') as fp:
        bert_dic_list=pickle.load(fp)
        bert_dic={}
        for ele in bert_dic_list:
            bert_dic[ele[0]]=ele[1]
    with open('filtered_rank_dic_list.txt', 'rb') as fp:
        filtered_rank_dic_list=pickle.load(fp)
        filtered_rank_dic={}
        for ele in filtered_rank_dic_list:
            filtered_rank_dic[ele[0]]=ele[1]

@app.route('/')
def home_endpoint():
    return "To make movie recommendations for an existing user, please input an integer between 0 and 150244."+\
            "\n"+"For a new user, please enter 150255."


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        X_user = np.array([int(request.get_json())])  # Get data posted as a json
        if X_user[0]>150244:
            prediction=filtered_rank_dic[4306]
            prediction=float(str(prediction)[:5])
            return 'the predicted movie rating for movie 7 and a new user is {}'\
                    .format(prediction)+'\n'

        X_movie = np.array([7])
        X_bert = np.array(pd.Series(np.array([4306])).map(bert_dic).to_list()) 
        # runs globally loaded model on the data
        prediction = model.predict([X_user, X_movie, X_bert])[0, 0]  
        prediction+=filtered_rank_dic[4306]
        if prediction<1: prediction=1
        elif prediction>5: prediction=5
        prediction=float(str(prediction)[:5])
        
    return 'the predicted movie rating for movie 7 and user {} is {}'\
            .format(X_user[0], prediction)+'\n'


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
