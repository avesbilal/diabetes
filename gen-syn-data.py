import pandas as pd
import numpy as np

np.random.seed(42)
n = 100000

# Gender distribution
genders = ['female', 'male']
gender_probs = [0.59, 0.41]
gender = np.random.choice(genders, size=n, p=gender_probs)

# Age
age = np.random.randint(8, 91, size=n)

# Hypertension
hypertension = np.random.choice(['yes', 'no'], size=n, p=[0.07, 0.93])

# Heart Disease
heart_disease = np.random.choice(['yes', 'no'], size=n, p=[0.04, 0.96])

# Smoking history with specified probabilities (converted to fractions)
smoking_categories = ['never', 'No info', 'current', 'former', 'ever', 'not current']
smoking_raw_probs = np.array([0.35, 0.36, 0.09, 0.09, 0.04, 0.06])
smoking_probs = smoking_raw_probs / smoking_raw_probs.sum()
smoking_history = np.random.choice(smoking_categories, size=n, p=smoking_probs)

# BMI - continuous values between 18.5 and 40
bmi = np.round(np.random.uniform(10.01, 95.69, size=n), 1)

# HbA1c level
HbA1c_level = np.round(np.random.normal(loc=5.5, scale=1.0, size=n), 1)
HbA1c_level = np.clip(HbA1c_level, 3.5, 9.0)

# Blood glucose level
blood_glucose_level = np.round(np.random.normal(loc=110, scale=30, size=n))
blood_glucose_level = np.clip(blood_glucose_level, 80, 280)

# Diabetes logic
diabetes = np.where((HbA1c_level >= 6.5) | (blood_glucose_level >= 126), 'yes', 'no')

# Create dataframe
df = pd.DataFrame({
    'gender': gender,
    'age': age,
    'hypertension': hypertension,
    'heart_disease': heart_disease,
    'smoking_history': smoking_history,
    'bmi': bmi,
    'HbA1c_level': HbA1c_level,
    'blood_glucose_level': blood_glucose_level,
    'diabetes': diabetes
})

# Add missing values (3-9%) in age, bmi, and blood_glucose_level
for col in ['age', 'bmi', 'blood_glucose_level']:
    missing_pct = np.random.uniform(0.03, 0.09)
    n_missing = int(n * missing_pct)
    missing_indices = np.random.choice(df.index, n_missing, replace=False)
    df.loc[missing_indices, col] = np.nan

# Export CSV
df.to_csv("diabetes.csv", index=False)