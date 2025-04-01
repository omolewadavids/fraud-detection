import pandas as pd
import numpy as np
import random

# Define parameters
NUM_TRANSACTIONS = 10_000
FRAUD_RATIO = 0.05  # 5% fraudulent transactions

# Define transaction categories
transaction_types = ["online_purchase", "ATM_withdrawal", "bank_transfer"]
time_of_day = ["morning", "afternoon", "night"]


# Generate normal transactions
def generate_normal_transaction():
    return {
        "transaction_amount": np.random.normal(
            loc=100, scale=50
        ),  # Avg $100 transaction
        "transaction_time": np.random.choice(
            time_of_day, p=[0.5, 0.4, 0.1]
        ),  # Most during day
        "transaction_type": np.random.choice(transaction_types),
        "location_risk": np.random.randint(1, 4),  # Low-moderate risk
        "device_risk": np.random.randint(1, 3),  # Mostly safe devices
        "customer_history": np.random.randint(1, 5),  # Frequent users
        "is_fraud": 0,  # Normal transaction
    }


# Generate fraudulent transactions
def generate_fraud_transaction():
    return {
        "transaction_amount": np.random.uniform(500, 10_000),  # Large amounts
        "transaction_time": np.random.choice(
            time_of_day, p=[0.1, 0.2, 0.7]
        ),  # Most at night
        "transaction_type": np.random.choice(transaction_types),
        "location_risk": np.random.randint(3, 6),  # High-risk areas
        "device_risk": np.random.randint(2, 5),  # High-risk devices
        "customer_history": np.random.randint(0, 2),  # New or inactive customers
        "is_fraud": 1,  # Fraudulent transaction
    }


# Create dataset
num_fraud = int(NUM_TRANSACTIONS * FRAUD_RATIO)
num_normal = NUM_TRANSACTIONS - num_fraud

normal_transactions = [generate_normal_transaction() for _ in range(num_normal)]
fraud_transactions = [generate_fraud_transaction() for _ in range(num_fraud)]

# Combine and shuffle dataset
data = normal_transactions + fraud_transactions
random.shuffle(data)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/synthetic_fraud_data.csv", index=False)
print(f"✅ Synthetic dataset saved with {len(df)} transactions!")
