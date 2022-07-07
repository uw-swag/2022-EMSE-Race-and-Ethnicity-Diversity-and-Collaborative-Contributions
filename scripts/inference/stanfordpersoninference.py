from nltk.tag import StanfordNERTagger
import pandas as pd

jar = '../stanford/stanford/stanford-ner.jar'
model = '../stanford/stanford/classifiers/english.all.3class.distsim.crf.ser.gz'
tagger = StanfordNERTagger(model, jar)
print("Model loaded")

usersall_df = pd.read_csv("/home/sham/Desktop/846spring2020/project/github/ethanalysis75/vault/data/team_members.csv")

notfind = []
usersall_df["stanford_person_identifier"] = 0 * len(usersall_df)
for index,row in usersall_df.iterrows():
    print(index)
    try:
        name = str(row["name"])
        if (name != "nan" or len(name) <=1):
            for s in tagger.tag(name.split()):
                if s[1]=='PERSON':
                    usersall_df.at[index,"stanford_person_identifier"] = 1
    except Exception as e:
        print(index)
usersall_df.to_csv("results.csv",index=False)