from lxml import etree

root_1 = etree.parse('test1.xml').getroot()
root_2 = etree.parse('test2.xml').getroot()

d1, d2 = [], []
for node in root_1.findall('.//catalog_item'):
    for x in node.iter():
        if x.attrib:
            d1.append(x.attrib.values()[0])
        if x.text.strip():
            d1.append(x.text.strip())

for node in root_2.findall('.//catalog_item'):
    for x in node.iter():
        if x.attrib:
            d2.append(x.attrib.values()[0])
        if x.text.strip():
            d2.append(x.text.strip())

if(set(d1) == set(d2)):
    print('Data is same in both XML files') 
else:
    print('Data is different in both XML files')
    print(d1-d2)
