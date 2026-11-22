
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

from data.dataset import houses


# Separate Features and Target
X = houses[["area", "rooms", "age"]]
y = houses["price"]


# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# Create and Train Model
model = LinearRegression()
model.fit(X_train, y_train)


# Evaluate Model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Training Completed")
print("Predictions:", predictions)
print("Actual Prices:", y_test.values)
print("MAE:", mae)
print("R2:", r2)


# Save Model
joblib.dump(model, "models/house_model.pkl")

print("Model Saved Successfully")
