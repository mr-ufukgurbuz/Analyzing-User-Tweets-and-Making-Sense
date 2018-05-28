import FeatureFunctions as FF
import pandas as pd

#load the data
data = pd.read_csv("documentTokenAll.csv", header=None)

tokens = []
docIDs = []
tokenIDs = []
targets = []

for i in range(1, data.get_values().__len__()):
    docIDs.append(data.get_values()[i][0])
    tokenIDs.append(data.get_values()[i][1])
    tokens.append(data.get_values()[i][2])
    targets.append(data.get_values()[i][4])

StrtCptList = []
AllCptList = []
CptRatioList = []
LengthList = []
VwlRatioList = []
NoVwlList = []
NoCnsList = []
NoDigitList = []
DigitRatioList = []
NoNonAlphaList = []
NonAlphaRatioList = []
AllCnsList = []
HashtagList = []
MentionList = []
AllDigitList = []

PrevStrtCptList = []
PrevAllCptList = []
PrevCptRatioList = []
PrevLengthList = []
PrevVwlRatioList = []
PrevNoVwlList = []
PrevNoCnsList = []
PrevNoDigitList = []
PrevDigitRatioList = []
PrevNoNonAlphaList = []
PrevNonAlphaRatioList = []
PrevAllCnsList = []
PrevHashtagList = []
PrevMentionList = []
PrevAllDigitList = []

NextStrtCptList = []
NextAllCptList = []
NextCptRatioList = []
NextLengthList = []
NextVwlRatioList = []
NextNoVwlList = []
NextNoCnsList = []
NextNoDigitList = []
NextDigitRatioList = []
NextNoNonAlphaList = []
NextNonAlphaRatioList = []
NextAllCnsList = []
NextHashtagList = []
NextMentionList = []
NextAllDigitList = []

PrevTokenList = []
NextTokenList = []

