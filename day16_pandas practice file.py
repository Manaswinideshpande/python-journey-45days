import pandas as pd 
import numpy as np

#Series: A pandas series is lika column in a table, it is a one dimensional array holding data of any type

s2 =  pd.Series([2,34,56,78,90,21],index =['maths','science','english','maths-2','social','hindi'])
print(s2)
                

s=  pd.Series([2,34,56,78,90,21],index =['maths','science','english','maths-2','social','hindi'],dtype = float)
print(s)

d = pd.DataFrame(s)
print(d)
d2 = {'Marks':[21,34,56,78,90,21],'Subjects':['maths','science','english','maths-2','social','hindi']}
d3 = pd.DataFrame(d2)
print(d3)
