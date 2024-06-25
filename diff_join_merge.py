import pandas as pd
data1=({
    'key1':['foo','bar','veg','nonVeg'],
    'lval':[1,2,3,4]
})

data2=({
    'key2':['foo','bar'],
    'rval':[4,5]
})

df1=pd.DataFrame(data1)
df1.index=['a','b']

print(df1)

df2=pd.DataFrame(data2)
df2.index=['c','d']
print(df2)




# *****************join****************

# join=df1.join(df2)               # ************* It by default perform left join**********
# print(join)

# ****************merge*****************


merge=pd.merge(df1,df2,on='key1', how='left')
# merge=df1.merge(df2)
print(merge)





