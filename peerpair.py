import pandas as pd

#Reading into spreadsheet and creating variables that represent the diff columns
df = pd.read_excel (r'/Users/ziyanishani/Desktop/MunPartners.xlsx')
firstNames = df["First Name"].tolist()
lastNames = df["Last Name"].tolist()
req1 = df["Partner1"].tolist()
req2 = df["Partner2"].tolist()
req3 = df["Partner3"].tolist()
req4 = df["Partner 4"].tolist()

# Declaration of important variables
fullNames = []
paired = []
misc = []

# Filling fullNames
counter=0
for i in firstNames:
    if isinstance(firstNames[counter], str) and isinstance(lastNames[counter], str):
        fullNames.append(firstNames[counter] + " " + lastNames[counter])
    counter+=1


# Making it all lowercase and remiving whitespace at front or back
for i in range(len(fullNames)):
    
    if isinstance(fullNames[i], str):
        fullNames[i] = fullNames[i].lower() 
        fullNames[i] = fullNames[i].strip()
    if isinstance(req1[i], str):
        req1[i] = req1[i].lower()
        req1[i] = req1[i].strip()
    if isinstance(req2[i], str):
        req2[i] = req2[i].lower()
        req2[i] = req2[i].strip()
    if isinstance(req3[i], str):
        req3[i] = req3[i].lower()
        req3[i] = req3[i].strip()
    if isinstance(req4[i], str):
        req4[i] = req4[i].lower()
        req4[i] = req4[i].strip()

        
#Matching first requests 
counter = 0
for i in range(len(fullNames)):
     
    if isinstance(fullNames[i], str) and isinstance(req1[i], str):
       
        for j in range(len(req1)):
            if j != i and fullNames[i] == req1[j] and fullNames[j] == req1[i]:
                paired.append(fullNames[i] + " and " + fullNames[j])
                fullNames[i] = None
                fullNames[j] = None
               
   
    
        


