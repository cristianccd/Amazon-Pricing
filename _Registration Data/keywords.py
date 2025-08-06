# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:36:21 2022

@author: crist
"""

from ad_api.api.sb.keywords import Keywords
from ad_api.api import sponsored_products


my_credentials = dict(
    refresh_token='[YOUR CREDENTIALS]',
    client_id='[YOUR CREDENTIALS]',
    client_secret='[YOUR CREDENTIALS]',
    profile_id='[YOUR CREDENTIALS]',
)



result=sponsored_products.Campaigns(credentials=my_credentials).list_campaigns()

result = Keywords().list_keywords()


print(result)