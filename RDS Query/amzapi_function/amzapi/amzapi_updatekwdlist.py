# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:13:02 2022

@author: crist
"""
#imports
from amzapi_keyword import KeywordEntry
from amzapi_append_db import amzapi_append_db
import pandas as pd



def amzapi_updatekwdlist(endpoint: str, username: str, password: str, database_name: str, table_name: str, df: pd):
    """ 
    
    Parameters
    ----------
    endpoint = SQL database address (AWS)
    username = your username
    password = your obfuscated password
    database_name = the database name
    table_name = the table name
    df = the dataframe containing all the keywords
    
    Returns
    ------
    keyword_list: true when succeded and the error message when fail
    """

    try:
        #readout the list and convert it to an array of keyword element
        kwd_arr = []
        
        print("\nUpdating entries...")
        print("======================\n")
        count = 0
        for i in range(df.shape[0]):
            kwd_arr.append(
                KeywordEntry(
                    keywordId = df.iloc[i,0],
                    adGroupId = df.iloc[i,1],
                    campaignId = df.iloc[i,2],
                    kwd_name = df.iloc[i,3],
                    kwd_match = df.iloc[i,4],
                    kwd_status = df.iloc[i,5],
                    curr_bid = df.iloc[i,6],
                    max_bid = df.iloc[i,7],
                    min_bid = df.iloc[i,8],
                    sugg_bid = df.iloc[i,9])
                )
            amzapi_append_db(endpoint, username, password, database_name, table_name, kwd_arr[i])
            count += 1
            
        print("\n")
        print("Finished... Updated "+str(count)+" registries...")
        print("===================================")
           
        #return the result
        return True
    
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                          # but may be overridden in exception subclasses
                          
