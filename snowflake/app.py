import snowflake.connector
import os
import pandas as pd
conn = snowflake.connector.connect(
    account='vj89581.eu-central-2.aws',
    user='gals',
    password='Galshuler1910ifat!',
)

cur = conn.cursor()
cur.execute('SELECT * FROM tests.public.employees')
# for row in cur:
#     print(row)

df = cur.fetch_pandas_all()
print(df)