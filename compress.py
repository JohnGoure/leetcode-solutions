def compress(word):
    letterCount = {}
    compress = False

    for letter in word:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
        if letterCount[letter] > 1:
            compress = True
    
    if compress == True:
        compressedWord = ""
        for letter in letterCount:
            compressedWord += letter
            compressedWord += str(letterCount[letter])
        return compressedWord
    return word

print(compress('John'))