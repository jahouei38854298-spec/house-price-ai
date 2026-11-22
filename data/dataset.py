
import pandas as pd
import numpy as np


np.random.seed(42)


areas = np.random.randint(80, 181, size=100)
rooms = np.random.randint(2, 6, size=100)
ages = np.random.randint(1, 11, size=100)


area_noise = np.random.normal(0, 3, size=100)
noisy_areas = areas + area_noise


noise = np.random.normal(0, 0, size=100)

prices = (
    areas * 30
    + rooms * 200
    - ages * 50
    + noise
)


data = {
    "area": noisy_areas,
    "rooms": rooms,
    "age": ages,
    "price": prices
}


houses = pd.DataFrame(data)
