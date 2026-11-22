
import joblib
import pandas as pd

try:
    model = joblib.load("models/house_model.pkl")

except FileNotFoundError:
    print("فایل مدل یافت نشد. لطفاً ابتدا مدل را آموزش دهید")
    exit()


print("Model Loaded Successfully")

while True:
    try:
        area = float(input("Enter house area: "))
        if area >= 30 and area <= 180 :
            print("متراژ خانه معتبر")
            break
        print("متراژ خانه باید بین 30 تا 180 متر باشد")

    except ValueError:
        print("لطفا یک عدد معتبر وارد کنید")

while True:
    try:
        rooms = int(input("Enter house rooms: "))
        if rooms >=2 and rooms<=5 :
            print("تعداد اتاق ها معتبر")
            break
        print("تعداد اتاق ها بایدبین 2 تا 5 باشد")

    except ValueError:
        print("لطفا یک عدد صحیح معتبر وارد کنید")

while True:
    try:
        age = int(input("Enter house age: "))
        if age>=1 and age<= 10 :
            print("سن معتبر")
            break
        

        print("سن خانه باید بین 1 تا 10 باشد")

    except ValueError:
        print("لطفا یک عدد صحیح معتبر وارد کنید")


new_house = pd.DataFrame({
    "area": [area],
    "rooms": [rooms],
    "age": [age]
})

try:
    prediction = model.predict(new_house)

except Exception as error:
    print("پیش بینی ناموفق بود", error)
else:
    print("قیمت پیش بینی خانه:", prediction[0])
