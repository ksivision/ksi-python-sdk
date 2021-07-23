"""
    KSI Public API

    # Introduction This is the KSI Vision API, in the following sections it is explained how to connect and get all analitycs/KPIs of your Locations.  ### What is a Location? The Locations in KSI are virtual representations of the real physical locations where the cameras system are located.  ### What is a Bot? KSI VISION bots allow adding various types of analysis to be obtained from the Location. A bot equals an analytic.  # Environments This is the base path to access the API.   API Url: https://app.ksivision.com/api.   # Parameters ## Filtering Allows to delimit and/or specify the wich results are expected considering the information provided.  ### location_id:     Type: int     Description: The endpoints that have location_id as a filter allow you to obtain all the information related to that Location     Where: You can get all the locations that you have available on the endpoint https://app.ksivision.com/api/locations.  ### bot_id:     Type: int     Description: The endpoints that have bot_id as a filter allow you to obtain all the information related to a specific Bot.     Where: You can get all the bots related to a Location in the following endpoint https://app.ksivision.com/api/bots.  ### time_bucket:     Description: It is necessary to get the information in time intervals. For example: if you want to see data for a whole year, it is convenient to group the information in time_bucket = '1 month'.  ## Pagination Allows to specify how to paginate the response items.   The maximum size limit is 100 items.    You must iterate over the pages to get all the data. All endpoints response the necessary information for the iteration.   This is an example:   ```json {     \"items\": [         {             \"time\": \"2019-08-24T14:15:22Z\",             \"sum_impressions\": 0,             \"avg_dwell_time\": 0,             \"location_id\": 0         }     ],     \"total\": 0,     \"page\": 0,     \"size\": 0 } ``` #### total:   Total items found with applied filters.   #### page:  Current page you are iterating on.    #### size:   Number of page elements.       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ksi_client_sdk
from ksi_client_sdk.model.bot_event_for_response import BotEventForResponse


class TestBotEventForResponse(unittest.TestCase):
    """BotEventForResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBotEventForResponse(self):
        """Test BotEventForResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BotEventForResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
