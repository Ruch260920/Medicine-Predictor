# Medicine-Predictor

Disease Prediction from Various Symptoms using Machine Learning
Overview
This project aims to develop a disease prediction system using multiple machine learning (ML) algorithms. The system analyzes symptoms, age, and gender of individuals to predict potential diseases with high accuracy. The Weighted KNN algorithm provided the best results, achieving an accuracy of 93.5%.

Table of Contents
Project Structure
Installation
Usage
Data Collection and Preprocessing
Model Training and Evaluation
Results
Visualization
Contributing
License
Project Structure
The project is organized into the following directories and files:
ssrn-3661426.pdf: Research paper detailing the methodology and results.
README.md: Project documentation.
mainCode.py: code used
Installation
To set up the project on your local machine, follow these steps:

Clone the repository from GitHub.
Create and activate a virtual environment.
Install the required dependencies listed in requirements.txt.
Usage
To preprocess the data, train the model, and evaluate it, run the respective scripts located in the src directory. Alternatively, you can refer to the research paper for a detailed explanation of the methodology and results.

Data Collection and Preprocessing
Data Collection: Collected a dataset with more than 230 diseases and over 1000 unique symptoms.
Data Cleaning: Processed the text data to remove noise, handle punctuation, and standardize the format.
Feature Engineering: Symptoms, age, and gender were used as input features for the ML models.
Model Training and Evaluation
Models Used:
Fine, Medium, and Coarse Decision Trees
Gaussian Naïve Bayes
Kernel Naïve Bayes
Fine, Medium, and Coarse KNN
Weighted KNN
Subspace KNN
RUSBoosted Trees
Training: The data was split into training and testing sets, and each model was trained using the training set.
Evaluation: Model performance was evaluated using accuracy metrics. The Weighted KNN model achieved the highest accuracy of 93.5%.
Results
The Weighted KNN model provided the highest accuracy for disease prediction. The model's ability to handle varying values of K and give more weight to closer points contributed to its superior performance.

Visualization
Visualizations were created to compare the performance of different ML models. Training and validation metrics were plotted to assess model convergence and accuracy.

