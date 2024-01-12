import pandas as pd

dict1 = {"Name":"Ramesh"}
print(dict1['Name'])


data = {
        'Studentname' : ['Ajay','Bijaya','Milan'],
        'Studentmarks' : [45,69,89],
        'studentresult' : ['Satisfy','good','excellent']
       }

df = pd.DataFrame(data)
print(df)