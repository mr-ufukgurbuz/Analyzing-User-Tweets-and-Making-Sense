import FeatureFunctions as FF
import pandas as pd

#load the data
data = pd.read_csv("documentTokenAll.csv", header=None)

tokens = []
targets = []

for i in range(1, data.get_values().__len__()):
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

raw_data = {
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
    "Targets" : targets
}

df = pd.DataFrame(raw_data, columns=['StrtCpt', 'AllCpt', 'CptRatio', 'Length', 'VwlRatio', 'NoVwl', 'NoCns',
                                    'NoDigit', 'DigitRatio', 'NoNonAlpha', 'NonAlphaRatio', 'AllCns', 'Hashtag',
                                    'Mention', 'AllDigit', 'Targets'])
df.to_csv("FeatureOutput.csv")
