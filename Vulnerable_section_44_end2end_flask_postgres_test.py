 import pytest
 import requests
 # e2e tests for flask_postgres sample app
 post_url_fw = "http://localhost:8090/create"
 post_url_nofw = "http://localhost:8091/create"
 
 def test_safe_response_with_firewall():
     dog_name = "Bobby Tables"
     res = requests.post(post_url_nofw, data={'dog_name': dog_name})
     assert res.status_code == 200
 