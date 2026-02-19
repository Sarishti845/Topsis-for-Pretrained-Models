import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")

models = data.iloc[:, 0]
decision_matrix = data.iloc[:, 1:].values

weights = np.array([1, 1, 1, 1, 1, 1])
weights = weights / np.sum(weights)


impacts = np.array(['+', '+', '+', '+', '-', '-'])


norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))


weighted_matrix = norm_matrix * weights


ideal_best = []
ideal_worst = []

for i in range(len(impacts)):
    if impacts[i] == '+':
        ideal_best.append(np.max(weighted_matrix[:, i]))
        ideal_worst.append(np.min(weighted_matrix[:, i]))
    else:
        ideal_best.append(np.min(weighted_matrix[:, i]))
        ideal_worst.append(np.max(weighted_matrix[:, i]))

ideal_best = np.array(ideal_best)
ideal_worst = np.array(ideal_worst)

distance_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
distance_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))


scores = distance_worst / (distance_best + distance_worst)

rank = scores.argsort()[::-1] + 1


data['TOPSIS Score'] = scores
data['Rank'] = data['TOPSIS Score'].rank(ascending=False)


data.to_csv("result.csv", index=False)

print(data)


plt.figure()
plt.bar(models, scores)
plt.xlabel("Models")
plt.ylabel("TOPSIS Score")
plt.title("TOPSIS Ranking - Text Classification Models")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graph.png")
plt.show()
