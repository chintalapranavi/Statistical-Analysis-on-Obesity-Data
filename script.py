import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

df = pd.DataFrame(data)
df
categorical_features = ['Gender','CALC', 'FAVC', 'SCC', 'SMOKE', 'family_history_with_overweight', 'CAEC', 'MTRANS']
continuous_features = ['Age', 'Height', 'Weight','FCVC', "NCP", 'CH2O' ,'FAF', 'TUE']
target_count = df['NObeyesdad'].value_counts()
target_unique = df['NObeyesdad'].unique()
df_ot = df[df["NObeyesdad"] == 'Obesity_Type_I' ]
df_ot2 = df[df["NObeyesdad"] == 'Obesity_Type_II']
df_ot3 = df[df["NObeyesdad"] == 'Obesity_Type_III']
df_ot_final = pd.concat([df_ot,df_ot2,df_ot3])      # data frem of Obesity_Type I, II, III
df_ot_final.reset_index(drop=True, inplace = True)
df_ow = df[df["NObeyesdad"]=='Overweight_Level_I']
df_ow2 = df[df["NObeyesdad"]=='Overweight_Level_II']
df_ow_final = pd.concat([df_ow,df_ow2])    # data frem of Over_weight_Type I, II
df_ow_final.reset_index(drop=True, inplace = True)
df_n = df[df["NObeyesdad"]=='Normal_Weight']
df_In = df[df["NObeyesdad"]=='Insufficient_Weight']
categorical_features = ['Gender','CALC', 'FAVC', 'SCC', 'SMOKE', 'family_history_with_overweight', 'CAEC', 'MTRANS']
continuous_features = ['Age', 'Height', 'Weight','FCVC', "NCP", 'CH2O' ,'FAF', 'TUE']
df1 = df.copy()
df1.loc[df1['NObeyesdad'] == 'Normal_Weight', 'NObeyesdad'] = 2
df1.loc[df1['NObeyesdad'] == 'Overweight_Level_I', 'NObeyesdad'] = 3
df1.loc[df1['NObeyesdad'] == 'Overweight_Level_II', 'NObeyesdad'] = 4
df1.loc[df1['NObeyesdad'] == 'Obesity_Type_I', 'NObeyesdad'] = 5
df1.loc[df1['NObeyesdad'] == 'Insufficient_Weight', 'NObeyesdad'] = 6
df1.loc[df1['NObeyesdad'] == 'Obesity_Type_II', 'NObeyesdad'] = 7
df1.loc[df1['NObeyesdad'] == 'Obesity_Type_III', 'NObeyesdad'] = 8

        ###################### data to number #################

        # Gender

df1.loc[df1['Gender'] == 'Female', 'Gender'] = 2
df1.loc[df1['Gender'] == 'Male', 'Gender'] = 3

        # family_history_with_overweight

df1.loc[df1['family_history_with_overweight'] == 'no', 'family_history_with_overweight'] = 2
df1.loc[df1['family_history_with_overweight'] == 'yes', 'family_history_with_overweight'] = 3

        # FAVC

df1.loc[df1['FAVC'] == 'no', 'FAVC'] = 2
df1.loc[df1['FAVC'] == 'yes', 'FAVC'] = 3

        # CAEC

df1.loc[df1['CAEC'] == 'no', 'CAEC'] = 2
df1.loc[df1['CAEC'] == 'Sometimes', 'CAEC'] = 3
df1.loc[df1['CAEC'] == 'Frequently', 'CAEC'] = 4
df1.loc[df1['CAEC'] == 'Always', 'CAEC'] = 5

        # SMOKE

df1.loc[df1['SMOKE'] == 'no', 'SMOKE'] = 2
df1.loc[df1['SMOKE'] == 'yes', 'SMOKE'] = 3
        
        # SCC

df1.loc[df1['SCC'] == 'no', 'SCC'] = 2
df1.loc[df1['SCC'] == 'yes', 'SCC'] = 3

        # CALC

df1.loc[df1['CALC'] == 'no', 'CALC'] = 2
df1.loc[df1['CALC'] == 'Sometimes', 'CALC'] = 3
df1.loc[df1['CALC'] == 'Frequently', 'CALC'] = 4
df1.loc[df1['CALC'] == 'Always', 'CALC'] = 5

        # MTRANS

df1.loc[df1['MTRANS'] == 'Automobile', 'MTRANS'] = 2
df1.loc[df1['MTRANS'] == 'Motorbike', 'MTRANS'] = 3
df1.loc[df1['MTRANS'] == 'Bike', 'MTRANS'] = 4
df1.loc[df1['MTRANS'] == 'Public_Transportation', 'MTRANS'] = 5
df1.loc[df1['MTRANS'] == 'Walking', 'MTRANS'] = 6

#########################################################

df1 = df1.astype('float64')

x = df1.drop(columns=["NObeyesdad"])
y = df1["NObeyesdad"].values.reshape(-1, 1)

from sklearn.pipeline import make_pipeline
rfc = make_pipeline( RandomForestClassifier(n_estimators=50))
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
params = rfc.get_params()

accuracy = accuracy_score(y_test, y_pred)

import mlflow
from mlflow.models import infer_signature

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

# Create a new MLflow Experiment
mlflow.set_experiment("Obesity Prediction")

# Start an MLflow run
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log metrics
    mlflow.log_metric("accuracy_score", accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "RandomForestClassifier model")

    # Infer the model signature
    signature = infer_signature(X_train, rfc.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=rfc,
        artifact_path="obesity_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="rfc_model_base_deploy",
    )