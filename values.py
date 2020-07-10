from lxml import etree
from collections import defaultdict

root_1 = etree.parse('a.xml').getroot()
d1= []
print("x")
for node in root_1.findall('.//catalog_item'):
    item = defaultdict(list)
    for x in node.iter():
        # iterate over the items
        for k, v in x.attrib.items():
            item[k].append(v)
        if x.attrib is None:
          item[x.attrib].append('None')
        if x.text is None:
          item[x.tag].append('None')
        elif x.text.strip():
            item[x.tag].append(x.text.strip())

    d1.append(dict(item))


print(d1)

for f in d1:
  print(f)
  res = {key: f[key] for key in f.keys() 
                               & {'gender', 'price'}} 
  print(str(res))
