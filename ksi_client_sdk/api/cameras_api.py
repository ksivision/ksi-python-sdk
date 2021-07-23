"""
    KSI Public API

    # Introduction This is the KSI Vision API, in the following sections it is explained how to connect and get all analitycs/KPIs of your Locations.  ### What is a Location? The Locations in KSI are virtual representations of the real physical locations where the cameras system are located.  ### What is a Bot? KSI VISION bots allow adding various types of analysis to be obtained from the Location. A bot equals an analytic.  # Environments This is the base path to access the API.   API Url: https://app.ksivision.com/api.   # Parameters ## Filtering Allows to delimit and/or specify the wich results are expected considering the information provided.  ### location_id:     Type: int     Description: The endpoints that have location_id as a filter allow you to obtain all the information related to that Location     Where: You can get all the locations that you have available on the endpoint https://app.ksivision.com/api/locations.  ### bot_id:     Type: int     Description: The endpoints that have bot_id as a filter allow you to obtain all the information related to a specific Bot.     Where: You can get all the bots related to a Location in the following endpoint https://app.ksivision.com/api/bots.  ### time_bucket:     Description: It is necessary to get the information in time intervals. For example: if you want to see data for a whole year, it is convenient to group the information in time_bucket = '1 month'.  ## Pagination Allows to specify how to paginate the response items.   The maximum size limit is 100 items.    You must iterate over the pages to get all the data. All endpoints response the necessary information for the iteration.   This is an example:   ```json {     \"items\": [         {             \"time\": \"2019-08-24T14:15:22Z\",             \"sum_impressions\": 0,             \"avg_dwell_time\": 0,             \"location_id\": 0         }     ],     \"total\": 0,     \"page\": 0,     \"size\": 0 } ``` #### total:   Total items found with applied filters.   #### page:  Current page you are iterating on.    #### size:   Number of page elements.       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ksi_client_sdk.api_client import ApiClient, Endpoint as _Endpoint
from ksi_client_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.message_response import MessageResponse
from ksi_client_sdk.model.node_detections_request import NodeDetectionsRequest
from ksi_client_sdk.model.page_camera_for_response import PageCameraForResponse


class CamerasApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_persons_detections_camera_api_cameras_person_detections_post(
            self,
            node_detections_request,
            **kwargs
        ):
            """Add persons detections for the camera  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_persons_detections_camera_api_cameras_person_detections_post(node_detections_request, async_req=True)
            >>> result = thread.get()

            Args:
                node_detections_request (NodeDetectionsRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MessageResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['node_detections_request'] = \
                node_detections_request
            return self.call_with_http_info(**kwargs)

        self.add_persons_detections_camera_api_cameras_person_detections_post = _Endpoint(
            settings={
                'response_type': (MessageResponse,),
                'auth': [
                    'APIToken'
                ],
                'endpoint_path': '/api/cameras/person-detections',
                'operation_id': 'add_persons_detections_camera_api_cameras_person_detections_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'node_detections_request',
                ],
                'required': [
                    'node_detections_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'node_detections_request':
                        (NodeDetectionsRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'node_detections_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__add_persons_detections_camera_api_cameras_person_detections_post
        )

        def __get_all_cameras_api_cameras_get(
            self,
            **kwargs
        ):
            """Get All Cameras  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_all_cameras_api_cameras_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                location_id (int): Location id to filter.. [optional]
                page (int): [optional] if omitted the server will use the default value of 0
                size (int): [optional] if omitted the server will use the default value of 50
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PageCameraForResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_all_cameras_api_cameras_get = _Endpoint(
            settings={
                'response_type': (PageCameraForResponse,),
                'auth': [
                    'APIToken'
                ],
                'endpoint_path': '/api/cameras',
                'operation_id': 'get_all_cameras_api_cameras_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'location_id',
                    'page',
                    'size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'size',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('size',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'location_id':
                        (int,),
                    'page':
                        (int,),
                    'size':
                        (int,),
                },
                'attribute_map': {
                    'location_id': 'location_id',
                    'page': 'page',
                    'size': 'size',
                },
                'location_map': {
                    'location_id': 'query',
                    'page': 'query',
                    'size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_all_cameras_api_cameras_get
        )