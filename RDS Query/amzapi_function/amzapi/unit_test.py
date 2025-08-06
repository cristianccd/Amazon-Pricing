# -*- coding: utf-8 -*-

import amzapi_getkwd
import amzapi_getcampaigns
import amzapi_getadgroups
import  amzapi_updatebid
import amzapi_updateall
from  amzapi_read_db import amzapi_read_db
from  amzapi_updatekwdlist import amzapi_updatekwdlist
from  amzapi_append_db import amzapi_append_db
import base64
import time
from amzapi_keyword import KeywordEntry
import pandas as pd
from dotenv import load_dotenv
import pipreqs


from ad_api.api import Profiles

load_dotenv()

print(chr(27) + "[2J")

data = []
kwdlist = pd.DataFrame(data)
cmplist = pd.DataFrame(data)
aglist = pd.DataFrame(data)
kwd = pd.DataFrame(data)

'''
**************
*GET KEYWORDS*
**************
'''

# =============================================================================
# kwd = amzapi_getkwd.getkwdlist("[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]", #IT
#             #"[YOUR CREDENTIALS]", #NL
#             #"[YOUR CREDENTIALS]"
#             #"[YOUR CREDENTIALS]"
#             #"[YOUR CREDENTIALS]"
#             #"[YOUR CREDENTIALS]" #NL BROAD
#             )
# 
# kwdlist = pd.DataFrame(kwd)
# 
# kwdlist.to_csv("Kwd_Export.csv")
# =============================================================================

'''
**************
*GET CAMPAIGNS*
**************
'''

# =============================================================================
# cmplist = amzapi_getcampaigns.getcampaigns("[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]") #NL
#             #"[YOUR CREDENTIALS]") #IT
# 
# cmplist = pd.DataFrame(cmplist)
# 
# cmplist.to_csv("Cmp_Export.csv")
# =============================================================================

'''
**************
*GET ADGROUPS*
**************
'''

# =============================================================================
# aglist = amzapi_getadgroups.getadgroups("[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             #"[YOUR CREDENTIALS]") #NL
#             #"[YOUR CREDENTIALS]") #IT
#             "[YOUR CREDENTIALS]") #TR
# 
# aglist = pd.DataFrame(aglist)
# 
# aglist.to_csv("Ag_Export.csv")
# 
# =============================================================================
'''
********************************
*UNIT TEST FOR READING DATABASE*
********************************
'''

# =============================================================================
# endp = "[YOUR CREDENTIALS]"
# user = "[YOUR CREDENTIALS]"
# #obfuscate the password
# pwd = "[YOUR CREDENTIALS]"
# pwd_enc = base64.b64encode(pwd.encode("ascii"))
# db_name = "AN_HUB_001_DB"
# t_name = "AN_HUB_001_TABLE"
# 
# kwdlist = amzapi_read_db(endpoint = endp, username = user, password = pwd_enc, database_name = db_name, table_name = t_name)
# =============================================================================

'''
*************************************
*UNIT TEST FOR APPENDING VALUE TO DB*
*************************************
'''

# =============================================================================
# endp = "[YOUR CREDENTIALS]"
# user = "[YOUR CREDENTIALS]"
# #obfuscate the password
# pwd = "[YOUR CREDENTIALS]"
# pwd_enc = base64.b64encode(pwd.encode("ascii"))
# db_name = "AN_HUB_001_DB"
# t_name = "AN_HUB_001_TABLE"
#       
# kwd = KeywordEntry(
#             "[YOUR CREDENTIALS]",
#             #"[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "usb hub",
#             "exact",
#             "1.1",
#             "enabled",
#             1.0,
#             0.55,
#             0.71)
# 
# kwdlist = amzapi_append_db(endpoint = endp, username = user, password = pwd_enc, database_name = db_name, table_name = t_name, KwdEntry = kwd)
# kwdlist = amzapi_read_db(endpoint = endp, username = user, password = pwd_enc, database_name = db_name, table_name = t_name)
# =============================================================================

'''
************************************
*UNIT TEST FOR UPDATE BUID FUNCTION*
************************************
'''

# =============================================================================
# kwd = amzapi_updatebid.updatebid("[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             #"[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]", # adattatore usb ipad
#             0.2)
# 
# kwd = amzapi_getkwd.getkwdlist("[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             "[YOUR CREDENTIALS]",
#             #"[YOUR CREDENTIALS]"
#             #"[YOUR CREDENTIALS]"
#             "[YOUR CREDENTIALS]"
#             )
# =============================================================================

'''
************************************
*UPDATE ADGROUP WITH NEW BID VALUES*
************************************
'''

kwd = amzapi_updateall.updateall("[YOUR CREDENTIALS]",
             "[YOUR CREDENTIALS]",
             #"[YOUR CREDENTIALS]", #NL
             "[YOUR CREDENTIALS]", #IT
             #"[YOUR CREDENTIALS]", #TR
             "[YOUR CREDENTIALS]", #IT EXACT
             #"[YOUR CREDENTIALS]", #NL BROAD
             #"[YOUR CREDENTIALS]", #NL EXACT
             #"[YOUR CREDENTIALS]", #NL EXACT LONG
             #"[YOUR CREDENTIALS]", #TR EXACT
             1.2, #factor
             2 #cap
             )
 

kwd = amzapi_getkwd.getkwdlist("[YOUR CREDENTIALS]",
            "[YOUR CREDENTIALS]",
            "[YOUR CREDENTIALS]",
            #"[YOUR CREDENTIALS]", #NL
            "[YOUR CREDENTIALS]", #IT
            #"[YOUR CREDENTIALS]", #TR
            "[YOUR CREDENTIALS]", #IT EXACT
            #"[YOUR CREDENTIALS]" #NL BROAD
            #"[YOUR CREDENTIALS]" #NL EXACT
            #"[YOUR CREDENTIALS]", #NL EXACT LONG
            #"[YOUR CREDENTIALS]", #TR EXACT
            )

kwdlist = pd.DataFrame(kwd)


'''
*************************************
*UPDATE DATABASE WITH CURRENT VALUES*
*************************************
'''

# =============================================================================
# endp = "[YOUR CREDENTIALS]"
# user = "[YOUR CREDENTIALS]"
# #obfuscate the password
# pwd = "[YOUR CREDENTIALS]"
# pwd_enc = base64.b64encode(pwd.encode("ascii"))
# db_name = "AN_HUB_001_DB"
# t_name = "AN_HUB_001_TABLE"
# 
# # =============================================================================
# # kwd = amzapi_updatebid.updatebid("[YOUR CREDENTIALS]",
# #             "[YOUR CREDENTIALS]",
# #             "[YOUR CREDENTIALS]",
# #             "[YOUR CREDENTIALS]",
# #             #"[YOUR CREDENTIALS]",
# #             "[YOUR CREDENTIALS]",
# #             "15065000281000", # hub usb c
# #             0.7)
# # =============================================================================
# 
# kwdlist = amzapi_getkwd.getkwdlist("[YOUR CREDENTIALS]",
#            "[YOUR CREDENTIALS]",
#            "[YOUR CREDENTIALS]",
#            "[YOUR CREDENTIALS]", #IT
#            "[YOUR CREDENTIALS]" #IT EXACT
#            )
# 
# kwdlist = pd.DataFrame(kwdlist)
# 
# result = amzapi_updatekwdlist(endp, user, pwd_enc, db_name, t_name, kwdlist)
# kwdb = amzapi_read_db(endp, user, pwd_enc, db_name, t_name)
# 
# =============================================================================
