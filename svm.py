from __future__ import division
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

class SVM:

    def __init__(self):
        """
        Train the model from generated training data.
        """
        data = np.loadtxt('result.csv', delimiter=',')
        X = data[:, 0:3]
        y = data[:, 3].astype(int)

        # Data preprocessing and model pipeline
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier())
        ])

        # Grid search to find best parameters
        param_grid = {
            'classifier__n_estimators': [100, 200, 300],
            'classifier__max_depth': [None, 10, 20, 30],
            'classifier__min_samples_split': [2, 5, 10]
        }

        grid_search = GridSearchCV(pipeline, param_grid, cv=5)
        grid_search.fit(X, y)
        self.model = grid_search.best_estimator_

    def classify(self, data):
        """
        Classify new instances using the trained model.
        """
        try:
            fparams = np.array(data).reshape(1, -1)
            prediction = self.model.predict(fparams)
            print("Input data:", data, "Prediction result:", prediction)
            return prediction
        except Exception as e:
            print("Error during classification:", e)
            return None 

