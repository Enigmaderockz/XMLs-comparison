from collections import defaultdict

with open('prod.csv', 'r') as t1, open('uat.csv', 'r') as t2:

    prod_set = set(t1.read().splitlines()[1:])
    print("prod set values\n")
    print(prod_set)
    print("\n")
    uat_set = set(t2.read().splitlines()[1:])
    print('uat set values\n')
    print(uat_set)
    print('\n')

# Code to populate the sets reading the csv files (use the `add` method of sets)

# Find the difference
diff = uat_set.difference(prod_set)

print(f"uat.csv has {len(diff)} rows extra:\n")

# It would be better to not hardcode the name of the columns in the output
# but getting the info depends on the package you use to read csv files

for row in diff:
    print(row)

print(
    "\nremoving extra rows from uat.csv file and generating new_uat_set equivalent to prod_set\n"
)

new_uat_list = [i for i in list(uat_set) if i in list(prod_set)]
new_uat_set = set(new_uat_list)
print(new_uat_set)

a = prod_set
b = new_uat_set

res_dict = defaultdict(list)
diff = ([('prod.csv,' + i) if i in a else ('uat.csv,' + i) if i in b else ''
         for i in list(a ^ b)])

if diff == []:
    print('\nGreat!!! There are no differences')
else:
    print("comparison results\n")
    print('\n'.join(diff))
