import pandas as pd
df = pd.read_excel (r'/Users/ziyanishani/Desktop/PPC.xlsx')
#print(df)
names = df["Full Name (first and last)"]

newNames = []
counter = 0
for i in names:  
    newNames.append(i.lower())

counter = 0
for i in newNames:
    counter+=1
    if i == "gordon beaupain":
        print(counter)
    