# https://cs50.harvard.edu/python/2022/psets/3/grocery/

count = 0
total_items = {}
while True:
    try:
        item = input("Item: ")
        if item in total_items:
            total_items[item] += 1
        else:
            total_items[item] = 1

    except EOFError:
        print()
        break

for item in total_items:
    print(total_items[item], item.upper())
