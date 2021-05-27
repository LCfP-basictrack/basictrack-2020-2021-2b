# combining data
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
week_day_numbers = [7, 1, 2, 3, 4, 5, 6]

if __name__ == '__main__':

    for day_number, day_name in zip(week_day_numbers, week_days):
        print("The name of day {} is {}".format(day_number, day_name))

    print(list(enumerate(week_days)))
    print(list(zip(week_day_numbers, week_days, week_days, week_day_numbers)))
