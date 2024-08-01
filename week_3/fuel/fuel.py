# https://cs50.harvard.edu/python/2022/psets/3/fuel/
while True:
    fraction = input("Fraction: ") # 12/2
    fraction = fraction.split("/") # ['12', '2']
    try:
        x = int(fraction[0]) # x = 12
        y = int(fraction[1]) # y = 2
        z = x/y # z = 6
        if x > y:
            continue
    except (ValueError, ZeroDivisionError):
        continue
    else:
        break

z = z * 100
z = round(z)

if z >= 99:
    print("F")
elif z <= 1:
    print("E")
else:
    print(str(z) + "%")
