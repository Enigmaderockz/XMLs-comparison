list_1 = ['banana', 'aple', 'at', 'peacock', 'hjhhhjhjh']
list_2 = ['hello', 'apple', 'cat', 'sherrif']

Changed = False
for x in list_1:
    if x in list_2:
        if not Changed:
            list_2[list_2.index(x)] = "jackie"
            Changed = True
        else:
            list_2.remove(x)

print(list_2)

print(list(dict.fromkeys(['Jacky' if el in list_1 else el for el in list_2])))
