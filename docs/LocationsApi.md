# ksi_client_sdk.LocationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_locations_api_locations_get**](LocationsApi.md#get_all_locations_api_locations_get) | **GET** /api/locations | Get all locations
[**get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get**](LocationsApi.md#get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get) | **GET** /api/locations/{location_id}/kpis/area-performance | Get Location Kpis Area Performance
[**get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get**](LocationsApi.md#get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get) | **GET** /api/locations/{location_id}/kpis/distribution | Get Location Kpis Distribution
[**get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get**](LocationsApi.md#get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get) | **GET** /api/locations/{location_id}/kpis/exterior-analysis | Get Location Kpis Exterior Analysis
[**get_location_kpis_performance_api_locations_location_id_kpis_performance_get**](LocationsApi.md#get_location_kpis_performance_api_locations_location_id_kpis_performance_get) | **GET** /api/locations/{location_id}/kpis/performance | Get Location Kpis Performance
[**get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get**](LocationsApi.md#get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get) | **GET** /api/locations/{location_id}/kpis/total-visitors | Get Location Kpis Total Visitors
[**get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get**](LocationsApi.md#get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get) | **GET** /api/locations/{location_id}/kpis/traffic | Get Location Kpis Traffic


# **get_all_locations_api_locations_get**
> [LocationForResponse] get_all_locations_api_locations_get()

Get all locations

### Example

* Bearer Authentication (APIToken):
```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import locations_api
from ksi_client_sdk.model.location_for_response import LocationForResponse
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
    api_instance = locations_api.LocationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all locations
        api_response = api_instance.get_all_locations_api_locations_get()
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_all_locations_api_locations_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LocationForResponse]**](LocationForResponse.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get**
> PageKPIAreaPerformanceForResponse get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get(location_id)

Get Location Kpis Area Performance

### Example

* Bearer Authentication (APIToken):
```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import locations_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
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
    api_instance = locations_api.LocationsApi(api_client)
    location_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601. (optional)
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601. (optional)
    time_bucket =  # dict | Time bucket of query items. (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Location Kpis Area Performance
        api_response = api_instance.get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Location Kpis Area Performance
        api_response = api_instance.get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get(location_id, from_time=from_time, to_time=to_time, time_bucket=time_bucket, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_area_performance_api_locations_location_id_kpis_area_performance_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. | [optional]
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. | [optional]
 **time_bucket** | **dict**| Time bucket of query items. | [optional]
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

# **get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get**
> PageKPILocationDistributionForResponse get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get(location_id)

Get Location Kpis Distribution

### Example

* Bearer Authentication (APIToken):
```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import locations_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.page_kpi_location_distribution_for_response import PageKPILocationDistributionForResponse
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
    api_instance = locations_api.LocationsApi(api_client)
    location_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601. (optional)
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601. (optional)
    time_bucket =  # dict | Time bucket of query items. (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Location Kpis Distribution
        api_response = api_instance.get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Location Kpis Distribution
        api_response = api_instance.get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get(location_id, from_time=from_time, to_time=to_time, time_bucket=time_bucket, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_distribution_api_locations_location_id_kpis_distribution_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. | [optional]
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. | [optional]
 **time_bucket** | **dict**| Time bucket of query items. | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPILocationDistributionForResponse**](PageKPILocationDistributionForResponse.md)

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

# **get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get**
> PageKPIExteriorAnalysisForResponse get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get(location_id)

Get Location Kpis Exterior Analysis

### Example

* Bearer Authentication (APIToken):
```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import locations_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
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
    api_instance = locations_api.LocationsApi(api_client)
    location_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601. (optional)
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601. (optional)
    time_bucket =  # dict | Time bucket of query items. (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Location Kpis Exterior Analysis
        api_response = api_instance.get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Location Kpis Exterior Analysis
        api_response = api_instance.get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get(location_id, from_time=from_time, to_time=to_time, time_bucket=time_bucket, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_exterior_analysis_api_locations_location_id_kpis_exterior_analysis_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. | [optional]
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. | [optional]
 **time_bucket** | **dict**| Time bucket of query items. | [optional]
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

# **get_location_kpis_performance_api_locations_location_id_kpis_performance_get**
> PageKPILocationPerformanceForResponse get_location_kpis_performance_api_locations_location_id_kpis_performance_get(location_id)

Get Location Kpis Performance

### Example

* Bearer Authentication (APIToken):
```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import locations_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.page_kpi_location_performance_for_response import PageKPILocationPerformanceForResponse
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
    api_instance = locations_api.LocationsApi(api_client)
    location_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601. (optional)
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601. (optional)
    time_bucket =  # dict | Time bucket of query items. (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Location Kpis Performance
        api_response = api_instance.get_location_kpis_performance_api_locations_location_id_kpis_performance_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_performance_api_locations_location_id_kpis_performance_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Location Kpis Performance
        api_response = api_instance.get_location_kpis_performance_api_locations_location_id_kpis_performance_get(location_id, from_time=from_time, to_time=to_time, time_bucket=time_bucket, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_performance_api_locations_location_id_kpis_performance_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. | [optional]
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. | [optional]
 **time_bucket** | **dict**| Time bucket of query items. | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPILocationPerformanceForResponse**](PageKPILocationPerformanceForResponse.md)

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

# **get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get**
> PageKPITotalVisitorsForResponse get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get(location_id)

Get Location Kpis Total Visitors

### Example

* Bearer Authentication (APIToken):
```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import locations_api
from ksi_client_sdk.model.http_validation_error import HTTPValidationError
from ksi_client_sdk.model.page_kpi_total_visitors_for_response import PageKPITotalVisitorsForResponse
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
    api_instance = locations_api.LocationsApi(api_client)
    location_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601. (optional)
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601. (optional)
    time_bucket =  # dict | Time bucket of query items. (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Location Kpis Total Visitors
        api_response = api_instance.get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Location Kpis Total Visitors
        api_response = api_instance.get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get(location_id, from_time=from_time, to_time=to_time, time_bucket=time_bucket, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_total_visitors_api_locations_location_id_kpis_total_visitors_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. | [optional]
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. | [optional]
 **time_bucket** | **dict**| Time bucket of query items. | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**PageKPITotalVisitorsForResponse**](PageKPITotalVisitorsForResponse.md)

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

# **get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get**
> PageKPITrafficForResponse get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get(location_id)

Get Location Kpis Traffic

### Example

* Bearer Authentication (APIToken):
```python
import time
import ksi_client_sdk
from ksi_client_sdk.api import locations_api
from ksi_client_sdk.model.page_kpi_traffic_for_response import PageKPITrafficForResponse
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
    api_instance = locations_api.LocationsApi(api_client)
    location_id = 1 # int | 
    from_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date from fetch results. Format ISO-8601. (optional)
    to_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date to fetch results. Format ISO-8601. (optional)
    time_bucket =  # dict | Time bucket of query items. (optional)
    is_entrance = True # bool | Flag to filter entrance bots. Don't set to ignore condition. (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Location Kpis Traffic
        api_response = api_instance.get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get(location_id)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Location Kpis Traffic
        api_response = api_instance.get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get(location_id, from_time=from_time, to_time=to_time, time_bucket=time_bucket, is_entrance=is_entrance, page=page, size=size)
        pprint(api_response)
    except ksi_client_sdk.ApiException as e:
        print("Exception when calling LocationsApi->get_location_kpis_traffic_api_locations_location_id_kpis_traffic_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **int**|  |
 **from_time** | **datetime**| Date from fetch results. Format ISO-8601. | [optional]
 **to_time** | **datetime**| Date to fetch results. Format ISO-8601. | [optional]
 **time_bucket** | **dict**| Time bucket of query items. | [optional]
 **is_entrance** | **bool**| Flag to filter entrance bots. Don&#39;t set to ignore condition. | [optional]
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

