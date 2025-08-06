# -*- coding: utf-8 -*-

import logging
import amzapi_updatebid
import amzapi_getkwd
from ad_api.base import AdvertisingApiException
from dotenv import load_dotenv
import pandas as pd


#high_10_kwds = [238855657272117,174641434978471,148188776515063,271928941156622,91148830183707,44117182155710,229912579586754,84030263906493,24657515388099,43670666375582,235268014349070]
high_kwds = [0]#[121398725344244,15065000281000,75578463109113]
suggested_kwds = [0]#[185136125053399,57430632368419,146090070133161,227466984183482,100881665761292]


def updateall(refresh_token: str, client_id: str, client_secret: str, profile_id: str, adgroup_id: str, factor: float, cap: float):

    """
    
    Parameters
    ----------
    refresh_token = Refresh token from AMZ ads
    client_id = Your client id
    client_secret = Your client secret
    profile_id = your profile id
    adgroup_id = the adgroup id from the keywords
    factor = suggbid+((maxbid-suggbid)*factor)
    cap: price cap

    Returns
    ------
    keyword_list: dataframe with updated bids
    """

    #Load environment
    load_dotenv()
    
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )
    
    
    try:
        #first get all the keywords
        kwd = amzapi_getkwd.getkwdlist(refresh_token,
                   client_id,
                   client_secret,
                   profile_id,
                   adgroup_id)
        
        kwdlist = pd.DataFrame(kwd)
        
        print("Processign Keywords...")
        print("======================\n")
        
        for i in range(kwdlist.shape[0]):
            try:
                #calculate new formula
                maxbid = round(kwdlist.iat[i,-3],2)
                suggbid = round(kwdlist.iat[i,-1],2)
                currbid = round(kwdlist.iat[i,-4],2)
                word = kwdlist.iat[i,3]
                changed = " ***CHANGED***"
                #see in which bid category is each keyword and assign the new bid
                if int(kwdlist.iat[i,0]) in high_kwds:
                    newbid = round(maxbid,2)
                elif int(kwdlist.iat[i,0]) in suggested_kwds:
                    newbid = round(suggbid,2)
                else:
                    #suggested + difference between max and suggested * factor
                    newbid = round(suggbid+((maxbid-suggbid)*factor),2)
                #if it is over the cap, then do not go further
                if newbid > cap:
                    newbid = cap
                                    
                if abs(currbid - newbid) >= 0 and abs(currbid - newbid) < 0.01:
                    changed = ""
                
                print("Updating:\t "+word+" - Current Bid: "+str(currbid)+"\t- Sugg. Bid: "+str(suggbid)+"\t- New Bid: "+str(newbid)+changed)

                kwd = amzapi_updatebid.updatebid(refresh_token,
                            client_id,
                            client_secret,
                            profile_id,
                            adgroup_id,
                            int(kwdlist.iat[i,0]),#keyword_id
                            newbid)

            except AdvertisingApiException as error:
                logging.info(error)
                
        print("Finished...")
        print("===========\n")
        return True
                
    except AdvertisingApiException as error:
        logging.info(error)
        return False