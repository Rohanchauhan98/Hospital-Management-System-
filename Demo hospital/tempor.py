import pandas as pd
import sklearn as sk
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle  # Import pickle for saving the model

# 1. LOAD THE DATA
df1 = pd.read_csv("C:\hrt\heart.csv")
df1.info()

# 2. REMOVE NULL
df1.isnull()
df1.dropna(inplace=True)

# 3. REMOVE OUTLIER
ch_mean = df1['chol'].mean()
std_dev = df1['chol'].std()

z_scores = (df1['chol'] - ch_mean) / std_dev

print("Z-Scores:")
print(z_scores)

outliers = df1[abs(z_scores) > 3]

df_new = df1[abs(z_scores) <= 3]
print("\nOutliers removed DataFrame:")
print(df_new)

# 4. CATEGORIAL --- NUMERICAL
categorical_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
df_new = pd.get_dummies(df_new, columns=categorical_columns, drop_first=True)
print("\nCategorical data:")
print(df_new)

# 5. NORMALIZE
print(df1)
df_max_scaled = df_new.copy()

column1 = ['chol', 'age', 'trestbps', 'thalach']
for column in df_max_scaled.columns:
    df_max_scaled[column1] = df_max_scaled[column1] / df_max_scaled[column1].abs().max()

print("\nNormalized data:")
print(df_max_scaled)

# 6. CORRELATION
import pandas as pd
import numpy as np

covariance1 = np.cov(df_max_scaled['chol'], df_max_scaled['age'])
covariance2 = np.cov(df_max_scaled['chol'], df_max_scaled['trestbps'])
covariance3 = np.cov(df_max_scaled['chol'], df_max_scaled['thalach'])
print("Covariance between 'chol' and 'age': ", covariance1)
print("Covariance between 'chol' and 'trestbps': ", covariance2)
print("Covariance between 'chol' and 'thalach': ", covariance3)

import matplotlib.pyplot as plt

plt.matshow(df_max_scaled.corr())
plt.show()

# Load in model
x = df_max_scaled[['age', 'trestbps', 'thalach']]
y = df_max_scaled[['chol']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)
regr = svm.SVR(kernel='rbf')
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)
print("\nPredicted values:\n", y_pred)

r2 = r2_score(y_test, y_pred)
print("\nR^2 Score: ", r2)
mse = mean_squared_error(y_test, y_pred)
print("\nMean Sq Error: ", mse)

# Save the trained model to a .pkl file using pickle
model_filename = 'heart_disease_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(regr, file)
print(f"\nModel saved as {model_filename}")