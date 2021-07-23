
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.bots_api import BotsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ksi_client_sdk.api.bots_api import BotsApi
from ksi_client_sdk.api.cameras_api import CamerasApi
from ksi_client_sdk.api.locations_api import LocationsApi
