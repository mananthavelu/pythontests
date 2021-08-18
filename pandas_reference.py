# Creating a dataframe using list
list_sample=[[1,3,4],[2,4,5]]
import pandas as pd
df=pd.DataFrame(list_sample,index=["a","b"],columns=["column1","column2","column3"])

# Creating a dataframe using dictionary
dic_sample={"column1":[1,2],"column2":[11,12]}
import pandas as pd
df=pd.DataFrame(dic_sample,index=["a","b"])

df.values

df.info()
df.head()
df.shape
df.describe()
df.values
df.columns
df.index

# Sorting and Subsetting

df.sort_values(["column1","column2"],ascending=[True,False],inplace=True)

df["column1"]

df["column1"]>1 # will result in Boolean True False etc

df[df["column1"]>1] # will result in the actual values/rows/subset of dataset
df[df["column1"]=="Hello"] # will result in the actual values/rows/subset of dataset

is_lab = df["breed"] == "Labrador"
is_brown = df["color"] == "Brown"
df[is_lab & is_brown]

df["column1"].isin([1,2,3]) # will result in the actual values/rows/subset of dataset


# Statistics using Pandas

df["column"].mean()
df["column"].median()
df["column"].min()
df["column"].max()
df["column"].var()
df["column"].std()
df["column"].sum()
df["column"].quantile()


