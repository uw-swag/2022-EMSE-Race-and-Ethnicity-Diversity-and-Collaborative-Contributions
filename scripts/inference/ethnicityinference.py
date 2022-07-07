import pandas as pd
import urllib
import requests
import json

#replace path for team_members.csv
members_df = pd.read_csv("/home/sham/Desktop/846spring2020/project/github/ethanalysis75/vault/data/team_members.csv")
#the api token is expired, please replace with your own
ETH_URL='http://www.name-prism.com/api_token/eth/json/39308a9faeb054ca/'
notfound = []
members_df["resultfetch"] = 0 *len(members_df)

for index,row in members_df.iterrows():
    login = row["login"]
    name = str(row["name"])
    print(index)
    if(name!="nan" and len(name)>1):
        try:
            r = requests.get(ETH_URL + urllib.parse.quote(str(name)))
            with open("../data/membersethdataall/"+login+".json","w") as resultfile:
                json.dump(json.loads(r.text),resultfile)
                members_df.at[index,"resultfetch"] = 1
                print("success")
                
        except Exception as e:
            print(e)
            print(login)
            print(r.text)
            notfound.append(login)
            members_df["resultfetch"] = 0
        
members_df.to_csv("fetch_results.csv",index=False)