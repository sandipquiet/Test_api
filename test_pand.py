import numpy as np
import pandas as pd

dic1 = {
    "name": ["Sanjeev Rai","Rajkumar","Anil Kumar","Mukesh Kumar","Ajay Rai"],
    "marks": [80, 75, 90, 85, 76],
    "city": ["Chennai", "Gorakhpur", "Patna", "Samastipur", "Gopalganj"]
}
df = pd.DataFrame(dic1)
#df.to_csv("pandas.csv")
df.head(3) # print top 3 value
df.tail(2) # show last two row
df.describe() # show all numarical field count mean std,max, percent
df1=pd.read_csv("pandas_test.csv")
#df1['Speed'][0]=54
df1.index = [1,2,3,4,5] # change indexes of df1 starting 1,2,3,4
ser=pd.Series(np.random.rand(45))
ndf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
ndf[0][0]=0.5 #change 0 position index
ndf.index # indexes
ndf.columns # columns
ndf.to_numpy() #change DF to numpy

ndf.T # Transpose or change row as column and  column as row
ndf.sort_index(axis=0, ascending=False)  # sort data frame row wise if axis=0 and axis=1 then column wise
ndf2=ndf # just like create a view both DF point same address
ndf_c=ndf.copy() # ndf_c=ndf.copy() this is copy of ndf not point same address
#ndf_c=ndf[:]
ndf.loc[0,0] = "888"
#ndf.drop(0,axis=1) drop column value
ndf.loc[[1,2],[0,1]] #show 1,2 rows and 0,1 column value
ndf.loc[:, :] #show all rows and all column value
x=ndf.loc[(ndf[1]<0.3)] # condition base fid data row wise ,column wise
ndf.iloc[0,4] #print 0 row and 5th column
ndf.iloc[[0,1],[1,2]] #print 0,1 rows with 1,2 column
#ndf.drop([0], axis=1, inplace=True) drop 0 columns
#ndf.reset_index(drop=True, inplace=True) reset index again and drop index column
#ndf.loc[:,['col']]="xyz" set column value
d1 = {'Name': ['Pankaj', 'Meghna', 'Pankaj', 'Lisa'], 'ID': [1, 2, 3, 4], 'Salary': [100, 200, np.nan, pd.NaT],
      'Role': ['CEO', None, pd.NaT, pd.NaT]}

df1=pd.DataFrame(d1)
#df1.dropna() drop all Na value from data
#df1.dropna(how='all', axis=1) drop all Na value from column data if any column data if any column data full nan
#df1.drop_duplicates(subset=['Name']) remove duplicate name
#df1.drop_duplicates(subset=['Name'], keep='last') remove duplicate name except last name
#df1.shape() show how many rows and column(3*3) in DF
#df1['name]'.value_counts(dropna=False) find unique count value
print(df1.corr())