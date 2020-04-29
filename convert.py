import xmltodict
import glob
import csv

lista_arqs_xml = glob.glob("Indiana/*.xml")

lista_laudos = []

i = 0
for xml in lista_arqs_xml:
    i += 1
    comparison = "Comparison: "
    indication = "Indication: "
    findings = "Findings: "
    impression = "Impression: "
    with open(xml) as fd:
        doc = xmltodict.parse(fd.read())
        try:
            comparison = comparison + doc['eCitation']['MedlineCitation']['Article']['Abstract']['AbstractText'][0]['#text']
        except:
            pass

        try:
            indication = indication + doc['eCitation']['MedlineCitation']['Article']['Abstract']['AbstractText'][1][
                '#text']
        except:
            pass

        try:
            findings = findings + doc['eCitation']['MedlineCitation']['Article']['Abstract']['AbstractText'][2][
                '#text']
        except:
            pass

        try:
            impression = impression + doc['eCitation']['MedlineCitation']['Article']['Abstract']['AbstractText'][3][
                '#text']
        except:
            pass

        laudo = comparison + "\n" + indication + "\n" + findings + "\n" + impression
        print(i)

        lista_laudos.append(laudo)

i = 0
with open('convert.csv','w') as CSV_File:
    CSV_File.write("Report\n")
    for laudos in lista_laudos:
        i += 1
        CSV_File.write('"' + laudos + '"\n')

print (f"XML Files successfully converted to convert.csv. {i} records were exported.")