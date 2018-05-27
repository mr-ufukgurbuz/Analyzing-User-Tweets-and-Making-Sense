globalVowels = "aeıioöuüAEIİOÖUÜ"

def StartCapital(term):
    return term[0].isupper()

def AllCapital(term):
    for i in range(0, term.__len__()):
        if not term[i].isupper():
            return False

    return True

def CapitalRatio(term):
    capitalCount = 0

    for i in range(0, term.__len__()):
        if term[i].isupper():
            capitalCount += 1

    return capitalCount/term.__len__()

# Length function already exist in python!


def VowelRatio(term):
    vowelCount = 0

    for i in range(0, term.__len__()):
        for j in range(0, globalVowels.__len__()):
            if term[i] == globalVowels[j]:
                vowelCount += 1
                break

    return vowelCount/term.__len__()


def NumberOfVowel(term):
    vowelCount = 0

    for i in range(0, term.__len__()):
        for j in range(0, globalVowels.__len__()):
            if term[i] == globalVowels[j]:
                vowelCount += 1
                break

    return vowelCount


def NumberOfConsonant(term):
    consonantCount = 0

    for i in range(0, term.__len__()):
        if term[i].isalpha():
            for j in range(0, globalVowels.__len__()):
                if term[i] == globalVowels[j]:
                    break
                elif term[i] != globalVowels[j] and j == globalVowels.__len__() - 1:
                    consonantCount += 1
        else:
            continue

    return consonantCount


def NumberOfDigits(term):
    digitCount = 0

    for i in range(0, term.__len__()):
        if term[i].isdigit():
            digitCount += 1

    return digitCount


def DigitRatio(term):
    digitCount = NumberOfDigits(term)

    return digitCount/term.__len__()


def NumberOfNonAlphanumeric(term):
    nonalphaCount = 0

    for i in range(0, term.__len__()):
        if not term[i].isalnum():
            nonalphaCount += 1

    return nonalphaCount


def NonAlphanumericRatio(term):
    nonalphaCount = NumberOfNonAlphanumeric(term)

    return nonalphaCount/term.__len__()


def AllConsonant(term):
    consonantCount = NumberOfConsonant(term)

    return consonantCount == term.__len__()


def StartHashtag(term):
    return term[0] == "#"


def StartMention(term):
    return term[0] == "@"


def AllDigits(term):
    digitsCount = NumberOfDigits(term)

    return digitsCount == term.__len__()
