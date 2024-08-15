import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip): #----------#.#.#.#
    ip = ip.split(".")

    try:
        if len(ip) == 4:
            if 0 <= int(ip[0]) <= 255:
                if 0 <= int(ip[1]) <= 255:
                    if 0 <= int(ip[2]) <= 255:
                        if 0 <= int(ip[3]) <= 255:
                            return True
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False

    except ValueError:
        return False


...


if __name__ == "__main__":
    main()
