import logging
from ad_api.api import Profiles
from ad_api.base import AdvertisingApiException

def list_profiles(**kwargs):

    logging.info("-------------------------------------")
    logging.info("Profiles > list_profiles(%s)" % kwargs)
    logging.info("-------------------------------------")

    try:

        credentials = dict(
            refresh_token = "[YOUR CREDENTIALS]",
            client_secret = "[YOUR CREDENTIALS]",
            profile_id = "[YOUR CREDENTIALS]",
        )
        
        
        result = Profiles(credentials=credentials).list_profiles(
            **kwargs
        )
        logging.info(result)

        accounts_info = result.payload

        for account_info in accounts_info:
            logging.info(account_info)

    except AdvertisingApiException as error:
        logging.info(error)

list_profiles()
# list_profiles(profileTypeFilter="seller")
# list_profiles(profileTypeFilter="vendor")
# list_profiles(profileTypeFilter="agency")
# list_profiles(accessLevel="edit")
# list_profiles(apiProgram="store")
# list_profiles(validPaymentMethodFilter="true")