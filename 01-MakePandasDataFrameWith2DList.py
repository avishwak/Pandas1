# Problem 1 : Make a Pandas DataFrame with two-dimensional list	(	https://www.geeksforgeeks.org/make-a-pandas-dataframe-with-two-dimensional-list-python/)

import pandas as pd

data = [
    ['Geek1', 26, 'Scientist'],
    ['Geek2', 31, 'Researcher'],
    ['Geek3', 24, 'Engineer']
]

cols = ['Name', 'Age', 'Occupation']

# method 1: using pd.DataFrame()
df = pd.DataFrame(data, columns=cols) 

#if columns not provided, it will be assigned as 0, 1, 2, ...
#2nd arg in DataFrame constructor is index, so if I provide cols without specifying columns, it will be used as index

# method 2: using pd.DataFrame.from_records()
df = pd.DataFrame.from_records(data, columns=cols)

# method 3: using pd.DataFrame.from_dict()
df = pd.DataFrame.from_dict(dict(zip(cols, zip(*data))))

# other ways of creating a DataFrame
customers = pd.DataFrame({'id':[1,2,3,4], \
                          'name':['Joe', 'Henry', 'Sam', 'Max']})