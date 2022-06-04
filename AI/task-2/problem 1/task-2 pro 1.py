import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ADANIPORTS.csv")

sample = df.sample(20)

sns.set()

fig, axes = plt.subplots(2,2)

plt.rcParams['font.size'] = 2

sns.barplot(data=df, x=sample["VWAP"],y=sample["Date"],ax=axes[0,0],color="red")

sns.histplot(data=df,x=df["VWAP"],ax=axes[0,1])


sns.scatterplot(data=df,x=df["Open"],y = df["VWAP"],ax=axes[1,0])

sns.heatmap(data=df.corr(),annot = True, cmap='viridis',ax=axes[1,1])

plt.show()
