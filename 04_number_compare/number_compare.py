def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if type(a) != int or type(b) != int:
        return "Please enter a valid number"
    if a == b:
        return "Numbers are equal"
    elif a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    else:
        return "Please enter a valid number for the parameters"

print(number_compare(1, 1))
print(number_compare(-1, 1))
print(number_compare(1, -2))
print(number_compare(1, "hi"))
print(number_compare("hello", 100))