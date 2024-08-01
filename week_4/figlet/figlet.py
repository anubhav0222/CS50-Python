# https://cs50.harvard.edu/python/2022/psets/4/figlet/
import pyfiglet
import sys
import random

argv = sys.argv
try:
    """
    figlet.py exits given one command-line argument
    figlet.py exits given invalid first command-line argument
    figlet.py exits given invalid second command-line argument
    """
    if len(argv) == 1 or (
        len(argv) == 3 and argv[1] == "-f" or "--font" and argv[2] in f.getFonts()
    ):
        f = pyfiglet.Figlet()
        text = input("Input: ")
        font_styles = f.getFonts()
        font_style = random.choice(font_styles)
    else:
        sys.exit("Invalid usage")

    # Main conditions
    if len(argv) == 1:
        f = pyfiglet.Figlet(font_style)
        result = f.renderText(text)

    elif len(argv) == 3 and argv[1] == "-f" or "--font" and argv[2] in f.getFonts():
        f = pyfiglet.Figlet(font=argv[2])
        result = f.renderText(text)

    else:
        sys.exit("Invalid usage")

    # Final output
    print(result)
except:
    sys.exit("Invalid usage")
