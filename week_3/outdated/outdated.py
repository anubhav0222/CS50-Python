# https://cs50.harvard.edu/python/2022/psets/3/outdated/

months = ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]
day = 0; month = 0; year = 0

# checking if the given input is "9/8/1636"
def is_first_order(full_date):
    full_date = full_date.split("/")
    try:
        if len(full_date) != 3: return False
        if not 1 <= int(full_date[0]) <= 12: return False
        if not 1 <= int(full_date[1]) <= 31: return False
        if len(full_date[2]) != 4: return False
        return True
    except:
        return False

# Checking if the given input is "September 8, 1636"
def is_second_order(full_date):
    full_date = full_date.split(" ")
    try:
        if ',' not in full_date[1]: return False
        full_date[1] = full_date[1].replace(',', '')
        if len(full_date) != 3: return False
        if not 1 <= int(full_date[1]) <= 31: return False
        if full_date[0].title() not in months: return False
        if len(full_date[2]) != 4: return False
        return True
    except:
        return False

# Main code
while True:
    date = input("Date: ").strip()
    if is_first_order(date):
        date = date.split("/")

        # Updating day, month, year
        day = date[1]; month = date[0]; year = date[2]

        # if 9 ==> 09 for both month and day
        if len(day) == 1: day = "0" + day
        if len(month) == 1: month = "0" + month
        break

    elif is_second_order(date):
        date = date.split(" ")
        date[1] = date[1].replace(',', '')

        # Updating day, month, year
        for i in range(len(months)):
            if date[0].title() in months[i]:
                month = str(i + 1)
        day = date[1]; year = date[2]

        # if 9 ==> 09 for both month and day
        if len(day) == 1: day = "0" + day
        if len(month) == 1: month = "0" + month
        break

# Printing in the formar "YYYY-MM-DD"
print(year + '-' + month + '-' + day)
