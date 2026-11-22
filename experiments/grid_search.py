
import joblib

from data.dataset import houses

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

houses["area_per_room"] = houses["area"] / houses["rooms"]

X = houses[["area", "rooms", "age", "area_per_room"]]

y = houses["price"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


model = RandomForestRegressor(random_state=42)


param_grid = {
    "n_estimators": [50, 100, 150, 200],
    "max_depth": [3, 5, 7]
}


grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)


grid_search.fit(X_train, y_train)


print("Best Parameters:")
print(grid_search.best_params_)

print("\nBest CV MAE:")
print(-grid_search.best_score_)


best_model = grid_search.best_estimator_

joblib.dump(best_model , "models/best_house_model.pkl")

print("Best Model Saved Successfully")

predictions = best_model.predict(X_test)



print("\nFinal Model Results")
print("MAE:", mean_absolute_error(y_test, predictions))
print("R2:", r2_score(y_test, predictions))
