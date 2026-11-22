import joblib
import pandas as pd


model = joblib.load("models/house_pipeline_model.pkl")

print("Pipeline Model Loaded Successfully")


while True:
    try:
        area = float(input("Enter house area: "))

        if 30 <= area <= 300:
            break

        print("Area must be between 30 and 300")

    except ValueError:
        print("Please enter a valid number")


while True:
    try:
        rooms = int(input("Enter number of rooms: "))

        if 1 <= rooms <= 10:
            break

        print("Rooms must be between 1 and 10")

    except ValueError:
        print("Please enter a valid integer")


while True:
    try:
        age = int(input("Enter house age: "))

        if 0 <= age <= 100:
            break

        print("Age must be between 0 and 100")

    except ValueError:
        print("Please enter a valid integer")


house = pd.DataFrame(
    [[area, rooms, age]],
    columns=["area", "rooms", "age"]
)


prediction = model.predict(house)

print("Predicted House Price:", prediction[0])