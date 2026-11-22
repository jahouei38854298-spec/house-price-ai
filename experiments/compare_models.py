import joblib

from data.dataset import houses

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor




X = houses[["area", "rooms", "age"]]
y = houses["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

decision_predictions = model.predict(X_test)


mae = mean_absolute_error(y_test, decision_predictions)
r2 = r2_score(y_test, decision_predictions)

print("Decision Tree Results")
print("MAE:", mae)
print("R2:", r2)



model = RandomForestRegressor(
    n_estimators= 100 ,
    max_depth= 5 ,
    random_state= 42
)
model.fit(X_train , y_train)
random_predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, random_predictions)
r2 = r2_score(y_test, random_predictions)

print("Random Forest Results")
print("MAE:", mae)
print("R2:", r2)

