
import joblib
import pandas as pd


model = joblib.load("models/best_house_model.pkl")

print("Best Model Loaded Successfully")


area = float(input("Enter house area: "))
rooms = int(input("Enter number of rooms: "))
age = float(input("Enter house age: "))


area_per_room = area / rooms


new_house = pd.DataFrame([{
    "area": area,
    "rooms": rooms,
    "age": age,
    "area_per_room": area_per_room
}])


predicted_price = model.predict(new_house)

print("Predicted House Price:", predicted_price[0])
