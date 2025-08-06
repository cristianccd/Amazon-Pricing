# -*- coding: utf-8 -*-

import logging
from ad_api.base import AdvertisingApiException
from ad_api.api import sponsored_products
from dotenv import load_dotenv
import pandas as pd

def getcampaigns(refresh_tkn: str, cli_id: str, cli_sec: str, prof_id: str):
    
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
        print("\nProcessign Campaigns...")
        print("======================\n")
        
        cmp = sponsored_products.Campaigns(credentials=credentials).list_campaigns()
        pd.set_option('display.max_columns', None)
        df_cmp = pd.DataFrame(cmp.payload)
        
        print(df_cmp)
        
        print("\nFinished...")
        print("===========")
              
        return df_cmp

    except AdvertisingApiException as error:
        logging.info(error)
        