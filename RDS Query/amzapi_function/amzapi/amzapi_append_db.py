# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:13:02 2022

@author: crist
"""
#imports
import sqlalchemy as db
import base64
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert
from sqlalchemy import MetaData
from amzapi_keyword import KeywordEntry



def amzapi_append_db(endpoint: str, username: str, password: str, database_name: str, table_name: str, KwdEntry: KeywordEntry):
    
    """ 
    
    Parameters
    ----------
    endpoint = SQL database address (AWS)
    username = your username
    password = your obfuscated password
    database_name = the database name
    table_name = the table name
    KwdEntry = a keyword entry with the info of each keyword

    Returns
    ------
    keyword_list: true when succesfull or the error code when fail
    """

    #decode the password
    passwd = base64.b64decode(password).decode("ascii")
    #create the connection string
    conn_str = "mysql+pymysql://"+username+":"+passwd+"@"+endpoint+"/"+database_name
    
    try:
        # Create engine
        engine = db.create_engine(conn_str)
        # Connect
        connection = engine.connect()
        # Create MetaData instance
        meta = MetaData()
        meta.reflect(bind=engine)
        # Get Table
        table = meta.tables[table_name]
        # Insert value
        stmt = insert(table).values(
            keywordId = KwdEntry.keywordId,
            adGroupId = KwdEntry.adGroupId,
            campaignId = KwdEntry.campaignId,
            kwd_name = KwdEntry.kwd_name,
            kwd_match = KwdEntry.kwd_match,
            kwd_status = KwdEntry.kwd_status,
            curr_bid = KwdEntry.curr_bid,
            max_bid = KwdEntry.max_bid,
            min_bid = KwdEntry.min_bid,
            sugg_bid = KwdEntry.sugg_bid)
        
        # =============================================================================
        # 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        #     keywordId VARCHAR(255) NOT NULL PRIMARY KEY,
        #     adGroupId VARCHAR(255) NOT NULL,
        #     campaignId VARCHAR(255) NOT NULL,
        #     kwd_name VARCHAR(255) NOT NULL,
        #     kwd_match VARCHAR(255) NOT NULL,
        #     curr_bid DECIMAL(4,2) NOT NULL,
        #     kwd_status ENUM('enabled', 'paused', 'archived') NOT NULL,
        #     max_bid DECIMAL(4,2) NOT NULL,
        #     min_bid DECIMAL(4,2) NOT NULL,
        #     sugg_bid DECIMAL(4,2) NOT NULL
        # =============================================================================

        connection.execute(stmt)
        
        #return the list
        return True
    
    except SQLAlchemyError as e:
      error = str(e.__dict__['orig'])
      print(error)
      return error
