import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.split("<")     # <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    s = s[1].split(" ")
    for i in range(len(s)):
        if 'src=' in s[i]:
            return s[i][5:-1]
    return None

if __name__ == "__main__":
    main()
