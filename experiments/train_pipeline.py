import joblib

from data.dataset import houses

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


X = houses[["area", "rooms", "age"]]
y = houses["price"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)


model = Pipeline([
    ("scaler", StandardScaler()),
    ("regression", LinearRegression())
])


model.fit(X_train, y_train)


predictions = model.predict(X_test)


mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)


print("Model Training Completed")
print("MAE:", mae)
print("R2:", r2)


joblib.dump(model, "models/house_pipeline_model.pkl")

print("Pipeline Model Saved Successfully")