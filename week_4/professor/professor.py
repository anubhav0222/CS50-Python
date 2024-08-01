# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    level = get_level()
    chances = 3
    index = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = input(f"{x} + {y} = ")

        try:
            if int(ans) == x+y:
                index += 1
                continue
            else:
                print("EEE")
                while True:
                    ans = input(f"{x} + {y} = ")
                    if type(ans) == int and ans == (x + y):
                        index += 1
                        chances = 3
                        break
                    elif chances == 2:
                        print(f"{x} + {y} =", x+y)
                        chances = 3
                        break
                    else:
                        chances -= 1
                        continue

        except:
            print("EEE")
            while True:
                ans = input(f"{x} + {y} = ")
                if type(ans) == int and ans == (x + y):
                    chances = 3
                    break
                elif chances == 2:
                    print(f"{x} + {y} =", x+y)
                    chances = 3
                    break
                else:
                    chances -= 1
                    continue
    print(index)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except:
            continue


def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)
    elif level == 2:
        num = random.randint(10, 99)
    elif level == 3:
        num = random.randint(100, 999)
    else:
        return ValueError
    return num

if __name__ == "__main__":
    main()
