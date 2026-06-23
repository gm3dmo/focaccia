def bread_ingredients_by_flour(flour_amount):
    # Original recipe (anchor: flour = 500g)
    ratios = {
        'water': 340 / 500,
        'sugar': 20 / 500,
        'salt': 10 / 500,
        'yeast': 10 / 500,
        'oil': 30 / 500
    }
    ingredients = {'flour': flour_amount}
    for name, ratio in ratios.items():
        ingredients[name] = round(flour_amount * ratio, 2)
    return ingredients

#d Example usage:
for flour in [1906]:
    print(f"For {flour}g flour: {bread_ingredients_by_flour(flour)}")
