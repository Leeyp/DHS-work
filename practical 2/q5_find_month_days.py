import calendar
x = 1
while x != 0:
    month = int(input("Input month: "))
    year = int(input("Input year: "))

    print(calendar.month_name[month], year, "has",
          calendar.monthrange(year, month)[1], "days.")
