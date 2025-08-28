         """Azure client error messages."""
         scrubbed_message = ProviderErrors.AZURE_GENERAL_CLIENT_ERROR_MESSAGE
         if any(test in message for test in ["http error: 401", "Authentication failed", "(401) Unauthorized"]):
            scrubbed_message = ProviderErrors.AZURE_INCORRECT_CLIENT_SECRET_MESSAGE
         if "AADSTS700016" in message:
             scrubbed_message = ProviderErrors.AZURE_INCORRECT_CLIENT_ID_MESSAGE
         if "AADSTS90002" in message: