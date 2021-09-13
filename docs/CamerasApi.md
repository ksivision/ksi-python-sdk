# ksi_client_sdk.CamerasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_persons_detections_camera_api_cameras_person_detections_post**](CamerasApi.md#add_persons_detections_camera_api_cameras_person_detections_post) | **POST** /api/cameras/person-detections | Add persons detections for the camera
[**get_all_cameras_api_cameras_get**](CamerasApi.md#get_all_cameras_api_cameras_get) | **GET** /api/cameras | Get All Cameras


# **add_persons_detections_camera_api_cameras_person_detections_post**
> MessageResponse add_persons_detections_camera_api_cameras_person_detections_post(node_detections_request)

Add persons detections for the camera

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import cameras_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.node_detections_request import NodeDetectionsRequest
from ksi_client_sdk.model.message_response import MessageResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ksi_client_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIToken
configuration = ksi_client_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ksi_client_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cameras_api.CamerasApi(api_client)
    node_detections_request = NodeDetectionsRequest(
        location_id=1,
        camera_id=1,
        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        objects=[
            NodeDetectionObject(
                id=1,
                uuid="",
                class_name="person",
                box=NodeDetectionBox(
                    x1=3.14,
                    y1=3.14,
                    x2=3.14,
                    y2=3.14,
                ),
                rot_bbox=[
                    3.14,
                ],
                in_camera_zone=True,
                image_path="image_path_example",
            ),
        ],
    ) # NodeDetectionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add persons detections for the camera
        api_response = api_instance.add_persons_detections_camera_api_cameras_person_detections_post(node_detections_request)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling CamerasApi->add_persons_detections_camera_api_cameras_person_detections_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_detections_request** | [**NodeDetectionsRequest**](NodeDetectionsRequest.md)|  |

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cameras_api_cameras_get**
> PageCameraForResponse get_all_cameras_api_cameras_get(location_id)

Get All Cameras

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import cameras_api
from ksi_client_sdk.model.page_camera_for_response import PageCameraForResponse
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ksi_client_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIToken
configuration = ksi_client_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ksi_client_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cameras_api.CamerasApi(api_client)
    location_id = 1 # int | Location id to filter.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get All Cameras
        api_response = api_instance.get_all_cameras_api_cameras_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling CamerasApi->get_all_cameras_api_cameras_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Cameras
        api_response = api_instance.get_all_cameras_api_cameras_get(location_id, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling CamerasApi->get_all_cameras_api_cameras_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Location id to filter. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageCameraForResponse**](PageCameraForResponse.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

