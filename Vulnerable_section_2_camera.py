 
 from homeassistant.components.camera import Camera, CameraEntityFeature
 from homeassistant.helpers.entity_platform import AddEntitiesCallback
 
 from .const import DOMAIN, CONF_HOST, CONF_USERNAME, CONF_PASSWORD, DEFAULT_HOST, CONF_VERIFY_SSL
 
             "identifiers": {(DOMAIN, host)},
             "name": "Intelbras 3542 MFW Camera",
             "manufacturer": "Intelbras",
         }
 
         # Build the RTSP URL with proper credentials and protocol.