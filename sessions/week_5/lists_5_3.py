from sessions.week_5.tuples_5_2 import week_days

if __name__ == '__main__':

    print(" | ".join(week_days[1:4]))   # slice

    for day in week_days[-3:-1]:
        print(day)

    # have a look at the "brighten.py" in week6 for list comprehension.
