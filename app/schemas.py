from pydantic import BaseModel,Field

class HouseInput (BaseModel) :
    area : float = Field(
        ge= 80,
        le= 180,
        description= "متراژ خانه"   
        )

    rooms : int = Field(
        ge= 2,
        le= 5,
        description="تعداد اتاق ها"
    )

    age : int = Field (
        ge= 1,
        le= 10, 
        description= "سن خانه"
    )


class HousePrediction (BaseModel) :
    area : float
    rooms : int
    age : int
    predicted_price : float