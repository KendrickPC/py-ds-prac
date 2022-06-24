def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    splitStringList = list(s)
    # return splitStringList
    left = 0
    right = len(s)-1
    vowels = 'aeiouAEIOU'
    while left < right:
        if splitStringList[left] in vowels and splitStringList[right] in vowels:
            splitStringList[left], splitStringList[right] = splitStringList[right], splitStringList[left]
            left += 1
            right -= 1
        elif splitStringList[left] in vowels and splitStringList[right] not in vowels:
            right -= 1
        elif splitStringList[right] in vowels and splitStringList[left] not in vowels:
            left += 1
        else:
            left += 1
            right -= 1
    return ('').join(splitStringList)

print(reverse_vowels("au"))
print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
