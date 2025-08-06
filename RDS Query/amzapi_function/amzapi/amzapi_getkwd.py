# -*- coding: utf-8 -*-

import logging
from ad_api.base import AdvertisingApiException
from ad_api.api.sp import Keywords
from ad_api.api.sp import BidRecommendations
from dotenv import load_dotenv
import pandas as pd

def getkwdlist(refresh_tkn: str, cli_id: str, cli_sec: str, prof_id: str, *adgroup_id: str):
    
    """
    
    Parameters
    ----------
    refresh_token = Refresh token from AMZ ads
    client_id = Your client id
    client_secret = Your client secret
    profile_id = your profile id
    adgroup_id = the adgroup id from the keywords. If empty, all groups will be returned

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
        #first get all the keywords and their ids
        kwd=Keywords(credentials=credentials).list_keywords()
        keywords = kwd.payload
        #create a dataframe to work with the keywords
        df_kwd = pd.DataFrame(keywords)
        #copy only the adgroupid
        
        adgroup_id = str(adgroup_id[0])
        if adgroup_id != "":
            df_kwd_campaign = df_kwd[(df_kwd['adGroupId'] == int(adgroup_id)) & (df_kwd['state'] == 'enabled')].copy()
        #only copy the enabled ones
        else:
            df_kwd_campaign = df_kwd[(df_kwd['state'] == 'enabled')].copy()
        #add 3 columns: max min suggested
        df_kwd_campaign = df_kwd_campaign.assign(maxbid = 0, minbid = 0, suggestedbid = 0)
        
        print("\nProcessign Keywords...")
        print("======================\n")
        for i in range(df_kwd_campaign.shape[0]):
            try:
                    brc=BidRecommendations(credentials=credentials).get_keyword_bid_recommendations(int(df_kwd_campaign.iloc[i,0]))
                    bidrecomenmmendations = brc.payload
                    df_brc = pd.DataFrame(bidrecomenmmendations)
                    #maxbid
                    df_kwd_campaign.iat[i,-3] = df_brc.iat[0,2]
                    #minbid
                    df_kwd_campaign.iat[i,-2] = df_brc.iat[1,2]
                    #suggested
                    df_kwd_campaign.iat[i,-1] = df_brc.iat[2,2]

            except AdvertisingApiException as error:
                logging.info(error)
                
        df_kwd_campaign = df_kwd_campaign.reset_index(drop=True)
        print(df_kwd_campaign.to_string())
        print("\nFinished...")
        print("===========")
        
        return df_kwd_campaign
   
    
    except AdvertisingApiException as error:
        logging.info(error)
        return -1
