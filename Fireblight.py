import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("apple_quality.csv") # Created by Nidula Elgiriyewithana

quality = df['Quality'].values.tolist()


def Fireblight():
    pquality = [] #create new list
    for apple,row in df.iterrows():#for every apple in each row
        points = 0
        sweet = row['Sweetness']
        juice = row['Juiciness']
        acid = row['Acidity']
        crunch = row['Crunchiness']
        ripe = row['Ripeness']
        if sweet < -3: points += 1
        if juice <= -2: points += 1
        if acid <= -3: points += 1
        if crunch >= 0: points += 1
        if ripe < -1 or ripe > 4: points += 1

        if points >= 3: pquality.append("bad") #If there are 3 or more negative qualities spotted, label apple as bad
        else: pquality.append("good") #otherwise, label apple as good
        
    return pquality

new_col = pd.DataFrame({"Predicted Quality":Fireblight()})
df = pd.concat([df, new_col], axis=1)


