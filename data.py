import requests
import json
import re
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
with open("dataset.json","r") as reader:
    dictList = json.load(reader)
df = pd.DataFrame(dictList)
tagSum = []
for i in pd.unique(df.prob):
    tagSum+=df[df.prob==i]["tags"].iloc[0]
print(set(tagSum))
df.loc[df['lang'].str.contains('C\+\+', na=False), 'lang'] = 'C++'
df.loc[df['lang'].str.contains('GNU', na=False), 'lang'] = 'C'
df.loc[df['lang'].str.contains('Java', na=False), 'lang'] = 'Java'
df = df[df.lang.isin(["C++","C","Java","Python 3","Go"])]
print(pd.value_counts(df.lang))
#Which languages are the best? 
#given a type of problem (tag), and whether to measure by fastest runtime or OK rate on that problem, graph languages
def plot(tag=None,langs=[],time=False):
    plot_df = df[tag in df.tags] if tag else df
    plot_df = plot_df[df.lang.isin(langs)] if len(langs) > 0 else plot_df
    plot_df["time"] = plot_df["time"].astype(pd.Int64Dtype())
    if not time:
        plot_df["percent"] = df['lang'].map(plot_df.groupby('lang')['status'].apply(lambda x: (x.sum() / len(x)) * 100))
        print(plot_df)
        ax = sb.barplot(x=plot_df["lang"],y=plot_df["percent"])
        plt.show()
        return
        #print(plot_df)
        #def update_prob_dict(row):
            #if row["prob"] in prob_dict:
                #prob_dict[row["prob"]][1]+=1
                #prob_dict[row["prob"]][0]+=1 if row["status"] else 0
            #else:
                #prob_dict[row["prob"]]=[1 if row["status"] else 0,1]
            #return row
        #plot_df.apply(update_prob_dict,axis=1)
        print(lang_dict)
    else:
        ax = sb.boxplot(x=plot_df["lang"],y=plot_df["time"],hue=plot_df["lang"])
        plt.legend([],[], frameon=False)
        ax.set(xlabel="Language",ylabel="Running Time (ms)",title="Average Running time per language")
        plt.show()
plot(time=False)

#keep track of the tags on each submission, the language, the time, OK or not
#MAKE SURE type == "PROGRAMMING"
