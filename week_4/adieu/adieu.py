# https://cs50.harvard.edu/python/2022/psets/4/adieu/

name = []

while True:
    try:
        name.append(input("Name: "))
    except:
        print()
        break

len = len(name)
if len != 1 and len != 2:
    result = ", ".join(name[: len - 1])
    print("Adieu, adieu, to", result + ", and", name[-1])

elif len == 1:
    print("Adieu, adieu, to", name[0])

elif len == 2:
    print("Adieu, adieu, to", name[0], "and", name[1])