for i in range(0, tokens.__len__()):
    StrtCptList.append(FF.StartCapital(tokens[i]))
    AllCptList.append(FF.AllCapital(tokens[i]))
    CptRatioList.append(FF.CapitalRatio(tokens[i]))
    LengthList.append(tokens[i].__len__())
    VwlRatioList.append(FF.VowelRatio(tokens[i]))
    NoVwlList.append(FF.NumberOfVowel(tokens[i]))
    NoCnsList.append(FF.NumberOfConsonant(tokens[i]))
    NoDigitList.append(FF.NumberOfDigits(tokens[i]))
    DigitRatioList.append(FF.DigitRatio(tokens[i]))
    NoNonAlphaList.append(FF.NumberOfNonAlphanumeric(tokens[i]))
    NonAlphaRatioList.append(FF.NonAlphanumericRatio(tokens[i]))
    AllCnsList.append(FF.AllConsonant(tokens[i]))
    HashtagList.append(FF.StartHashtag(tokens[i]))
    MentionList.append(FF.StartMention(tokens[i]))
    AllDigitList.append(FF.AllDigits(tokens[i]))

    if i != 0 and docIDs[i-1] == docIDs[i] and int(tokenIDs[i-1]) == (int(tokenIDs[i])-1):
        PrevStrtCptList.append(StrtCptList[i-1])
        PrevAllCptList.append(AllCptList[i-1])
        PrevCptRatioList.append(CptRatioList[i-1])
        PrevLengthList.append(LengthList[i-1])
        PrevVwlRatioList.append(VwlRatioList[i-1])
        PrevNoVwlList.append(NoVwlList[i-1])
        PrevNoCnsList.append(NoCnsList[i-1])
        PrevNoDigitList.append(NoDigitList[i-1])
        PrevDigitRatioList.append(DigitRatioList[i-1])
        PrevNoNonAlphaList.append(NoNonAlphaList[i-1])
        PrevNonAlphaRatioList.append(NonAlphaRatioList[i-1])
        PrevAllCnsList.append(AllCnsList[i-1])
        PrevHashtagList.append(HashtagList[i-1])
        PrevMentionList.append(MentionList[i-1])
        PrevAllDigitList.append(AllDigitList[i-1])
        PrevTokenList.append(tokens[i-1])
    else:
        PrevStrtCptList.append('')
        PrevAllCptList.append('')
        PrevCptRatioList.append('')
        PrevLengthList.append('')
        PrevVwlRatioList.append('')
        PrevNoVwlList.append('')
        PrevNoCnsList.append('')
        PrevNoDigitList.append('')
        PrevDigitRatioList.append('')
        PrevNoNonAlphaList.append('')
        PrevNonAlphaRatioList.append('')
        PrevAllCnsList.append('')
        PrevHashtagList.append('')
        PrevMentionList.append('')
        PrevAllDigitList.append('')
        PrevTokenList.append('')

    if i != tokens.__len__()-1 and docIDs[i] == docIDs[i+1] and int(tokenIDs[i]) == (int(tokenIDs[i+1])-1):
        NextStrtCptList.append(FF.StartCapital(tokens[i+1]))
        NextAllCptList.append(FF.AllCapital(tokens[i+1]))
        NextCptRatioList.append(FF.CapitalRatio(tokens[i+1]))
        NextLengthList.append(tokens[i+1].__len__())
        NextVwlRatioList.append(FF.VowelRatio(tokens[i+1]))
        NextNoVwlList.append(FF.NumberOfVowel(tokens[i+1]))
        NextNoCnsList.append(FF.NumberOfConsonant(tokens[i+1]))
        NextNoDigitList.append(FF.NumberOfDigits(tokens[i+1]))
        NextDigitRatioList.append(FF.DigitRatio(tokens[i+1]))
        NextNoNonAlphaList.append(FF.NumberOfNonAlphanumeric(tokens[i+1]))
        NextNonAlphaRatioList.append(FF.NonAlphanumericRatio(tokens[i+1]))
        NextAllCnsList.append(FF.AllConsonant(tokens[i+1]))
        NextHashtagList.append(FF.StartHashtag(tokens[i+1]))
        NextMentionList.append(FF.StartMention(tokens[i+1]))
        NextAllDigitList.append(FF.AllDigits(tokens[i+1]))
        NextTokenList.append(tokens[i+1])
    else:
        NextStrtCptList.append('')
        NextAllCptList.append('')
        NextCptRatioList.append('')
        NextLengthList.append('')
        NextVwlRatioList.append('')
        NextNoVwlList.append('')
        NextNoCnsList.append('')
        NextNoDigitList.append('')
        NextDigitRatioList.append('')
        NextNoNonAlphaList.append('')
        NextNonAlphaRatioList.append('')
        NextAllCnsList.append('')
        NextHashtagList.append('')
        NextMentionList.append('')
        NextAllDigitList.append('')
        NextTokenList.append('')

