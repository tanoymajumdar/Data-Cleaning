import pandas as pd
import numpy as np
df1 = pd.read_csv(r"C:\ssa_fb.csv", index_col = False, names = ["A","B","C","D","E","F","G","H","I"])
df1 = df1.iloc[5:]
df1 = df1.drop(df1.index[12])
df1['1'] = df1['A'].fillna('') +  df1['B'].fillna('')  +  df1['C'].fillna('')
df1['2'] = df1['D'].fillna('') +  df1['E'].fillna('')  +  df1['F'].fillna('')
df1['3'] = df1['G'].fillna('') +  df1['H'].fillna('')  +  df1['I'].fillna('')
df1 = df1.drop(['A','B','C','D','E','F','G','H','I'], axis = 1)
a = ['1', '2', '3']
b = ['?', '(',')','$',]
for col in a:
    for character in b:
        if(col=='1' and character=='$'):
            continue
        else:
            df1[col] = df1[col].str.replace(character,'')
df2 = pd.DataFrame()
df2 = df2.append(df1, ignore_index = True)
df2 = df2.rename(index=str, columns={"1": ",", "2": "June 30, 2018", "3": "December 31, 2017"})
df2 = df2.replace('', np.NaN)
df1['4']= df1['2'].str.replace(',','')
df1['5'] = df1['3'].str.replace(',','')
df1['4'] = pd.to_numeric(df1['4'], errors='coerce')
df1['5'] = pd.to_numeric(df1['5'], errors='coerce')
df1['Yearly Percentage Change of each item'] = ((df1['5'] - df1['4'])/df1['4'])*100
s1 = df1.iloc[[6]]
s2 = df1.iloc[[18]]
df3 = pd.DataFrame()
df3 = df3.append(s1)
df3 = df3.append(s2)
df3 = df3.drop(df3.columns[[1,2,5]], axis=1)
df1 = df1.drop(df1.columns[[3,4]], axis=1)
df3 = df3.set_index('1')
df3['4'] = pd.to_numeric(df3['4'], errors='coerce')
df3['5'] = pd.to_numeric(df3['5'], errors='coerce')
df3.loc['Current Ratio'] = df3.iloc[0]/df3.iloc[1]
df3 = df3.rename(index=str, columns={"4": "2", "5": "3"})
df3 = df3.reset_index()
s = df3.iloc[[2]]
df1 = df1.append(s,ignore_index=True)
df1 = df1.rename(index=str, columns={"1": ",", "2": "June 30, 2018", "3": "December 31, 2017"})
df1.to_csv("e.csv")
print (df2)
print(df1)
