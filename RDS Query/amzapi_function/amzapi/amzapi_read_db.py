# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:13:02 2022

@author: crist
"""
#imports
import sqlalchemy as db
import base64
import pandas as pd
import time
from sqlalchemy.exc import SQLAlchemyError


def amzapi_read_db(endpoint: str, username: str, password: str, database_name: str, table_name: str):
    
    """Calculate product of two inputs. 
    
    Parameters
    ----------
    endpoint = SQL database address (AWS)
    username = your username
    password = your obfuscated password
    database_name = the database name

    Returns
    ------
    keyword_list: dataframe with all the keywords from the defined adgroup and their relevant bidding information
    """

    #decode the password
    passwd = base64.b64decode(password).decode("ascii")
    #create the connection string
    conn_str = "mysql+pymysql://"+username+":"+passwd+"@"+endpoint+"/"+database_name
    
    try:
        #create engine
        engine = db.create_engine(conn_str)
        #connect
        connection = engine.connect()
         
        print("\nRetrieving database... Time: "+ time.strftime("%Y-%m-%d %H:%M"))
        print("=============================================\n")
        #convert sql database to pandas
        pd.set_option('display.max_columns', None)
        keywordlist = pd.read_sql("select * from "+table_name, connection);
        print(keywordlist)
        print("\n")
        print("Finished...")
        print("===========")
        #return the list
        return keywordlist
    
    except SQLAlchemyError as e:
      error = str(e.__dict__['orig'])
      print(error)
      return error
