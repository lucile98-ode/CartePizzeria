
def same_ingredients(ingredients_0, ingredients_1):
    for ingredient in ingredients_0:
        if ingredient not in ingredients_1:
            return False
    for ingredient in ingredients_1:
        if ingredient not in ingredients_0:
            return False
    return True

