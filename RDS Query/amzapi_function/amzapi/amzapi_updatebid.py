# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:45:52 2022

@author: crist
"""
# -*- coding: utf-8 -*-

import logging
from ad_api.base import AdvertisingApiException
from ad_api.api.sp import Keywords
from dotenv import load_dotenv
import pandas as pd
import json



def updatebid(refresh_token: str, client_id: str, client_secret: str, profile_id: str, adgroup_id: str, keyword_id: str, newbid: int):
    
    """
    
    Parameters
    ----------
    refresh_token = Refresh token from AMZ ads
    client_id = Your client id
    client_secret = Your client secret
    profile_id = your profile id
    adgroup_id = the adgroup id from the keywords
    keyword_id = keyword id
    newbid = new bid

    Returns
    ------
    keyword_list: dataframe with updated bid
    """

    #Load environment
    load_dotenv()
    
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )
    
    credentials = dict(
        refresh_token = refresh_token,
        client_id = client_id,
        client_secret = client_secret,
        profile_id = profile_id,
    )
    
    try:
        #first get the keyword
        kwd = Keywords(credentials=credentials).get_keyword(keyword_id)
        #create a dataframe to work with the keywords
        df_kwd = pd.DataFrame(kwd.payload, index=[0])
        
        #update only if enabled
        if df_kwd.iat[0,-2] == "enabled":
            data =  [{"keywordId": keyword_id,"state": "enabled","bid": round(newbid,2)}]
            kwdbid = Keywords(credentials=credentials).edit_keywords(body=json.dumps(data))
            return (df_kwd)
        return -1
    
    except AdvertisingApiException as error:
        logging.info(error)
        return -1
