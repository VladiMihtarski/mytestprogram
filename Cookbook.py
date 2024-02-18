def cookbook(*args):
    # Initialize a dictionary to store recipes grouped by cuisine
    cuisine_recipes = {}

    # Count the number of recipes in each cuisine
    for recipe_name, cuisine, ingredients in args:
        if cuisine not in cuisine_recipes:
            cuisine_recipes[cuisine] = []
        cuisine_recipes[cuisine].append((recipe_name, ingredients))

    # Sort cuisines by the number of recipes (descending) and then alphabetically
    sorted_cuisines = sorted(cuisine_recipes.keys(), key=lambda x: (-len(cuisine_recipes[x]), x))

    # Prepare the result string
    result = ""

    # Iterate over sorted cuisines
    for cuisine in sorted_cuisines:
        # Add cuisine and the number of recipes to the result
        result += f"{cuisine} cuisine contains {len(cuisine_recipes[cuisine])} recipes:\n"

        # Sort recipes alphabetically by recipe name
        sorted_recipes = sorted(cuisine_recipes[cuisine], key=lambda x: x[0])

        # Add each recipe and its ingredients to the result
        for recipe_name, ingredients in sorted_recipes:
            result += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"

    return result
