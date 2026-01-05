import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.tree import plot_tree
from matplotlib import pyplot as plt

df = pd.read_csv("weatherAUS.csv")

df = df.dropna()

X = df[['Humidity3pm']]
y = df['RainTomorrow']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt = DecisionTreeClassifier(random_state=42) #Kookaburra sits in the old gum tree

dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, pos_label= 'Yes')
precision = precision_score(y_test, y_pred, pos_label= 'Yes')
f1 = f1_score(y_test, y_pred, pos_label= 'Yes')

print("Decision Tree Evaluation")
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')

print(f'F1 Score: {f1:.4f}')

