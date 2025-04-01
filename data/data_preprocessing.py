import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE  # For handling class imbalance

# Load dataset
df = pd.read_csv("data/synthetic_fraud_data.csv")

# 1️⃣ Handle missing values (if any)
print("Checking for missing values...")
print(df.isnull().sum())

# Fill missing values (if any)
df.fillna(df.mean(), inplace=True)

# 2️⃣ Encode categorical variables (transaction_type, transaction_time)
label_encoder = LabelEncoder()
df["transaction_type"] = label_encoder.fit_transform(df["transaction_type"])
df["transaction_time"] = label_encoder.fit_transform(df["transaction_time"])

# 3️⃣ Scale numeric features
scaler = StandardScaler()
df[["transaction_amount", "location_risk", "device_risk", "customer_history"]] = (
    scaler.fit_transform(
        df[["transaction_amount", "location_risk", "device_risk", "customer_history"]]
    )
)

# 4️⃣ Split dataset into train and test sets
X = df.drop("is_fraud", axis=1)  # Features
y = df["is_fraud"]  # Target variable

# Split into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Handle class imbalance using SMOTE (Synthetic Minority Over-sampling Technique)
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Save processed data for further use
X_train_resampled.to_csv("data/X_train_resampled.csv", index=False)
X_test.to_csv("data/X_test.csv", index=False)
y_train_resampled.to_csv("data/y_train_resampled.csv", index=False)
y_test.to_csv("data/y_test.csv", index=False)

print("✅ Data preprocessing complete!")
