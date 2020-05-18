from lxml import etree

root_1 = etree.parse('test1.xml').getroot()
root_2 = etree.parse('test2.xml').getroot()

d1, d2 = [], []
for node in root_1.findall('.//product'):
    for x in node.iter():
        if x.attrib:
            d1.append(x.attrib.values()[0])
        if x.text.strip():
            d1.append(x.text.strip())

for node in root_2.findall('.//product'):
    for x in node.iter():
        if x.attrib:
            d2.append(x.attrib.values()[0])
        if x.text.strip():
            d2.append(x.text.strip())