raw_data = {
    "DocID" : docIDs,
    "TokenID" : tokenIDs,
    "Token" : tokens,
    "StrtCpt" : StrtCptList,
    "AllCpt" : AllCptList,
    "CptRatio" : CptRatioList,
    "Length" : LengthList,
    "VwlRatio" : VwlRatioList,
    "NoVwl" : NoVwlList,
    "NoCns" : NoCnsList,
    "NoDigit" : NoDigitList,
    "DigitRatio" : DigitRatioList,
    "NoNonAlpha" : NoNonAlphaList,
    "NonAlphaRatio" : NonAlphaRatioList,
    "AllCns" : AllCnsList,
    "Hashtag" : HashtagList,
    "Mention" : MentionList,
    "AllDigit" : AllDigitList,

    "PrevToken" : PrevTokenList,
    "PrevStrtCpt": PrevStrtCptList,
    "PrevAllCpt": PrevAllCptList,
    "PrevCptRatio": PrevCptRatioList,
    "PrevLength": PrevLengthList,
    "PrevVwlRatio": PrevVwlRatioList,
    "PrevNoVwl": PrevNoVwlList,
    "PrevNoCns": PrevNoCnsList,
    "PrevNoDigit": PrevNoDigitList,
    "PrevDigitRatio": PrevDigitRatioList,
    "PrevNoNonAlpha": PrevNoNonAlphaList,
    "PrevNonAlphaRatio": PrevNonAlphaRatioList,
    "PrevAllCns": PrevAllCnsList,
    "PrevHashtag": PrevHashtagList,
    "PrevMention": PrevMentionList,
    "PrevAllDigit": PrevAllDigitList,

    "NextToken": NextTokenList,
    "NextStrtCpt": NextStrtCptList,
    "NextAllCpt": NextAllCptList,
    "NextCptRatio": NextCptRatioList,
    "NextLength": NextLengthList,
    "NextVwlRatio": NextVwlRatioList,
    "NextNoVwl": NextNoVwlList,
    "NextNoCns": NextNoCnsList,
    "NextNoDigit": NextNoDigitList,
    "NextDigitRatio": NextDigitRatioList,
    "NextNoNonAlpha": NextNoNonAlphaList,
    "NextNonAlphaRatio": NextNonAlphaRatioList,
    "NextAllCns": NextAllCnsList,
    "NextHashtag": NextHashtagList,
    "NextMention": NextMentionList,
    "NextAllDigit": NextAllDigitList,

    "Targets" : targets
}

dfFull = pd.DataFrame(raw_data, columns=['DocID', 'TokenID', 'Token', 'StrtCpt', 'AllCpt', 'CptRatio', 'Length', 'VwlRatio',
                                     'NoVwl', 'NoCns', 'NoDigit', 'DigitRatio', 'NoNonAlpha', 'NonAlphaRatio',
                                     'AllCns', 'Hashtag', 'Mention', 'AllDigit', 'PrevToken', 'PrevStrtCpt',
                                     'PrevAllCpt', 'PrevCptRatio', 'PrevLength', 'PrevVwlRatio', 'PrevNoVwl',
                                     'PrevNoCns', 'PrevNoDigit', 'PrevDigitRatio', 'PrevNoNonAlpha', 'PrevNonAlphaRatio',
                                     'PrevAllCns', 'PrevHashtag', 'PrevMention', 'PrevAllDigit', 'NextToken',
                                     'NextStrtCpt', 'NextAllCpt', 'NextCptRatio', 'NextLength', 'NextVwlRatio',
                                     'NextNoVwl', 'NextNoCns', 'NextNoDigit','NextDigitRatio', 'NextNoNonAlpha',
                                     'NextNonAlphaRatio', 'NextAllCns','NextHashtag', 'NextMention', 'NextAllDigit',
                                     'Targets'])

dfCropped = pd.DataFrame(raw_data, columns=['StrtCpt', 'AllCpt', 'CptRatio', 'Length', 'VwlRatio',
                                     'NoVwl', 'NoCns', 'NoDigit', 'DigitRatio', 'NoNonAlpha', 'NonAlphaRatio',
                                     'AllCns', 'Hashtag', 'Mention', 'AllDigit', 'PrevStrtCpt',
                                     'PrevAllCpt', 'PrevCptRatio', 'PrevLength', 'PrevVwlRatio', 'PrevNoVwl',
                                     'PrevNoCns', 'PrevNoDigit', 'PrevDigitRatio', 'PrevNoNonAlpha', 'PrevNonAlphaRatio',
                                     'PrevAllCns', 'PrevHashtag', 'PrevMention', 'PrevAllDigit',
                                     'NextStrtCpt', 'NextAllCpt', 'NextCptRatio', 'NextLength', 'NextVwlRatio',
                                     'NextNoVwl', 'NextNoCns', 'NextNoDigit','NextDigitRatio', 'NextNoNonAlpha',
                                     'NextNonAlphaRatio', 'NextAllCns','NextHashtag', 'NextMention', 'NextAllDigit',
                                     'Targets'])

dfFull.to_csv("FeatureOutputFull.csv")
dfCropped.to_csv("FeatureOutputCropped.csv")
