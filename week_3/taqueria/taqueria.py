# https://cs50.harvard.edu/python/2022/psets/3/taqueria/
d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0

while True:
    try:
        order = input("Item: ").title()
        if order not in d.keys():
            continue
        else:
            cost += d[order]
            print("Total: $" + str(cost))
    except EOFError:
        print()
        break
