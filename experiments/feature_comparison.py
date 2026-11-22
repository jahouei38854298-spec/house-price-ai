
from data.dataset import houses

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


houses["area_per_room"] = houses["area"] / houses["rooms"]


y = houses["price"]


X_original = houses[["area", "rooms", "age"]]


X_new = houses[["area", "rooms", "age", "area_per_room"]]


X_train_original, X_test_original, y_train, y_test = train_test_split(
    X_original,
    y,
    test_size=0.25,
    random_state=42
)


X_train_new, X_test_new, _, _ = train_test_split(
    X_new,
    y,
    test_size=0.25,
    random_state=42
)


model_original = LinearRegression()
model_original.fit(X_train_original, y_train)

predictions_original = model_original.predict(X_test_original)


model_new = LinearRegression()
model_new.fit(X_train_new, y_train)

predictions_new = model_new.predict(X_test_new)


mae_original = mean_absolute_error(y_test, predictions_original)
r2_original = r2_score(y_test, predictions_original)


mae_new = mean_absolute_error(y_test, predictions_new)
r2_new = r2_score(y_test, predictions_new)


#  results
print("Original Model Results")
print("MAE:", mae_original)
print("R2:", r2_original)

print("\nModel with New Feature Results")
print("MAE:", mae_new)
print("R2:", r2_new)
