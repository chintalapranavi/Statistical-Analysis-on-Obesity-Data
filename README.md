Project Overview

This project aims to address the growing public health issue of obesity through the application of machine learning and statistical analysis. Using a dataset of 17 variables, including dietary habits, physical activity, and other lifestyle factors, we developed models to predict obesity levels in individuals from Mexico, Peru, and Colombia. Our best model, Random Forest, achieved an accuracy of 99%, and a web application was built to provide personalized health recommendations based on the predictions.

Key Features

Dataset: We used a dataset from the study conducted by Palechor and de la Hoz Manotas (2019), consisting of 2,111 entries with 17 features including age, weight, height, family history of overweight, caloric intake, and physical activity levels.
Machine Learning Models: We implemented multiple models, including:
Random Forest (Best performance with 99% accuracy)
Multinomial Logistic Regression
Support Vector Machine (SVM)
Linear Discriminant Analysis (LDA)
k-Nearest Neighbors (kNN)
Naive Bayes
Decision Tree
Neural Network
Model Evaluation: We utilized metrics such as accuracy, sensitivity, and specificity to evaluate the models. K-fold cross-validation was applied to enhance model reliability.
Exploratory Data Analysis (EDA): Data visualization techniques were employed to uncover patterns within the dataset. Key visualizations included histograms, scatter plots, violin plots, and correlation heatmaps.
Feature Selection: The most significant features for obesity level prediction were identified through stepwise forward and backward selection. Top features included weight, height, age, and alcohol consumption frequency.
Web Application: A Streamlit-based web application was developed that allows users to input their data and receive predictions about their obesity level, along with personalized health suggestions.
Methodology

Data Preprocessing: Conversion of categorical variables, handling of missing data, normalization, and data splitting (80% training, 20% testing).
Model Training: Various machine learning models were trained and evaluated based on accuracy, sensitivity, and specificity.
K-Fold Cross Validation: All models were further validated using 5-fold cross-validation to ensure generalizability.
App Development: A user-friendly web interface was built to allow real-time predictions and recommendations.
Results

Best Performing Model: The Random Forest model achieved the highest accuracy (99%), perfect sensitivity (1.00), and specificity (1.00), demonstrating its reliability for obesity level prediction.
Other Models: Multinomial Logistic Regression and SVM also performed well with accuracies of 96.6% and 90%, respectively. Neural Networks and Decision Trees were less effective, with Neural Networks achieving the lowest accuracy.
Technologies Used

Programming Language: R, Python
Packages:
R: ggplot2, caret, randomForest, dplyr, e1071, MASS
Python: Streamlit for app development
Tools: RStudio, Streamlit, MLflow for model tracking
Web Application

The web application allows users to:

Input personal data (age, weight, height, lifestyle factors).
Receive a prediction of their obesity level.
Obtain personalized recommendations to improve health.
