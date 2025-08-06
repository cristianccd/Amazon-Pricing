# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:20:52 2022

@author: crist
"""

import logging
from ad_api.api import Profiles
from ad_api.base import AdvertisingApiException

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


def register_assistant(value: str):

    logging.info("-------------------------------------")
    logging.info("Profiles > register_assistant(%s)" % value)
    logging.info("-------------------------------------")

    try:

        result = Profiles(debug=True).register_assistant(
            country_code=value
        )
        logging.info(result)

    except AdvertisingApiException as error:
        logging.info(error)


if __name__ == '__main__':

    amz_country_code = "IT"
    register_assistant(amz_country_code)