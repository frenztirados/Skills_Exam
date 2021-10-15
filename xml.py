import xml.etree.cElementTree as ET
import csv

tree = ET.parse("vaccination.xml")
root = tree.getroot()
vacine =open('vacine.csv', 'w')

csvwriter=csv.writer(vacine)
head=[]

count=0
for element in root.findall('record'):
    nodes=[]

    if count == 0:
        YearWeekISO = element.find('YearWeekISO').tag
        head.append(YearWeekISO)

        FirstDose = element.find('FirstDose').tag
        head.append(FirstDose)

        FirsDoseRefused = element.find('FirsDoseRefused').tag
        head.append(FirsDoseRefused)

        SecondDose = element.find('SecondDose').tag
        head.append(SecondDose)

        UnknownDose = element.find('UnknownDose').tag
        head.append(UnknownDose)

        NumberDosesReceived = element.find('NumberDosesReceived').tag
        head.append(NumberDosesReceived)

        Region = element.find('Region').tag
        head.append(Region)

        Population = element.find('Population').tag
        head.append(Population)

        ReportingCountry = element.find('ReportingCountry').tag
        head.append(ReportingCountry)

        TargetGroup = element.find('TargetGroup').tag
        head.append(TargetGroup)

        Vaccine = element.find('Vaccine').tag
        head.append(Vaccine)

        Denominator = element.find('Denominator').tag
        head.append(Denominator)
        count = count +1

    YearWeekISO = element.find('YearWeekISO').text
    nodes.append(YearWeekISO)

    FirstDose = element.find('FirstDose').text
    nodes.append(FirstDose)

    FirsDoseRefused = element.find('FirsDoseRefused').text
    nodes.append(FirsDoseRefused)

    SecondDose = element.find('SecondDose').text
    nodes.append(SecondDose)

    UnknownDose = element.find('UnknownDose').text
    nodes.append(UnknownDose)

    NumberDosesReceived = element.find('NumberDosesReceived').tag
    nodes.append(NumberDosesReceived)

    Region = element.find('Region').text
    nodes.append(Region)

    Population = element.find('Population').text
    nodes.append(Population)

    ReportingCountry = element.find('ReportingCountry').text
    nodes.append(ReportingCountry)

    TargetGroup = element.find('TargetGroup').text
    nodes.append(TargetGroup)

    Vaccine = element.find('Vaccine').text
    nodes.append(Vaccine)

    Denominator = element.find('Denominator').text
    nodes.append(Denominator)

    csvwrite.writerow(nodes)
vacine.close()
    

        


