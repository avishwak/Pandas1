# Problem 4 :Customer Who Never Order	(	https://leetcode.com/problems/customers-who-never-order/  )

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, 'left', left_on='id', right_on='customerId')
    df = df[df['customerId'].isna()][['name']].rename(columns={'name':'Customers'})
    return df

# 'left_on' and 'right_on' are very important here because both tables have a column named 'id',
# but they mean different things