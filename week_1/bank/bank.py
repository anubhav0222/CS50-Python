## Get the input and if it is == "hello" ==> $0 if it's first char == 'h' ==> $20 else ==> $100 [CASE INSENSITIVE]

# Getting input
greeting = input("Greeting: ")
greeting = greeting.strip().lower()

# Cases
if "hello" in greeting:
    print("$0")
elif greeting[0] == 'h':
    print("$20")
else:
    print("$100")
