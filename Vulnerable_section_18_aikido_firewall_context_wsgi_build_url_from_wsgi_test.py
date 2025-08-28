     assert build_url_from_wsgi(request) == expected
 
 
 def test_build_url_from_wsgi_with_query_string():
     request = {
         "wsgi.url_scheme": "http",