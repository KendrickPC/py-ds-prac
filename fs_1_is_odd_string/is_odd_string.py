def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
        1 + 13 + 1 + 26 + 9 + 14 + 7
        >>> is_odd_string('amazing')
        True
    """
    # Hint: you may find the ord() function useful here
    # https://www.w3schools.com/python/ref_func_ord.asp
    # The ord() function returns the number representing the unicode code of a specified character.

    # Translate everything to lower:
    # Minus 96:
    count = 0
    transformToLower = word.lower()
    for char in transformToLower:
        count += ord(char) - 96
    # print(F"Count: {count}")
    return count % 2 != 0
    
"""
x = ord("a")
y = ord("A")
print(x) # 97
print(y) # 65
"""

print(is_odd_string('a'))
print(is_odd_string('A'))
print(is_odd_string('aaaa'))
print(is_odd_string('AAaa'))
print(is_odd_string('amazing'))
