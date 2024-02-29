spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level", 0) > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get("heat_level", 0)
        origin = food.get("cuisine")
        print(f"{food['name']} ({origin}) | Heat Level: {'🌶' * heat_level}")


 
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get("heat_level", 0)
        if heat_level > 5:
            origin = food.get("cuisine")
            print(f"{food['name']} ({origin}) | Heat Level: {'🌶' * heat_level}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    count = 0
    for food in spicy_foods:
        heat_level = food.get("heat_level", 0)
        total_heat += heat_level
        count += 1
    if count == 0:
        return 0
    return total_heat / count

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
