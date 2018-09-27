def oneAway(word, word2):
    if len(word) - len(word2) > 1:
        return False
    
    letterCount = {}
    count = 0

    for letter in word:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    
    for letter in word2:
        if letter in letterCount:
            letterCount[letter] -= 1

    for x, y in letterCount.items():
        count += y

    if len(word) == len(word2):
        if count == 0:
            return True
        return False
    elif len(word) > len(word2):
        if count == 1:
            return True
        return False
    else:
        if count == -1:
            return True
        return False

print(oneAway('godg', 'dogg')) # True
print(oneAway('drog', 'dog')) # True