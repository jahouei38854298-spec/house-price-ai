
import joblib
import pandas as pd

from pathlib import Path


# مسیر فایل مدل
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "final_house_model.pkl"


# بارگذاری مدل
try:
    model = joblib.load(MODEL_PATH)

except FileNotFoundError:
    print("فایل مدل یافت نشد. لطفاً ابتدا مدل را آموزش دهید.")
    exit()

except Exception as error:
    print("بارگذاری مدل ناموفق بود:", error)
    exit()


print("مدل با موفقیت بارگذاری شد")


# دریافت متراژ خانه
while True:
    try:
        area = float(input("متراژ خانه را وارد کنید: "))

        if 80 <= area <= 180:
            print("متراژ خانه معتبر است")
            break

        print("متراژ خانه باید بین 80 تا 180 متر باشد")

    except ValueError:
        print("لطفاً یک عدد معتبر وارد کنید")


# دریافت تعداد اتاق‌ها
while True:
    try:
        rooms = int(input("تعداد اتاق‌های خانه را وارد کنید: "))

        if 2 <= rooms <= 5:
            print("تعداد اتاق‌ها معتبر است")
            break

        print("تعداد اتاق‌ها باید بین 2 تا 5 باشد")

    except ValueError:
        print("لطفاً یک عدد صحیح معتبر وارد کنید")


# دریافت سن خانه
while True:
    try:
        age = int(input("سن خانه را وارد کنید: "))

        if 1 <= age <= 10:
            print("سن خانه معتبر است")
            break

        print("سن خانه باید بین 1 تا 10 سال باشد")

    except ValueError:
        print("لطفاً یک عدد صحیح معتبر وارد کنید")


# آماده‌سازی اطلاعات خانه
new_house = pd.DataFrame({
    "area": [area],
    "rooms": [rooms],
    "age": [age]
})


# پیش‌بینی قیمت خانه
try:
    prediction = model.predict(new_house)

except Exception as error:
    print("پیش‌بینی ناموفق بود:", error)

else:
    print("قیمت پیش‌بینی‌شده خانه:", round(prediction[0], 2))
