import matplotlib.pyplot as plt
import pandas as pd
from statistics import mode, mean, stdev

def DrawPieChart(labels, sizes):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


labels = 'Numeric', 'Boolean'
sizes = [9, 6]
DrawPieChart(labels, sizes)

labels = 'Address', 'Company', 'Contact', 'Date', 'Event/Activity', 'ID', 'Job', 'Name', 'Place'
sizes = [48, 1256, 9, 620, 869, 98, 617, 709, 646]
DrawPieChart(labels, sizes)

featureData = pd.read_csv('FeatureOutputCropped.csv', engine='python')
featureValues = featureData.get_values()[:,1:16]
featureNames = ['StrtCpt', 'AllCpt', 'CptRatio', 'Length', 'VwlRatio', 'NoVwl', 'NoCns',
                'NoDigit', 'DigitRatio', 'NoNonAlpha', 'NonAlphaRatio', 'AllCns', 'Hashtag',
                'Mention', 'AllDigit']

StrtCpt = []
AllCpt = []
CptRatio = []
Length = []
VwlRatio = []
NoVwl = []
NoCns = []
NoDigit = []
DigitRatio = []
NoNonAlpha = []
NonAlphaRatio = []
AllCns = []
Hashtag = []
Mention = []
AllDigit = []

for i in range(0, featureValues.__len__()):
    StrtCpt.append(featureValues[i][0])
    AllCpt.append(featureValues[i][1])
    CptRatio.append(featureValues[i][2])
    Length.append(featureValues[i][3])
    VwlRatio.append(featureValues[i][4])
    NoVwl.append(featureValues[i][5])
    NoCns.append(featureValues[i][6])
    NoDigit.append(featureValues[i][7])
    DigitRatio.append(featureValues[i][8])
    NoNonAlpha.append(featureValues[i][9])
    NonAlphaRatio.append(featureValues[i][10])
    AllCns.append(featureValues[i][11])
    Hashtag.append(featureValues[i][12])
    Mention.append(featureValues[i][13])
    AllDigit.append(featureValues[i][14])

minList = ['', '', str(min(CptRatio)), str(min(Length)), str(min(VwlRatio)), str(min(NoVwl)), str(min(NoCns)),
           str(min(NoDigit)), str(min(DigitRatio)), str(min(NoNonAlpha)), str(min(NonAlphaRatio)), '', '', '', '']
maxList = ['', '', str(max(CptRatio)), str(max(Length)), str(max(VwlRatio)), str(max(NoVwl)), str(max(NoCns)),
           str(max(NoDigit)), str(max(DigitRatio)), str(max(NoNonAlpha)), str(max(NonAlphaRatio)), '', '', '', '']
averageList = ['', '', str(mean(CptRatio)), str(mean(Length)), str(mean(VwlRatio)), str(mean(NoVwl)), str(mean(NoCns)),
           str(mean(NoDigit)), str(mean(DigitRatio)), str(mean(NoNonAlpha)), str(mean(NonAlphaRatio)), '', '', '', '']
stddevList = ['', '', str(stdev(CptRatio)), str(stdev(Length)), str(stdev(VwlRatio)), str(stdev(NoVwl)), str(stdev(NoCns)),
           str(stdev(NoDigit)), str(stdev(DigitRatio)), str(stdev(NoNonAlpha)), str(stdev(NonAlphaRatio)), '', '', '', '']
modeList = [str(mode(StrtCpt)), str(mode(AllCpt)), '', '', '', '', '', '', '', '', '', str(mode(AllCns)), str(mode(Hashtag)),
            str(mode(Mention)), str(mode(AllDigit))]

raw_data = {
    'Abbreviation' : featureNames,
    'Min' : minList,
    'Max' : maxList,
    'Average' : averageList,
    'Mode' : modeList,
    'Std. Dev.' : stddevList
}

df = pd.DataFrame(raw_data, columns=['Abbreviation', 'Min', 'Max', 'Average', 'Mode', 'Std. Dev.'])
df.to_csv("FeatureStats.csv", na_rep="-")
