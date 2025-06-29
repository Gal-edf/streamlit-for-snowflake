import os
from snowflake.snowpark import Session
import snowflake.connector

def getSession():
    return Session.builder.configs({
        "account": 'vj89581.eu-central-2.aws',
        "user": 'gals',
        "password": 'Galshuler1910ifat!',
        "database": 'TESTS',
        "schema": 'PUBLIC'
    }).create()


def getConnection():
    return snowflake.connector.connect(
        account='vj89581.eu-central-2.aws',
        user='gals',
        password='Galshuler1910ifat!',
        database='TESTS',
        schema='PUBLIC'
    )

