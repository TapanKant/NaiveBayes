# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:02:01 2019

@author: Tapan Kant
"""

import pandas as pd


def load_data(fileName):
    """ 
    this function is used to load data from a CSV file 
    
    """
    data = pd.read_csv(fileName)
    return data

def calculate_prob_col(data, colName):
    """
    calculates the number of accurance for a given column (responder)
    """
    col_name_set = set(data[colName])
    #data_len = len(data)
    prob = []
    for c in col_name_set:
        count = len([k for k in data[colName] if k == c])
        prob.append([c,(count)])
    prob = pd.DataFrame(prob, columns = ['cols','count'])
    return prob

def calculate_prob_with_respect_to(data, respective_column_name, to_column_name):
    """
    calculates the probability with responder
    """
    res_col_name = set(data[respective_column_name])
    #to_col_name = set(data[to_column_name])
    prob = calculate_prob_col(data, to_column_name)
    #print(prob,len(prob))
    prob_with_respect = []
    for r_c_name in res_col_name:
        #prob_c_name = [k for k in data[respective_column_name] if k == r_c_name]
        #print(prob_c_name)
        for i in range(0, len(prob)):
            prob_dict = dict(prob.loc[i])
            print(respective_column_name, r_c_name)
            print('prob ', prob_dict['cols'])
            count = 0
            dataLength = len(data)
            for i in range(0,dataLength):
                temp_dict = dict(data.loc[i])
                if prob_dict['cols'] == temp_dict[to_column_name] and temp_dict[respective_column_name] == r_c_name:
                    print(prob_dict)
                    print(temp_dict)
                    count += 1
            print('count :', count)
            prob_with_respect.append([r_c_name, prob_dict['cols'], count/prob_dict['count']])
    prob_with_respect = pd.DataFrame(prob_with_respect, columns = ['to','with','prob'])
    return (prob_with_respect)

def train_NaiveBayes(data, predict_col_name):
    """
    train the data with responder column and returns nested list
    """
    cols = list(data.columns)
    prob_list = []
    for c in cols:
        if c != predict_col_name:
            temp = calculate_prob_with_respect_to(data, c, predict_col_name)
            prob_list.append(temp)
    return prob_list