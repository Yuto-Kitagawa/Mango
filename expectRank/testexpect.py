from numpy import mean
from numpy import std
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import RandomForestClassifier

# データセットを定義
# ここのデータをあらかじめ作る
# n_informationは何でもいい
X, y = make_classification(
    n_samples=1000, n_features=20, n_informative=2, n_redundant=5, random_state=3)
print(X)
# モデルを定義
model = RandomForestClassifier()
# モデルの評価
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
n_scores = cross_val_score(
    model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
# report performance
print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))
