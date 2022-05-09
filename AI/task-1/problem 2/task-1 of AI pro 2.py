from numpy import nan
import pandas as pd

df = pd.read_csv("Data linkpro2.csv")
df_dtype = pd.DataFrame(index=df.index,columns=df.columns)

df['Alley'].fillna(method='bfill', inplace=True)

df['Alley'].fillna("Pave", inplace=True)
#print(df['Alley'])

df['LotFrontage'].fillna(method='bfill',inplace=True)
#print(df['LotFrontage'])

df['BsmtQual'].fillna(method='ffill',inplace=True)
#print(df['BsmtQual'])

df['BsmtCond'].fillna(method='ffill',inplace=True)
#print(df['BsmtCond'])

df['BsmtExposure'].fillna(method='ffill',inplace=True)
#print(df['BsmtExposure'])

df['BsmtFinType1'].fillna(0,inplace=True)
#print(df['BsmtCond'])

df['BsmtFinType2'].fillna(method='bfill',inplace=True)
#print(df['BsmtFinType2'])

df.interpolate(method ='linear', limit_direction ='forward', limit = 2)
print(df.isnull())
