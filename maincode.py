
# Importing Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('disease_data.csv')

# Display the first few rows of the dataset
print(data.head())

# Encode categorical features
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['symptoms'] = data['symptoms'].apply(lambda x: ' '.join(x.split(',')))
data['symptoms'] = label_encoder.fit_transform(data['symptoms'])

# Extract features and labels
X = data.drop('disease', axis=1)
y = label_encoder.fit_transform(data['disease'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training and Evaluating Machine Learning Models

# K-Nearest Neighbors (KNN)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"KNN Accuracy: {accuracy_knn * 100:.2f}%")

# Weighted KNN
weighted_knn = KNeighborsClassifier(weights='distance')
weighted_knn.fit(X_train, y_train)
y_pred_weighted_knn = weighted_knn.predict(X_test)
accuracy_weighted_knn = accuracy_score(y_test, y_pred_weighted_knn)
print(f"Weighted KNN Accuracy: {accuracy_weighted_knn * 100:.2f}%")

# Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)
accuracy_gnb = accuracy_score(y_test, y_pred_gnb)
print(f"Gaussian Naive Bayes Accuracy: {accuracy_gnb * 100:.2f}%")

# Fine, Medium, and Coarse Decision Trees
for criterion in ['gini', 'entropy']:
    for max_depth in [5, 10, None]:
        dt = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth)
        dt.fit(X_train, y_train)
        y_pred_dt = dt.predict(X_test)
        accuracy_dt = accuracy_score(y_test, y_pred_dt)
        print(f"Decision Tree ({criterion}, max_depth={max_depth}) Accuracy: {accuracy_dt * 100:.2f}%")

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {accuracy_rf * 100:.2f}%")

# Bagging (Subspace KNN)
bagging_knn = BaggingClassifier(base_estimator=KNeighborsClassifier(), n_estimators=10, random_state=42)
bagging_knn.fit(X_train, y_train)
y_pred_bagging_knn = bagging_knn.predict(X_test)
accuracy_bagging_knn = accuracy_score(y_test, y_pred_bagging_knn)
print(f"Bagging KNN Accuracy: {accuracy_bagging_knn * 100:.2f}%")

# Hyperparameter tuning for KNN
param_grid = {
    'n_neighbors': [3, 5, 7, 9],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan', 'minkowski']
}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
best_knn = grid_search.best_estimator_
y_pred_best_knn = best_knn.predict(X_test)
accuracy_best_knn = accuracy_score(y_test, y_pred_best_knn)
print(f"Best KNN Accuracy: {accuracy_best_knn * 100:.2f}%")

# Summary of Results
print(f"Summary of Model Accuracies:")
print(f"KNN Accuracy: {accuracy_knn * 100:.2f}%")
print(f"Weighted KNN Accuracy: {accuracy_weighted_knn * 100:.2f}%")
print(f"Gaussian Naive Bayes Accuracy: {accuracy_gnb * 100:.2f}%")
print(f"Random Forest Accuracy: {accuracy_rf * 100:.2f}%")
print(f"Bagging KNN Accuracy: {accuracy_bagging_knn * 100:.2f}%")
print(f"Best KNN Accuracy after Hyperparameter Tuning: {accuracy_best_knn * 100:.2f}%")
