from genderComputer import GenderComputer
from geotext import GeoText
import pandas as pd

gc = GenderComputer()
#replace with team_members.csv
members_df = pd.read_csv("/home/sham/Desktop/846spring2020/project/github/ethanalysis75/vault/data/team_members.csv")

result = []
for index,row in members_df.iterrows():
    address = str(row["location"]).title()
    name = str(row["name"])
    print(name)
    if name!="nan" and len(name)>1:
        places = GeoText(address)
        country = places.countries
        if(len(country) > 0):
            pg = gc.resolveGender(name,country[0])
        else:
            pg = gc.resolveGender(name,None)
        print(pg)
        if pg == None:
            pg= "UnKnown"
    else:
        pg = "NAN"        
    print(pg)