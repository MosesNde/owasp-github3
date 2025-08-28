 from geonode.upload.models import Upload
 from geonode.base.models import ResourceBase
 from geonode.storage.manager import storage_manager
from geonode.utils import resolve_object, check_ogc_backend, get_headers, http_client, json_response
 from geonode.base.enumerations import LINK_TYPES as _LT
 
 from geonode import geoserver  # noqa
             _remote_host = urlsplit(_s.base_url).hostname
             PROXY_ALLOWED_HOSTS += (_remote_host,)
 
        if not validate_host(url.hostname, PROXY_ALLOWED_HOSTS):
             return HttpResponse(
                 "DEBUG is set to False but the host of the path provided to the proxy service"
                 " is not in the PROXY_ALLOWED_HOSTS setting.",