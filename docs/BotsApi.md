# ksi_client_sdk.BotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_bots_api_bots_get**](BotsApi.md#get_all_bots_api_bots_get) | **GET** /api/bots | Get All Bots
[**get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get**](BotsApi.md#get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get) | **GET** /api/bots/{bot_id}/events/covid-19-prevention | Get Bot Events Covid 19 Prevention
[**get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get**](BotsApi.md#get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get) | **GET** /api/bots/{bot_id}/events/queue-management | Get Bot Events Queue Management
[**get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get**](BotsApi.md#get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get) | **GET** /api/bots/{bot_id}/kpis/area-performance | Get Bot Kpis Area Performance
[**get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get**](BotsApi.md#get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get) | **GET** /api/bots/{bot_id}/kpis/exterior-analysis | Get Bot Kpis Exterior Analysis
[**get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get**](BotsApi.md#get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get) | **GET** /api/bots/{bot_id}/kpis/queue-management | Get Bot Kpis Queue Managment
[**get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get**](BotsApi.md#get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get) | **GET** /api/bots/{bot_id}/kpis/traffic | Get Bot Kpis Traffic
[**get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get**](BotsApi.md#get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get) | **GET** /api/bots/{bot_id}/kpis/traffic-features | Get Bot Kpis Traffic With  Data Features


# **get_all_bots_api_bots_get**
> PageBotForResponse get_all_bots_api_bots_get(location_id)

Get All Bots

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.page_bot_for_response import PageBotForResponse
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
    api_instance = bots_api.BotsApi(api_client)
    location_id = 1 # int | Location id to filter.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get All Bots
        api_response = api_instance.get_all_bots_api_bots_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_all_bots_api_bots_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Bots
        api_response = api_instance.get_all_bots_api_bots_get(location_id, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_all_bots_api_bots_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**| Location id to filter. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageBotForResponse**](PageBotForResponse.md)

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

# **get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get**
> PageBotEventForResponse get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get(bot_id, from_time, to_time)

Get Bot Events Covid 19 Prevention

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.page_bot_event_for_response import PageBotEventForResponse
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
    api_instance = bots_api.BotsApi(api_client)
    bot_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601.
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Bot Events Covid 19 Prevention
        api_response = api_instance.get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get(bot_id, from_time, to_time)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bot Events Covid 19 Prevention
        api_response = api_instance.get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get(bot_id, from_time, to_time, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_events_covid19_prevention_api_bots_bot_id_events_covid19_prevention_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. |
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageBotEventForResponse**](PageBotEventForResponse.md)

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

# **get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get**
> PageBotEventForResponse get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get(bot_id, from_time, to_time)

Get Bot Events Queue Management

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.page_bot_event_for_response import PageBotEventForResponse
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
    api_instance = bots_api.BotsApi(api_client)
    bot_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601.
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Bot Events Queue Management
        api_response = api_instance.get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get(bot_id, from_time, to_time)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bot Events Queue Management
        api_response = api_instance.get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get(bot_id, from_time, to_time, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_events_queue_management_api_bots_bot_id_events_queue_management_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. |
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageBotEventForResponse**](PageBotEventForResponse.md)

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

# **get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get**
> PageKPIAreaPerformanceForResponse get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get(bot_id, time_bucket, from_time, to_time)

Get Bot Kpis Area Performance

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.time_bucket import TimeBucket
from ksi_client_sdk.model.page_kpi_area_performance_for_response import PageKPIAreaPerformanceForResponse
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
    api_instance = bots_api.BotsApi(api_client)
    bot_id = 1 # int | 
    time_bucket = TimeBucket("1 hour") # TimeBucket | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601.
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Bot Kpis Area Performance
        api_response = api_instance.get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get(bot_id, time_bucket, from_time, to_time)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bot Kpis Area Performance
        api_response = api_instance.get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get(bot_id, time_bucket, from_time, to_time, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_area_performance_api_bots_bot_id_kpis_area_performance_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  |
 **time_bucket** | **TimeBucket**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. |
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPIAreaPerformanceForResponse**](PageKPIAreaPerformanceForResponse.md)

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

# **get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get**
> PageKPIExteriorAnalysisForResponse get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get(bot_id, time_bucket, from_time, to_time)

Get Bot Kpis Exterior Analysis

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.time_bucket import TimeBucket
from ksi_client_sdk.model.page_kpi_exterior_analysis_for_response import PageKPIExteriorAnalysisForResponse
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
    api_instance = bots_api.BotsApi(api_client)
    bot_id = 1 # int | 
    time_bucket = TimeBucket("1 hour") # TimeBucket | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601.
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Bot Kpis Exterior Analysis
        api_response = api_instance.get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get(bot_id, time_bucket, from_time, to_time)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bot Kpis Exterior Analysis
        api_response = api_instance.get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get(bot_id, time_bucket, from_time, to_time, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_exterior_analysis_api_bots_bot_id_kpis_exterior_analysis_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  |
 **time_bucket** | **TimeBucket**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. |
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPIExteriorAnalysisForResponse**](PageKPIExteriorAnalysisForResponse.md)

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

# **get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get**
> PageKPIQueueManagmentResponse get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get(bot_id, time_bucket, from_time, to_time)

Get Bot Kpis Queue Managment

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.page_kpi_queue_managment_response import PageKPIQueueManagmentResponse
from ksi_client_sdk.model.time_bucket import TimeBucket
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
    api_instance = bots_api.BotsApi(api_client)
    bot_id = 1 # int | 
    time_bucket = TimeBucket("1 hour") # TimeBucket | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601.
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Bot Kpis Queue Managment
        api_response = api_instance.get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get(bot_id, time_bucket, from_time, to_time)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bot Kpis Queue Managment
        api_response = api_instance.get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get(bot_id, time_bucket, from_time, to_time, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_queue_managment_api_bots_bot_id_kpis_queue_management_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  |
 **time_bucket** | **TimeBucket**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. |
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPIQueueManagmentResponse**](PageKPIQueueManagmentResponse.md)

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

# **get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get**
> PageKPITrafficForResponse get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get(bot_id, time_bucket, from_time, to_time)

Get Bot Kpis Traffic

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.page_kpi_traffic_for_response import PageKPITrafficForResponse
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.time_bucket import TimeBucket
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
    api_instance = bots_api.BotsApi(api_client)
    bot_id = 1 # int | 
    time_bucket = TimeBucket("1 hour") # TimeBucket | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601.
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Bot Kpis Traffic
        api_response = api_instance.get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get(bot_id, time_bucket, from_time, to_time)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bot Kpis Traffic
        api_response = api_instance.get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get(bot_id, time_bucket, from_time, to_time, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_traffic_api_bots_bot_id_kpis_traffic_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  |
 **time_bucket** | **TimeBucket**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. |
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPITrafficForResponse**](PageKPITrafficForResponse.md)

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

# **get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get**
> PageKPITrafficWithFeaturesForResponse get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get(bot_id, from_time, to_time)

Get Bot Kpis Traffic With  Data Features

### Example

* Bearer Authentication (APIToken):

```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import bots_api
from ksi_client_sdk.model.page_kpi_traffic_with_features_for_response import PageKPITrafficWithFeaturesForResponse
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
    api_instance = bots_api.BotsApi(api_client)
    bot_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601.
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601.
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Bot Kpis Traffic With  Data Features
        api_response = api_instance.get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get(bot_id, from_time, to_time)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Bot Kpis Traffic With  Data Features
        api_response = api_instance.get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get(bot_id, from_time, to_time, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling BotsApi->get_bot_kpis_traffic_with_data_features_api_bots_bot_id_kpis_traffic_features_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. |
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPITrafficWithFeaturesForResponse**](PageKPITrafficWithFeaturesForResponse.md)

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

