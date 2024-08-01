# https://cs50.harvard.edu/python/2022/psets/2/plates/

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #1.  s.isalnum() = False ==> not possible
    for i in s:
        if not i.isalnum():
            return False

    #2.  num beech me nhi, end me hi possible and concecutive
    temp = 100000 # just a random big number for line 21
    for n in range(len(s)):
        if s[n].isdigit():
            temp = n
        elif s[n].isalpha() and temp < n:
            return False

    #3.  first no not '0'
    num = 0
    for k in range(len(s)):
        if s[k].isdigit() and num == 0:
            num = 1
            if s[k] == '0':
                return False

    #4.  2 <= len(s) <= 6
    if not 2 <= len(s) <= 6 :
        return False

    #5.  staring ke 2 letters alpha
    # if not ((s[0] >= 'a' and s[0] <= 'z') or (s[0] >= 'A' and s[0] <= 'Z') and (s[1] >= 'a' and s[1] <= 'z') or (s[1] >= 'A' and s[1] <= 'Z')):
    if (s[0].isdigit() and s[1].isdigit()): #full stopes and other will be handled by condition 1
        return False

    # if all conditions satisfyies
    return True

main()
