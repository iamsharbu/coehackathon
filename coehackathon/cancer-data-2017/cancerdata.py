import pandas as pd
import numpy as np
df=pd.read_csv('cancer2017.csv',encoding='utf-8')
df.replace({r'[^\x00-\x7F]+':np.nan}, regex=True, inplace=True)
for i in range(0,df.shape[0]):
    for j in range(1,df.shape[1]):
        if ',' in str(df.iloc[i][j]):
            df.iloc[i][j]=df.iloc[i][j].replace(',','')
        df.iloc[i][j]=pd.to_numeric(df.iloc[i][j])
df.columns = [c.strip() for c in df.columns.values.tolist()]
df.columns = [c.replace(' ','') for c in df.columns.values.tolist()]
print(df.columns)

#with open('cancer2017.csv', 'rb') as f:
#     lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
#data=[]
#for i in lines:
#    lis=i.split(',')
#    
#    data.append(lis)
#df=pd.DataFrame(data)
#print(df)


#col=lines[0].split(',')
#data.columns=data.iloc[0]
#print(data.columns)