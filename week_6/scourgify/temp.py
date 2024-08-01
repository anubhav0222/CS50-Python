# command line arg[1] ==> source csv ("last, first", house)
# command line arg[2] ==> output csv ("first, last", house)
import sys
import csv

def is_valid_argument():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        return True

def rearrange_name():
    try:
        with open("before.csv") as file:
            reader = csv.reader(file)
            students = []
            for row in reader:
                name = row[0].split(",") # [last, first]
                new_name = ''.join([name[-1], name[0]])
                student = [new_name, row[1]]

            return students
    except FileNotFoundError:
        sys.exit("Could not read before.csv")

def write_data(students):
    with open("name.csv", 'a') as file:
        writer = csv.writer(file)
        for row in students:
            writer.writerow([row[0], row[1]])

def main():
    data = rearrange_name()
    write_data(data)
main()
