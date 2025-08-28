         if not os.path.exists(os.path.dirname(file_local)):
             os.makedirs(os.path.dirname(file_local))
 
         url = urljoin(f'{source.base_url}/', resource)
         logger.debug('get url %s', url)
 