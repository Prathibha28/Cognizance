import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("country_wise_latest.csv")

plt.rcParams['font.size'] = 5

sample = df.sample(50)

sns.histplot(data=sample, x="New cases", color="lime")
sns.pairplot(sample)
plt.show()
