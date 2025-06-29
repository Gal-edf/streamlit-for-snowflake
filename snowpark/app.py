import os
from snowflake.snowpark import Session

pars = {
    "account":'vj89581.eu-central-2.aws',
    "user":'gals',
    "password":'Galshuler1910ifat!',
    "database": 'TESTS',
    "schema": 'PUBLIC'
}
session = Session.builder.configs(pars).create()

# basic usage
df = session.sql('select * from employees')
rows = df.collect()
for row in rows:
    print(row)

# alternative w/ pandas DataFrame
dfp = df.to_pandas()
print(dfp)