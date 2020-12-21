lines = [line.strip() for line in open("q21.txt", "r")]

all_ingredients = {}
suspects = {}

for line in lines:
    raw_ingredients, raw_allergens = line.split("(contains", 1)
    ingredients = raw_ingredients.strip().split(" ")
    for ingredient in ingredients:
        all_ingredients[ingredient] = all_ingredients.get(ingredient, 0) + 1

    allergens = raw_allergens.strip(")").strip().split(", ")
    for alg in allergens:
        if alg not in suspects:
            suspects[alg] = set(ingredients)
            continue

        suspects[alg] &= set(ingredients)

suspect_ingredients = set()
for ings in suspects.values():
    suspect_ingredients |= ings

count = 0
for ing in all_ingredients:
    if ing not in suspect_ingredients:
        count += all_ingredients[ing]

print("PART 1", count)

unsure = True
while unsure:
    unsure = False
    for alg, ings in suspects.items():
        if len(ings) > 1:
            unsure = True
        else:
            for other_alg in suspects:
                if alg != other_alg:
                    suspects[other_alg] -= ings

allergens = sorted(suspects.keys())
ing_list = [suspects[alg].pop() for alg in allergens]
print("PART 2", ",".join(ing_list))