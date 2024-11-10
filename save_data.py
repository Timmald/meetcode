import requests
import json
import pandas as pd
import seaborn as sb
obj = requests.get("https://codeforces.com/api/contest.status?contestId=566")
obj = json.loads(obj.text)['result']
#obj += json.loads(requests.get("https://codeforces.com/api/contest.status?contestId=567").text)["result"]
#obj += json.loads(requests.get("https://codeforces.com/api/contest.status?contestId=568").text)["result"]
print(len(obj))
obj = [i for i in obj if i["problem"]["type"]=="PROGRAMMING"]
print(len(obj))
dictList = []
for i in obj:
    dictList.append({
        "tags":i["problem"]["tags"],
        "lang":i["programmingLanguage"],
        "time":i["timeConsumedMillis"],
        "status":i["verdict"],
        "prob":i["problem"]["name"]
    })
with open("dataset.json","w") as writer:
    json.dump(dictList, writer, indent=0)