             {
                 "key": ProviderErrors.AZURE_CLIENT_ERROR,
                 "internal_message": ", AdalError: Get Token request returned http error: 401 and server response:",
                "expected_message": ProviderErrors.AZURE_INCORRECT_CLIENT_SECRET_MESSAGE,
             },
             {
                 "key": ProviderErrors.AZURE_CLIENT_ERROR,
                 "internal_message": "Authentication failed",
                "expected_message": ProviderErrors.AZURE_INCORRECT_CLIENT_SECRET_MESSAGE,
             },
             {
                 "key": ProviderErrors.AZURE_CLIENT_ERROR,
                 "internal_message": (
                     "(401) Unauthorized. Request ID: cca1a5a4-4107-4e7a-b3b4-b88f31e6a674\n"
                     "Code: 401\nMessage: Unauthorized. Request ID: cca1a5a4-4107-4e7a-b3b4-b88f31e6a674"
                 ),
                "expected_message": ProviderErrors.AZURE_INCORRECT_CLIENT_SECRET_MESSAGE,
             },
             {
                 "key": ProviderErrors.AZURE_CLIENT_ERROR,