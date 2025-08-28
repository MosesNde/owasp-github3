                 "destination": create_url("https://hackers.com"),
             },
         ],
        create_url("https://hackers.com"),
     ) == create_url("https://example.com")
 
     assert get_redirect_origin(
                 "destination": create_url("https://hackers.com/test"),
             },
         ],
        create_url("https://hackers.com/test"),
     ) == create_url("https://example.com")
 
 
 def test_get_redirect_origin_no_redirects():
    assert get_redirect_origin([], create_url("https://hackers.com")) is None
    assert get_redirect_origin(None, create_url("https://hackers.com")) is None
 
 
 def test_get_redirect_origin_not_a_destination():
                     "destination": create_url("https://hackers.com"),
                 },
             ],
            create_url("https://example.com"),
         )
         is None
     )
                     "destination": create_url("https://hackers.com"),
                 },
             ],
            create_url("https://example.com"),
         )
         is None
     )
                 "destination": create_url("https://another.com"),
             },
         ],
        create_url("https://hackers.com/test"),
     ) == create_url("https://example.com")
 
 