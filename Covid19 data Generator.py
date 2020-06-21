import pandas as pd
import requests

r = requests.get("https://covidnigeria.herokuapp.com/api") #covid19 raw data
data = r.json() 

Samples_Tested = data["data"]['totalSamplesTested']
confirmed_cases = data["data"]["totalConfirmedCases"]
Active_cases = data["data"]["totalActiveCases"]
Death = data["data"]["death"]
Discharged = data["data"]["discharged"]
all_states = data["data"]["states"]

keys = all_states[0].keys() #getting the keys for the all_state dictionary
length = len(all_states[0])
No_of_states = len(all_states)

#Adding the headers to the new txt
with open('Nigeria_covid19_data.txt', 'w') as r:
    for key in keys:
        #print(key) #printing out all the keys
        r.write(key)
        r.write(',')

file = open("Nigeria_covid19_data.txt", "a")
file.write("\n")
for state in range(No_of_states):
    file.write("\n")
    for key in keys:
        data = all_states[state][key]
        data = str(data)
        #print(data)
        file.write(data)
        file.write(",")
file.close()

data = pd.read_csv("Nigeria_covid19_data.txt")
data = data[["state", "confirmedCases","casesOnAdmission", "discharged", "death"]]
data = data.rename(columns={"state":"State", "confirmedCases":"Total_Confirmed_case", "casesOnAdmission":"Total_Active_case", "discharged":"Total_Recovered", "death": "Total_Death"})
data.to_csv("Nigeria covid-19 case.csv", index=False)