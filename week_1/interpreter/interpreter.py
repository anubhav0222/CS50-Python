# import re (ye bala module bhi elplore kra ja sakta hai)

# Getting input
expression = input("Expresion: ").strip()
expression = expression.split()
no_1 = int(expression[0])
no_2 = int(expression[2])
ope = expression[1]
ans = 0.0

# Conditions
if ope == '+':
    ans = no_1 + no_2

elif ope == '-':
    ans = no_1 - no_2

elif ope == '*':
    ans = no_1 * no_2

elif ope == '/':
    ans = no_1 / no_2

else:
    print("Error")

ans = float(ans)
ans = round(ans, 2)
print(ans)
