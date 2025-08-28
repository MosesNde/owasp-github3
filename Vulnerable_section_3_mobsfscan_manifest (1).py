 
 from mobsfscan.logger import init_logger
 from mobsfscan.manifest_metadata import metadata

 
 logger = init_logger(__name__)
 ANDROID_8_0_LEVEL = 26
     '32': '12L',
     '33': '13',
     '34': '14',
 }
 
 
             port = applink.get('@android:port')
             scheme = applink.get('@android:scheme')
             # Collect possible well-known paths
            if scheme and scheme in ('http', 'https') and host:
                host = host.replace('*.', '')
                if port:
                     c_url = f'{scheme}://{host}:{port}{well_known_path}'
                 else:
                     c_url = f'{scheme}://{host}{well_known_path}'