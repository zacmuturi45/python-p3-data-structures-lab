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
    return [n["name"] for n in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [n for n in spicy_foods if n["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        print(f"{n['name']} ({n['cuisine']}) | Heat Level: " + "\U0001F336" * n['heat_level'])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for n in spicy_foods:
        for n in spicy_foods:
            if n['cuisine'] == cuisine:
                return n

def print_spiciest_foods(spicy_foods):
    for n in spicy_foods:
        if n['heat_level'] > 5:
            print(f"{n['name']} ({n['cuisine']}) | Heat Level: " + n['heat_level'] * "\U0001F336")

def get_average_heat_level(spicy_foods):
    x = 0
    for n in spicy_foods:
        x += n['heat_level']
    return x / len(spicy_foods)


spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
