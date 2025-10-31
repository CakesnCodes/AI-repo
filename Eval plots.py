import numpy as np
import matplotlib.pyplot as plt

scores = ['Accuracy', 'Precision', 'Recall', 'F1']
c1 = [0.5045, 0.5440, 0.8014, 0.6481]
c2 = [0.5353, 0.5028, 0.9985, 0.6688]

plt.figure() #for a bar chart that shows evaluation metrics for both Honeybee and Fireblight
w, x = 0.4, np.arange(len(scores))
plt.bar(x - w/2, c1, w, label='Honeybee', color='yellow')
plt.bar(x + w/2, c2, w, label='Fireblight', color='red')

plt.xticks(x,scores)
plt.ylabel('Score')
plt.title('Evaluation metrics of Honeybee and Fireblight')

plt.show()

plt.figure() #Honeybee's evaluation metrics
plt.bar(scores, c1, color='yellow')
plt.xticks(scores)
plt.ylabel('Score')
plt.title('Evaluation metrics of Honeybee')

plt.show()

plt.figure() #Fireblight's evaluation metrics
plt.bar(scores, c2, color='red')
plt.xticks(scores)
plt.ylabel('Score')
plt.title('Evaluation metrics of Fireblight')


plt.show()

