import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")
path = "/Users/dhamotharan/PycharmProjects/fileautomation/files/"
os.chdir(path)
data_dict = {}
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}{file}"
        with open(file_path, 'r') as f:
            text = f.read()
            temp = text.split("\n")
            data_dict[file] = list(filter(None, temp))

data = [[filename, parameter]
        for filename, parameters in data_dict.items()
        for parameter in parameters]
df = pd.DataFrame(data, columns=['filename', 'parameters'])

df[["tempname","value"]] = df['parameters'].str.split(':',expand=True)
df[["tempname","name"]] = df['tempname'].str.split('.',expand=True)
df.drop(["tempname"],axis=1,inplace=True)

def optionfunc(temp_df):
    unaltered_df = temp_df
    get_option = str(input("Enter input value or values from the above listed options: "))
    option_list = get_option.split(",")
    option_list = [opt.lower() for opt in option_list]
    if get_option.lower() != "none" and get_option:
        if get_option.lower() == "all":
            pass
        else:
            temp_df = temp_df[temp_df['name'].str.lower().isin(option_list)]
        temp_df['output'] = temp_df[["name", "value"]].agg(': '.join, axis=1)
        temp_list = temp_df['output'].tolist()
        if temp_list:
            print("\n".join(temp_list))
        else:
            print("Please provide correct input")
            optionfunc(unaltered_df)
    else:
        print("You have chosen none hence utility is closing")

def filenamefunc(df):
    get_file = str(input("Enter the Filename: "))
    if get_file:
        temp_df = df[df['filename'].str.lower().isin([get_file.lower()])]
        temp_df = temp_df[temp_df['name'].notna()]
        if not temp_df.empty:
            print("Options: ",*(temp_df["name"].values))
            optionfunc(temp_df)
        elif get_file.lower() == "none" and (temp_df.empty):
            print("You have chosen none hence utility is closing")
        else:
            print("Please provide correct input")
            filenamefunc(df)
    else:
        print("You have chosen none hence utility is closing")

def get_tablenamefunc():
    get_tablename = str(input("Enter Table Name:"))
    if get_tablename:
        new_df = df[df['name'].str.lower().isin(["table_name"])]
        filename_list = []
        for row in new_df.values:
            if get_tablename.lower() in row[2].lower():
                filename_list.append(row[0])
        if filename_list:
            print("Given tables are present in following files: ", *(filename_list))
            temp_df = df[df['filename'].isin(filename_list)]
            filenamefunc(temp_df)
        elif (not filename_list) and (get_tablename.lower() == "none"):
            print("You have chosen none hence utility is closing")
        else:
            print("Please provide correct input")
            get_tablenamefunc()
    elif get_tablename.lower() == "none" or (not get_tablename):
        print("You have chosen none hence utility is closing")

def get_catalogfunc():
    get_catalog = str(input("Enter Catalog:"))
    if get_catalog:
        new_df = df[df['name'].str.lower().isin(["catalog"])]
        filename_list = []
        for row in new_df.values:
            if get_catalog.lower() in row[2].lower():
                filename_list.append(row[0])
        if filename_list:
            print("Given tables are present in following files: ", *(filename_list))
            temp_df = df[df['filename'].isin(filename_list)]
            filenamefunc(temp_df)
        elif (not filename_list) and (get_catalog.lower() == "none"):
            print("You have chosen none hence utility is closing")
        else:
            print("Please provide correct input")
            get_catalogfunc()
    elif get_catalog.lower() == "none" or (not get_catalog):
        print("You have chosen none hence utility is closing")

def get_firstinputfunc():
    first_input = str(input("Input any one of the following: Filename, Tablename, Catalog:\n"))

    if first_input.lower() == "filename":
        filenamefunc(df)

    elif first_input.lower() == "tablename":
        get_tablenamefunc()

    elif first_input.lower() == "catalog":
        get_catalogfunc()

    elif first_input.lower() == "none" or (not first_input):
        print("You have chosen none hence utility is closing")

    else:
        print("Please provide correct input")
        get_firstinputfunc()

get_firstinputfunc()
