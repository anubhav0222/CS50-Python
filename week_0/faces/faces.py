## Programme to convert :) to 🙂 and convert :( to 🙁

# Function to do that
def convert(string):
    string = string.replace(":)", '🙂')
    string = string.replace(":(", '🙁')
    return string

# The mains function
def main():
    string = input("Enter your string with emoticons: ")
    print(convert(string))

# Calling the main function
main()
