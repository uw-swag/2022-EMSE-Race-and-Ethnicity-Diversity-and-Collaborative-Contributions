#!/usr/bin/env python3

import pandas as pd
from collections import Counter

#replacefilename
team_df = pd.read_csv("/home/sham/Desktop/846spring2020/project/github/ethanalysis75/vault/team_details.csv")
cols = ["2PRACE","Hispanic","API","Black","AIAN","White","Unknown"]

result = {}
domresult = {}
atleastonedev = {}
minorityresult = {}
exactlyonedev = {}
for col in cols:
    result[col] = 0
    domresult[col] = 0
    atleastonedev[col] = 0
    minorityresult[col] = 0
    exactlyonedev[col] = 0
    
for index,row in team_df.iterrows():
    members_eth = eval(row["eth_stanandnameprism_st_withoutNAN"])
    unique_eth = list(set(members_eth))
    if len(unique_eth) == 1:
        result[unique_eth[0]] = result[unique_eth[0]] + 1
        
    else:
        if Counter(members_eth).most_common(1)[0][1] > len(members_eth)/2:
            domresult[Counter(members_eth).most_common(1)[0][0]] = domresult[Counter(members_eth).most_common(1)[0][0]] + 1
        
        for col in cols:
            if members_eth.count(col) > 0 and members_eth.count(col) <= len(members_eth)/2:
                minorityresult[col] = minorityresult[col] + 1
                
    
    for col in cols:
        if col in members_eth:
            atleastonedev[col] = atleastonedev[col] + 1

    
print("ALL SAME ETHNICITY:")        
print(result)
print("MAJORITY ETHNICITY:")
print(domresult)
print("MINORITY ETHNICITY:")
print(minorityresult)
print("ATLEAST ONE DEV")
print(atleastonedev)