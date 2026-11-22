from data.dataset import houses

houses["area_per_room"] = houses["area"]/houses["rooms"]

print(houses[["area", "rooms", "area_per_room"]].head())