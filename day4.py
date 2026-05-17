import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset (IMPORTANT PATH FIX)
df = pd.read_csv("data/cs-training.csv")

print("Dataset shape:", df.shape)

# Clean missing values
df = df.dropna()

# Target
y = df["SeriousDlqin2yrs"]

# Features
X = df.drop("SeriousDlqin2yrs", axis=1)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))

# Sample comparison
print("Pred:", predictions[:10])
print("Actual:", y_test.values[:10])