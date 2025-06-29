import os, configparser
from snowflake.snowpark import Session

# customize with your own local connection parameters
def getSession():
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.expanduser('~'), ".snowsql/config"))
    section = "connections.demo_conn"
    pars = {
        "account": parser.get(section, "accountname"),
        "user": parser.get(section, "username"),
        "password": parser.get(section, "password")
    }
    return Session.builder.configs(pars).create()
