import xml.etree.ElementTree as ET
tree = ET.parse('tes.xml')

lis = ["123456"]
root = tree.getroot()
print('root is', root)
print(type(root))

for continent in root.findall('.//continents'):
  for country in continent.findall('./country'):
    if country.find('state/rank').text not in lis:
      continent.remove(country)

tree.write('outpu.xml')
