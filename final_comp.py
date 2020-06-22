from lxml import etree
from collections import defaultdict
from pprintpp import pprint as pp

root_1 = etree.parse('test1.xml').getroot()
root_2 = etree.parse('test2.xml').getroot()

d1, d2 = [], []
for node in root_1.findall('.//catalog_item'):
    item = defaultdict(list)
    for x in node.iter():
        if x.attrib:
            item[x.attrib.keys()[0]].append(x.attrib.values()[0])
        if x.text is None:
          item[x.tag].append('None')
        elif x.text.strip():
            item[x.tag].append(x.text.strip())
    d1.append(dict(item))



for node in root_2.findall('.//catalog_item'):
    item = defaultdict(list)
    for x in node.iter():
        if x.attrib:
            item[x.attrib.keys()[0]].append(x.attrib.values()[0])
        if x.text is None:
          item[x.tag].append('None')
        elif x.text.strip():
            item[x.tag].append(x.text.strip())
    d2.append(dict(item))

d1 = sorted(d1, key = lambda x: x['item_number'])
d2 = sorted(d2, key = lambda x: x['item_number'])


res_dict = defaultdict(list)
for x, y in zip(d1, d2):
  for key1, key2 in zip(x.keys(), y.keys()):
      if (key1 == key2) and sorted(x[key1]) != sorted(y[key2]):
        a =set(x[key1])
        b = set(y[key2])
        diff = ([(i+'--'+'test1.xml') if i in a else (i+'--'+'test2.xml') if i in b else '' for i in list(a^b)])
        res_dict[x['item_number'][0]].append({key1: diff})



if res_dict == {}:
  print('Data is same in both XML files')
else:
  pp(dict(res_dict))
