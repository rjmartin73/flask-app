from datetime import date

year: int = date.today().year


def feb_days(year: int) -> int:
    if (year % 400 == 0 \
            or (year % 4 == 0 and year % 100 != 0)) \
            and year > 0:
        return 29
    else:
        return 28


def get_calendar_data(_year: int = year) -> dict:
    with open('./website/static/holidays.csv', 'r') as f:
        holidays = [tuple(line.split(',')) for line in f.readlines()]

    months = [('January', 31, _year), ('February', feb_days(_year), _year),
              ('March', 31, _year), ('April', 30, _year), ('May', 31, _year),
              ('June', 30, _year), ('July', 31, _year), ('August', 31, _year),
              ('September', 30, _year), ('October', 31, _year),
              ('November', 30, _year), ('December', 31, _year)]
    months_ = dict()
    weekdays_ = list()
    week = dict()

    for index, month in enumerate(months):
        week.clear()
        counter = 1
        position = 0
        additional_text = ""
        # print(counter)
        for _ in range(1, 7):
            weekdays_ = [(), (), (), (), (), (), ()]
            for day in range(1, 8):
                for holiday in holidays:
                    # print(holiday[0], holiday[1], holiday[2])
                    if int(holiday[0]) == index + 1 \
                            and int(holiday[1]) == counter:
                        additional_text += holiday[2] + "<br>"
                if counter <= month[1] and weekdays_[6] == ():
                    if date(_year, index + 1, counter).weekday() == 6:
                        position = 0
                    elif date(_year, index + 1, counter).weekday() == 0:
                        position = 1
                    elif date(_year, index + 1, counter).weekday() == 1:
                        position = 2
                    elif date(_year, index + 1, counter).weekday() == 2:
                        position = 3
                    elif date(_year, index + 1, counter).weekday() == 3:
                        position = 4
                    elif date(_year, index + 1, counter).weekday() == 4:
                        position = 5
                    else:
                        position = 6
                    if date.today().year == _year and \
                        date.today().day == counter \
                            and date.today().month == index + 1:
                        tup = (f"<span class='text-danger'>{counter}</span>",
                               date(_year, index + 1, counter).weekday(),
                               additional_text)
                    else:
                        tup = (counter,
                               date(_year, index + 1, counter).weekday(),
                               additional_text)
                    weekdays_[position] = tup
                else:
                    continue
                counter += 1
                additional_text = ""
            week[_] = weekdays_
        months_[month[0]] = week.copy()
    return months_
