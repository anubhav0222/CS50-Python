# command line arg[1] ==> source csv ("last, first", house)
# command line arg[2] ==> output csv ("first, last", house)
import sys
import csv

def is_valid_argument():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # elif ".csv" not in sys.argv[1]:
    #     print("Could not read", sys.argv[1])
    else:
        return True

def rearrange_name():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            students = []
            for row in reader:
                name = row[0].split(",") # [last, first]
                new_name = ', '.join([name[-1][1:], name[0]])
                # student = [new_name, row[1]]      # this will make list in list but in output heading will not be there
                student = {"name": new_name, "Place": row[1]}
                students.append(student)

            return students
    except FileNotFoundError:
        sys.exit("Could not read", sys.argv[1])

def write_data(students):
    with open(sys.argv[2], 'w') as file:
        writer = csv.writer(file)
        for student in students:
            writer.writerow(student)


def main():
    if is_valid_argument():
        data = rearrange_name()
        write_data(data)
main()
