import joblib

model = joblib.load("models/best_house_model.pkl")
print("Model Loaded Successfully")

print(type(model))