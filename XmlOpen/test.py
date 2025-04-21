
import xmltodict, json

#In case of wanting to try with element class, use the code below and remove the code not currently commented out!

'''from Element import XmlDocument

with open('Aflevering3.xml') as fd:
  doc = fd.read()

doc = XmlDocument(doc)
print(doc.toJson(indent=4))
'''


with open('Aflevering3.xml') as fd:
  doc = xmltodict.parse(fd.read())


f = open("jsonTis.txt","x")
f.write(str(doc))
f.close()

