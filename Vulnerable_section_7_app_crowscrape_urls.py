     path("accounts/", include("django.contrib.auth.urls")),
     path("", include("app.urls")),
 ]