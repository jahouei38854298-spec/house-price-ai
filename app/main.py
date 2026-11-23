from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI , HTTPException

from app.schemas import HouseInput , HousePrediction


# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# مسیر فایل مدل
MODEL_PATH = BASE_DIR / "models" / "final_house_model.pkl"


# بارگذاری مدل
model = joblib.load(MODEL_PATH)


# ساخت برنامه FastAPI
app = FastAPI()


# صفحه اصلی API
@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }



@app.get("/health")
def health_check():
    return {
        "status" : "healthy" ,
        "model_loaded" : model is not None
    }



# مسیر پیش‌بینی قیمت خانه
@app.post("/predict", response_model=HousePrediction)
def predict_price(house: HouseInput):

    try:
        new_house = pd.DataFrame({
            "area": [house.area],
            "rooms": [house.rooms],
            "age": [house.age]
        })

        prediction = model.predict(new_house)

        return {
            "area": house.area,
            "rooms": house.rooms,
            "age": house.age,
            "predicted_price": round(float(prediction[0]), 2)
        }
    except Exception as error :
        raise HTTPException(
            status_code= 500 ,
            detail= " خطا در انجام پیش بینی قیمت خانه"
    
        ) from error
    