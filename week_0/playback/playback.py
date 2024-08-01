## code to get input and replace every space with '...' (i.e., 3 periods)

# Asking for input
string = input("Enter you string: ")

# Removing trailing white spaces
string = string.strip()

# Changing every space to '...'
string = string.replace(" ", "...")

print(string)
