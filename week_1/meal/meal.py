def main():
    # ...
    ask_time = input("What time is it? ") # ask_time == 7:30
    no = convert(ask_time) # no == 7.5

    if 7.0 <= no <= 8.0:
        print("breakfast time")

    elif 12.0 <= no <= 13.0:
         print("lunch time")

    elif 18.0 <= no <= 19.0:
        print("dinner time")


def convert(time):
    # ... time == 7:30 --> 7.5
    time = time.split(":")  # time == ['7', '30']
    min = int(time[1])/60 # min == 0.5
    ntime = int(time[0]) + min
    return ntime




if __name__ == "__main__":
    main()
