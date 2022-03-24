# Serve model as a flask application

import numpy as np
from flask import Flask, request
import pandas as pd
import pickle
import os
import tensorflow
import get_the_string as gts

# declare a global variable for our model 
model = None

# bert_dic: {movie id : 768-dimensional vector for movie overview embedding}
bert_dic = {}

# filtered_rank_dic: {movie id : weighted average movie rating score}
filtered_rank_dic = {}

# movie_id_title_dic: {movie_id : movie title}
movie_id_title_dic = {}

# complete_filtered_train_movie_id_dic: {user id : a list of movie ids watched by this user in the training set}
complete_filtered_train_movie_id_dic = {}

# reversed_filtered_user_id_mapping_dic: {user id vocabulary number (0-tot_user_number) : user id}
reversed_filtered_user_id_mapping_dic = {}

# filtered_movie_id_mapping_dic: {movie id : movie id vocabulary number (0-tot number of movies in the training set)}
filtered_movie_id_mapping_dic = {}

# total number of users
tot_user_num = 150244

print('please enter a integer representing a user')
print('For an existing user please enter a number between 0 and {}'.\
        format(tot_user_num-1))
print('For a new user please enter {}'.format(tot_user_num))

user = int(input(''))

def load_model():
    # load our global variables
    global model, bert_dic, filtered_rank_dic, movie_id_title_dic,\
           complete_filtered_train_movie_id_dic, reversed_filtered_user_id_mapping_dic,\
           filtered_movie_id_mapping_dic

    # model variable refers to the global variable
    model = tensorflow.keras.models.load_model('../hybrid.h5')

    with open('../bert_dic_list.txt', 'rb') as fp:
        bert_dic_list = pickle.load(fp)
        for ele in bert_dic_list:
            bert_dic[ele[0]] = ele[1]

    with open('../filtered_rank_dic_list.txt', 'rb') as fp:
        filtered_rank_dic_list = pickle.load(fp)
        for ele in filtered_rank_dic_list:
            filtered_rank_dic[ele[0]] = ele[1]

    with open('../movie_id_vs_movie_title_list.txt', 'rb') as fp:
        movie_id_vs_movie_title_list = pickle.load(fp)
        for ele in movie_id_vs_movie_title_list:
            movie_id_title_dic[ele[0]] = ele[1]

    with open('../complete_filtered_train_movie_id_list.txt', 'rb') as fp:
        complete_filtered_train_movie_id_list = pickle.load(fp)
        for ele in complete_filtered_train_movie_id_list:
            complete_filtered_train_movie_id_dic[ele[0]] = ele[1]

    with open('../filtered_user_id_mapping_list.txt', 'rb') as fp:
        filtered_user_id_mapping_list = pickle.load(fp)
        for ele in filtered_user_id_mapping_list:
            reversed_filtered_user_id_mapping_dic[ele[1]] = ele[0]
    
    with open('../filtered_movie_id_mapping_list.txt', 'rb') as fp:
        filtered_movie_id_mapping_list = pickle.load(fp)
        for ele in filtered_movie_id_mapping_list:
            filtered_movie_id_mapping_dic[ele[0]] = ele[1]

    del bert_dic_list, filtered_rank_dic_list, movie_id_vs_movie_title_list,\
        complete_filtered_train_movie_id_list, filtered_user_id_mapping_list,\
        filtered_movie_id_mapping_list

load_model()

def get_prediction(user, tot_user_num):

    global movie_id_title_dic 

    # if this user is not in the training set
    if user >= tot_user_num:
        predictions = list(filtered_rank_dic.keys())[:10]

        return gts.get_the_string(predictions, movie_id_title_dic)

    rank_dic_copy = filtered_rank_dic.copy()

    # list of movies already rated in train set
    already = complete_filtered_train_movie_id_dic[reversed_filtered_user_id_mapping_dic[user]]

    # remove movies that are already in the train set
    for ele in already:
        rank_dic_copy.pop(ele)

    # save a copy of movie ids
    aaa = list(rank_dic_copy.keys())

    # map movie ids to movie vocabulary number
    X_bert = np.array(pd.Series(np.array(aaa)).map(bert_dic).tolist())

    X_user = np.array([user for i in range(X_bert.shape[0])])

    Y=model.predict([X_user, pd.Series(aaa).map(filtered_movie_id_mapping_dic).values, X_bert])
    Y=Y[:,0]
    Y=list(Y)

    pred=[]

    # add back the weighted average score
    for iii, y in enumerate(Y):
        pred.append([aaa[iii], y+filtered_rank_dic[aaa[iii]]])

    # sort by score from high to low
    pred.sort(key=lambda x : x[1], reverse=True)
    pred=np.array(pred)
    predictions=pred[:10,0]

    return gts.get_the_string(predictions, movie_id_title_dic)


print(get_prediction(user, tot_user_num))


