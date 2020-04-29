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
        print(f'Processing file number: {i}')

        lista_laudos.append(laudo)

i = 0
with open('convert.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerow(["Report"])
    for laudo in lista_laudos:
        csv_writer.writerow([laudo])
        i += 1

print (f"\nXML Files successfully converted to convert.csv. {i} records were exported.")