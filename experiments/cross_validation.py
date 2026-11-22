import joblib
from data.dataset import houses
from sklearn.model_selection import cross_val_score

model = joblib.load("models/house_pipeline_model.pkl")

X =houses [["area", "rooms", "age"]]
y =houses ["price"]

scores = cross_val_score(
    model,
    X,
    y,
    cv= 5,
    scoring="neg_mean_absolute_error"
)

mae_scores = - scores

print("MAE scores:" , mae_scores)

print("Average MAE" , mae_scores.mean())