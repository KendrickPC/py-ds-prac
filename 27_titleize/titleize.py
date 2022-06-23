def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    results = []
    # allLowerCase = phrase.lower()
    # print(allLowerCase)
    wordsArr =  phrase.split()
    
    for word in wordsArr:
        results.append(word.capitalize())
    return ' '.join(results)

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
