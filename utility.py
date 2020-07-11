for x in list1:
    if x not in list2:
      list3.append(x)
print(list3)

for node in root_1.findall('.//account'):
  listu.append(node.find('acctBasicInfo/acctName1').text)
print(listu)

list1 = ['appl', 'ban']
list2 = ['rt', 'ut', 'ect', 'fit']

for i,item in enumerate(list2):
  if item in list1:
    list2[i]= 'prep' + item

print(list2)
