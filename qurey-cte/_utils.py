import os
import snowflake.connector

def getConnection():
    return snowflake.connector.connect(
        account='vj89581.eu-central-2.aws',
        user='gals',
        password='Galshuler1910ifat!',
        database='TESTS',
        schema='PUBLIC'
    )

