RECIPE_FILE = "recipes.txt"

def save_recipes(recipes):
    # Save recipes to text file
    with open(RECIPE_FILE, 'w') as f:
        for name, details in recipes.items():
            f.write(f"{name}\n")
            f.write(f"{','.join(details['ingredients'])}\n")
            f.write(f"{details['instructions']}\n")
            f.write("-----\n")

def load_recipes():
    # Load recipes from text file
    recipes = {}
    try:
        with open(RECIPE_FILE, 'r') as f:
            current_recipe = None
            for line in f:
                line = line[:-1]  # Remove newline character only
                if line == "-----":
                    current_recipe = None
                    continue
                
                if current_recipe is None:
                    # First line is recipe name
                    current_recipe = line
                    recipes[current_recipe] = {'ingredients': [], 'instructions': ""}
                elif not recipes[current_recipe]['ingredients']:
                    # Second line is ingredients
                    if line:  # Only split if line isn't empty
                        recipes[current_recipe]['ingredients'] = line.split(',')
                else:
                    # Third line is instructions
                    recipes[current_recipe]['instructions'] = line
    except FileNotFoundError:
        pass
    return recipes

def add_recipe():
    # Add a new recipe
    print("\n=== Add New Recipe ===")
    name = input("Recipe name: ")
    ingredients = input("Ingredients (comma separated): ").split(',')
    instructions = input("Instructions: ")
    
    recipes = load_recipes()
    recipes[name] = {
        'ingredients': ingredients,
        'instructions': instructions
    }
    save_recipes(recipes)
    print(f"\nRecipe '{name}' added successfully!")

def view_recipe():
    # View a recipe
    print("\n=== View Recipe ===")
    name = input("Enter recipe name: ")
    recipes = load_recipes()
    
    if name in recipes:
        print(f"\nRecipe: {name}")
        print("Ingredients:")
        for ing in recipes[name]['ingredients']:
            print(f"- {ing}")
        print("\nInstructions:")
        print(recipes[name]['instructions'])
    else:
        print("Recipe not found!")

def list_recipes():
    # List all recipes
    print("\n=== All Recipes ===")
    recipes = load_recipes()
    
    if not recipes:
        print("No recipes found!")
    else:
        for i, name in enumerate(recipes.keys(), 1):
            print(f"{i}. {name}")

def delete_recipe():
    # Delete a recipe
    print("\n=== Delete Recipe ===")
    name = input("Enter recipe name to delete: ")
    recipes = load_recipes()
    
    if name in recipes:
        del recipes[name]
        save_recipes(recipes)
        print(f"Recipe '{name}' deleted!")
    else:
        print("Recipe not found!")

def main_menu():
    """Display main menu"""
    while True:
        print("\n=== Recipe Book ===")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. List Recipes")
        print("4. Delete Recipe")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipe()
        elif choice == '3':
            list_recipes()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            print("Bye")
            break
        else:
            print("Invalid choice. Please try again.")
main_menu()