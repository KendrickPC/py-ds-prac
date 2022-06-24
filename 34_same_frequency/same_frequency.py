# https://www.codegrepper.com/code-examples/python/python+split+int+into+list
# “python split int into list”

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1List = [int(i) for i in str(num1)]
    num1List.sort()

    num2List = [int(i) for i in str(num2)]
    num2List.sort()
    
    return num1List == num2List

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
