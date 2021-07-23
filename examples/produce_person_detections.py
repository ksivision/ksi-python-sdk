from datetime import datetime
import time
import ksi_client_sdk as ksi_client_sdk
from pprint import pprint
from ksi_client_sdk.api import cameras_api

configuration = ksi_client_sdk.Configuration(
    host = "http://ksi-domain",
    access_token = 'Personal Access Token'
)

# Enter a context with an instance of the API client
with ksi_client_sdk.ApiClient(configuration) as api_client:

    # Create an instance of the API class
    camera_api_instance = cameras_api.CamerasApi(api_client)
    location_id = 1 # int | Location id to filter. (optional)
    page = 0 # int |  (optional) (default to 0)
    size = 50 # int |  (optional) (default to 50)
    camera_name = "Camera Name" # Camera Name to send person detections

    try:
        # Get All Bots
        api_response = camera_api_instance.get_all_cameras_api_cameras_get(location_id=location_id, page=page, size=size)
        pprint(api_response)
        cameras = api_response["items"]
        camera = next((item for item in cameras if item["description"] == camera_name), None)
        if camera == None:
            raise Exception("Not camera found")
        
        # Person detections are simulated and sent to the KSI platform
        init_x = 200 
        init_y = 500 
        step = 0
        for n in range(1,1000):
            body = {
                        "camera_id": camera.id,
                        "timestamp": datetime.utcnow(),
                        "objects": [
                            {
                                "id": 1,
                                "class_name": "person",
                                "box": {
                                    "x1": init_x + step,
                                    "y1": init_y,
                                    "x2": init_x + step + 10,
                                    "y2": init_y
                                }
                            }
                        ]
                    }
            api_response = camera_api_instance.add_persons_detections_camera_api_cameras_person_detections_post(node_detections_request=body)
            pprint(api_response)
            step += 10
            if step > 1920:
                step = 0

            time.sleep(0.1)

    except ksi_client_sdk.ApiException as e:
        print("Exception when calling CamerasApi: %s\n" % e)
    except Exception as e:
        print("Exception adding person detections: %s\n" % e)