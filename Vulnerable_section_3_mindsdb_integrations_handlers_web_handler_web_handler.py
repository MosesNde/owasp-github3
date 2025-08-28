     HandlerResponse as Response,
     RESPONSE_TYPE
 )
 
 from .urlcrawl_helpers import get_df_from_query_str, get_all_websites
 
                         urls = url
                 else:
                     raise NotImplementedError(
                        f'url can be url = "someurl", you can also crawl multiple sites, as follows: url IN ("url1", "url2", ..)')
 
             else:
                 pass
 
         if limit < 0:
             limit = 0
            
         result = get_all_websites(urls, limit, html=False)
         if len(result) > limit:
             result = result[:limit]