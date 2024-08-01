## if the user types 42, forty-two or forty two ==> 'yes' as output, else 'no'

# Getting input
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.strip().lower()

# Condition
if answer == '42' or answer == "forty-two" or answer == "forty two":
    print("yes")
else:
    print("no")
