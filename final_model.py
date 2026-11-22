
import joblib

from data.dataset import houses

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# Features and target
X = houses[["area", "rooms", "age"]]
y = houses["price"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# Train final model
model = LinearRegression()

model.fit(X_train, y_train)


# Evaluate model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)


print("Final Linear Regression Model")
print("MAE:", mae)
print("R2:", r2)


# Save model
joblib.dump(model, "models/final_house_model.pkl")

print("Final Model Saved Successfully")
