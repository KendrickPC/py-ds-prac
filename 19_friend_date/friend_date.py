# https://stackoverflow.com/questions/740287/how-to-check-if-one-of-the-following-items-is-in-a-list

def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    aHobbies = a[2]
    bHobbies = b[2]
    results = [i for i in aHobbies if i in bHobbies]
    if results == []:
        return False
    else:
        return True
    # return aHobbies

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

print(friend_date(elmo, sauron))
print(friend_date(sauron, gandalf))