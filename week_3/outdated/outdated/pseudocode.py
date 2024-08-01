'''
day, month, year = 0
is_first_type():            # 9/8/1636
    date = split"/"
    try:
        if len(date) != 3 ==> False
        if not int(date[0]) 0 to 12 ==> False
        if not int(date[1]) 1 to 31 ==> False
        if len(date[2]) != 4 ==> False
        return True
    except:
        return False

is_second_type():           # September 8, 1636
    date = split" "

    try:
        if ',' not in date[1] ==> False
        date[1].replace(',', " ")
        if len(date) != 3 ==> False
        if not int day 1 to 31 ==> False
        if month not in months ==> False
        if len(year) != 4 ==> False
        return True
    except:
        return False

while True:
    if is_first_order(date):
        date = split"/"

        day, month, year = put the value
        if len(day), len(month) == 1 ==> "0" + day or month

        break

    if is_second_order(date):
        date = split" "
        date[1].replace(',', "")

        for i in months ==> put index of Sep in month
        put date in day and yr in year

        if len(day), len(month) == 1 ==> "0" + day or month

        break

print(year + '-' + month + "-" + day)

'''
