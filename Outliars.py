# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 13:59:25 2025

@author: User
"""


import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("apple_quality.csv") # Created by Nidula Elgiriyewithana

quality = df['Quality'].values.tolist()


def casndra():
    pquality = []
    for apple,row in df.iterrows():
        points = 0
        sweet = row['Sweetness']
        acid = row['Acidity']
        juice = row['Juiciness']
        crunch = row['Crunchiness']
        ripe = row['Ripeness']
        if sweet > -3: points += 1
        if acid > -3 and acid < 3:points += 1
        if juice >= -2: points += 1
        if crunch > 0: points += 1
        if ripe > -1 and ripe <2: points += 1

        if points >= 4: pquality.append("good")

        else:pquality.append("bad")
        
    return pquality

new_col = pd.DataFrame({"Predicted Quality":casndra()})
df = pd.concat([df, new_col], axis=1)

    
