# -*- coding: utf-8 -*-
"""LAB_SHEET_3__PANDASERIES.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/paradox-86678/demo-colab/blob/main/LAB_SHEET_3__PANDASERIES.ipynb
"""

import pandas as pd

s1=pd.Series([-3,-1,1,3,5 ,'gaurav',7.3])
print(s1)

print(s1[2])

a=[1,7,2]
myvar=pd.Series (a,index=['x','y','z'])
print(myvar)
print(myvar ["y"])

calories={"day1":420,"day 2":345,"day3":390}
myvar=pd.Series(calories)

print(s1[[2,1,0]])

type(s1)

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s[['a','c','d']])

data={
    "calories":[420,345,390],
    "duration":[50,40,45]
}
df=pd.DataFrame(data)
print(df)