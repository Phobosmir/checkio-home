"""
What’s your favourite day of the week? Check if it's the most common day of the week in a year.

You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of the week in that particular year. The result has to be a list of days sorted by the order of days in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.

Input: Year as an int.

Output: The list of most common days sorted by the order of days in a week (from Monday to Sunday).

Example:

most_frequent_days(1084) == ['Tuesday', 'Wednesday']
most_frequent_days(1167) == ['Sunday']
1
2
Preconditions: Year is between 1 and 9999. Week starts with Monday.
"""
import datetime
import calendar


def most_frequent_days(year):
    d = datetime.date(year=year, month=1, day=1)
    res = {weekday: 0 for weekday in range (7)}
    while d.year != year+1:
        res[d.weekday()] += 1
        d += datetime.timedelta(days=1)

    most_freq = [k for k, v in res.items() if v == max(res.values())]
    weekday_names = {wd: i for wd, i in zip(range(7), calendar.weekheader(9).split())}

    r = [weekday_names[d] for d in most_freq]
    return r


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
