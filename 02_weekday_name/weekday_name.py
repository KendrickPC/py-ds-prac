# https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
# In Python 3.10, they introduced the pattern matching.

def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if day_of_week == 1:
        return "Sunday"
    elif day_of_week == 2:
        return "Monday"
    elif day_of_week == 3:
        return "Tuesday"
    elif day_of_week == 4:
        return "Wednesday"
    elif day_of_week == 5:
        return "Thursday"
    elif day_of_week == 6:
        return "Friday"
    elif day_of_week == 7:
        return "Saturday"
    else:
        return None

print(weekday_name(1))
print(weekday_name(2))
print(weekday_name(3))
print(weekday_name(4))
print(weekday_name(5))
print(weekday_name(6))
print(weekday_name(7))

print(weekday_name(9))
print(weekday_name(0))
