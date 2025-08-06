# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:16:41 2022

@author: crist
"""

import amzapi_getkwd
from  amzapi_read_db import amzapi_read_db
from  amzapi_updatekwdlist import amzapi_updatekwdlist
import base64
import pandas as pd
import json

def amzapi_handler(event, context):

    print(chr(27) + "[2J")
    
    endp = "[YOUR CREDENTIALS]"
    user = "[YOUR CREDENTIALS]"
    #obfuscate the password
    pwd = "[YOUR CREDENTIALS]"
    pwd_enc = base64.b64encode(pwd.encode("ascii"))
    db_name = "[YOUR CREDENTIALS]"
    t_name = "[YOUR CREDENTIALS]"
    
    kwdlist = amzapi_getkwd.getkwdlist("[YOUR CREDENTIALS]",
               "[YOUR CREDENTIALS]",
               "[YOUR CREDENTIALS]",
               "[YOUR CREDENTIALS]",
               "[YOUR CREDENTIALS]")
    
    kwdlist = pd.DataFrame(kwdlist)
    
    result = amzapi_updatekwdlist(endp, user, pwd_enc, db_name, t_name, kwdlist)
    kwdb = amzapi_read_db(endp, user, pwd_enc, db_name, t_name)
    
    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": json.dumps("Execution completed...")
    }