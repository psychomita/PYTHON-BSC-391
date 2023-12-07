import pandas as pd
d = { 'Name' : pd.Series(["John","Aza","Zen","Ditu","Mark"],index=[1,2,3,4,5]),'Marks' : pd.Series ([40,50,20,10,30], index = [1,2,3,4,5])}
x= pd.DataFrame(d)
print(x)
