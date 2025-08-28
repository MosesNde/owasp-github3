 import os
 
 basedir = os.path.abspath(os.path.dirname(__file__))
 
         os.environ.get("JWT_SECRET_KEY")
         or "ereteyubcgdhfjmazensherifahmedmostafaanas##$$%^djyfgjidigp0-ititjgj"
     )
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get("JWT_ACCESS_TOKEN_EXPIRES") or 3600