 
 SSRF_DEFAULT_MAX_RETRIES = dify_config.SSRF_DEFAULT_MAX_RETRIES
 
proxy_mounts = (
    {
        "http://": httpx.HTTPTransport(proxy=dify_config.SSRF_PROXY_HTTP_URL),
        "https://": httpx.HTTPTransport(proxy=dify_config.SSRF_PROXY_HTTPS_URL),
    }
    if dify_config.SSRF_PROXY_HTTP_URL and dify_config.SSRF_PROXY_HTTPS_URL
    else None
)

 BACKOFF_FACTOR = 0.5
 STATUS_FORCELIST = [429, 500, 502, 503, 504]
 
             if dify_config.SSRF_PROXY_ALL_URL:
                 with httpx.Client(proxy=dify_config.SSRF_PROXY_ALL_URL) as client:
                     response = client.request(method=method, url=url, **kwargs)
            elif proxy_mounts:
                 with httpx.Client(mounts=proxy_mounts) as client:
                     response = client.request(method=method, url=url, **kwargs)
             else: