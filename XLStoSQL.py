################################################

# AUTHOR: @srtoPeixet
# VERSION : Contains lots of exceptions if not used as it has to. I will be updating asap.

###############################################

import json
import pandas as pd

PATH = ''
OUTPUT=''
PATH = input("PATH to your excel file including extension...  \n")
sheets = {}
while True:

    name = input("Enter sheet name (or Enter to quit): ")
    if not name:
        break
    content = input("Enter your column names separated by comas e.g. Id,Client,Salary (or Enter to quit): ")
    content = content.split(",")
    sheets[name] = content

print("Your sheets are:")
print(json.dumps(
sheets,
indent = 4
))
OUTPUT = input("Name your output file... (without extension)")
print("Generating txt file ...")
dfs = []
xls = pd.ExcelFile(PATH)
for sheet in sheets:
    df = pd.read_excel(xls, sheet,header = None)
    df.columns = sheets[sheet]
    dfs.append(df)

count = 0
with open(str(OUTPUT) + '.txt', 'w') as f:
     for df in dfs:

        print("INSERT INTO " + str(list(sheets.keys())[count]) +'(',end="",file=f)

        for i in range(len(sheets[list(sheets.keys())[count]])):
            print('`' + str(sheets[list(sheets.keys())[count]][i]) + '`',end="",file=f)
            if (i < len(sheets[list(sheets.keys())[count]]) - 1):
                print(',',end="",file=f)

        print(')' + " VALUES",file=f)

        for index, row in df.iterrows():
            print("(",end="",file=f)
            for i in range(len(row)):

                if (str(row[i]).lower().islower()):
                    print('"' + str(row[i]) + '"',end="",file=f)
                else:
                    print(row[i],end="",file=f)


                if i < len(row) - 1:
                    print(",",end="",file=f)

            print(")",end="",file=f)
            if index < df.shape[0] - 1:
                print(",",file=f)
            else:
                print(";",file=f)
        count += 1
print("Successful ! File generated correctly.")
