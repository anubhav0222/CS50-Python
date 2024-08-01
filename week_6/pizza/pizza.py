# https://cs50.harvard.edu/python/2022/psets/6/pizza/
from tabulate import tabulate
import sys

def len_of_argv():
    # command line argv => the CSV file sys.argv[1]
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        pass

def print_table(file_name):
        with open(file_name) as file:
            table = []
            for line in file:
                table.append(line.rstrip().split(","))
            # print(tabulate(table, headers, tablefmt="grid"))
            print(tabulate(table[1:], table[0], tablefmt="grid"))

def main():
    len_of_argv()
    try:
        print_table(sys.argv[1])
    except:
        sys.exit("file not found")

if __name__ == "__main__":
    main()
