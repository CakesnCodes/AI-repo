import numpy as np
import matplotlib.pyplot as plt

scores = ['Accuracy', 'Precision', 'Recall', 'F1']
c1 = [0.7821, 0.5489, 0.0588, 0.1061]
c2 = [0.7821, 0.6226, 0.0266, 0.0509]

plt.figure()
w, x = 0.4, np.arange(len(scores))
plt.bar(x - w/2, c1, w, label='Decision Tree', color='green')
plt.bar(x + w/2, c2, w, label='Logistic Regression', color='blue')

plt.xticks(x,scores)
plt.ylabel('Score')
plt.title('Evaluation metrics of Decision Tree and Logistic Regression')

plt.legend(loc='upper right')

plt.show()


plt.figure()
plt.bar(scores, c1, color='green')
plt.xticks(scores)
plt.ylabel('Score')
plt.title('Evaluation metrics of Decision Tree')

plt.show()

plt.figure()
plt.bar(scores, c2, color='blue')
plt.xticks(scores)
plt.ylabel('Score')
plt.title('Evaluation metrics of Logistic Regression')


plt.show()
