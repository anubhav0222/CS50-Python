# https://cs50.harvard.edu/python/2022/psets/2/coke/

amount_due =  50
acceptable_currency = [5, 10, 25]
amount_received = 0

while (amount_received < 50):
    print("Amount Due: ", amount_due)
    inserted_value = int(input("Insert Coin: "))

    if inserted_value in acceptable_currency:
        amount_due = amount_due - inserted_value
        amount_received += inserted_value

print("Change Owed: ", amount_due * -1)



