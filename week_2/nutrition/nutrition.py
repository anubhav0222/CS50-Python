# https://cs50.harvard.edu/python/2022/psets/2/nutrition/

item = input("Item: ").lower()
chart = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60,
         "grapes": 90, "honeydewmelon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20,
         "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50,
         "plums": 70, "Strawberries": 50, "sweet cherries": 100, "Tangerine": 50,
         "watermelon": 80}

for i in chart.keys():
    if i == item:
        print("Calories: ", chart[i])
