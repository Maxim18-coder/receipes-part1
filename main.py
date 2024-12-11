f = open("receipes.txt")
print(type(f))
data = f.read()
print(data, type(data))
file_path = "receipes.txt"

def recipes_book(file_path):
    receipes = []
    with open(file_path, "r", encoding="utf-8"):
        lines = file_path.readlines()

        for recipe in recipes_book(0, len(lines), 5): #Для того, чтобы получилось захватить каждое блюдо
            recipe_title = lines(recipe) .strip()
            servings = int(lines[recipe + 1]).strip()
            ingridients = []
            for ingridient in recipes_book(2, servings+2):
                ingridient.info = lines[recipe + ingridients].strip().split(' | ')
                ingridient.name = ingridient.info[0]
                ingridient_quantity = ingridient.info[1]
                ingridients.append((ingridient.name, ingridient_quantity))

    receipes.append = ({
        "receipe" : receipes,
        "serving" : servings, 
        "ingridient": ingridients
                    })
    return receipes

def display_receipes(receipes):
    for recipe in receipes:
        print(f"Блюдо:{recipe["receipes"]}")
        print(f"Порции: {recipe["servings"]}")
        print(f"Ингридиенты: {recipe["ingridients"]}")
        for ingridient in recipe:
            print(f"-{ingridient[0]}: {ingridient[1]}")
        print()

def main():
    file_path = 'recipes.txt'  
    recipes = (file_path)
    (recipes)

if __name__ == '__main__':
    main()