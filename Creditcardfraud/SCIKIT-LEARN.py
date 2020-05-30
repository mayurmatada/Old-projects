import pandas as pd
import numpy as np
import sklearn.externals.joblib
import sklearn.model_selection
import sklearn.ensemble
import sklearn as sk

n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
min_samples_split = [2, 5, 10]
min_samples_leaf = [1, 2, 4]
bootstrap = [True, False]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

data = pd.read_csv('C:\\Users\\Mayur\\source\\repos\\Creditcardfraud\\creditcard.csv')

fraud = data[data['Class'] == 1]
nonfraud = data[data['Class'] == 0]

nonfraud = nonfraud.sample(492)
dataset = fraud.append(nonfraud, ignore_index = True)
dataset = dataset.sample(frac=1)

y = dataset['Class']
x = dataset.drop('Class', axis = 1)

y_train, y_test, x_train, x_test = sk.model_selection.train_test_split(y, x, test_size = 0.2)

rf = sk.ensemble.RandomForestClassifier()
rf_random = sk.model_selection.RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 2, verbose=2, random_state=42, n_jobs = -1)
rf_random.fit(x_train, y_train)

accuracy = rf_random.score(x_test, y_test)
print("Accuracy of trained model: " + str(accuracy))

sk.externals.joblib.dump(rf_random, 'sklearn-model.pkl', compress = 1)