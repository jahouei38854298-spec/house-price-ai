import numpy as np
import pandas as pd

areas = np.random.randint(80,181, size=100)

rooms = np.random.randint(2,6, size=100)

ages = np.random.randint(1,11, size=100)

price = (areas*30) + (rooms*200)- (ages*50)


data= {
    "area":areas,
    "rooms":rooms,
    "age":ages,
    "price":price
}


houses = pd.DataFrame(data)

print(houses.head())
print (houses.shape)


