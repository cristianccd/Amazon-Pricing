# -*- coding: utf-8 -*-

import logging
from ad_api.base import AdvertisingApiException
from ad_api.api import sponsored_products
from ad_api.api.sp import AdGroups
from dotenv import load_dotenv
import pandas as pd

def getadgroups(refresh_tkn: str, cli_id: str, cli_sec: str, prof_id: str):
    
    """
    
    Parameters
    ----------
    refresh_token = Refresh token from AMZ ads
    client_id = Your client id
    client_secret = Your client secret
    profile_id = your profile id

    Returns
    ------
    keyword_list: matrix with all the keywords from the defined adgroup and their relevant bidding information
    """

    #Load environment
    load_dotenv()
    
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )
    
    credentials = dict(
        refresh_token = refresh_tkn,
        client_id = cli_id,
        client_secret = cli_sec,
        profile_id = prof_id,
    )
    
    
    try:
        print("\nProcessign Adgroups...")
        print("======================\n")
        
        adg = AdGroups(credentials=credentials).list_ad_groups()
        df_adg = pd.DataFrame(adg.payload)
        
        print(df_adg)
        
        print("\nFinished...")
        print("===========")
              
        return df_adg

    except AdvertisingApiException as error:
        logging.info(error)
        