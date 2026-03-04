import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Create synthetic dataset
data = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56, 48],
    "salary": [20000, 25000, 60000, 80000, 50000, 90000, 65000],
    "purchased": [0, 0, 1, 1, 1, 1, 1]
})

X = data[["age", "salary"]]
y = data["purchased"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")