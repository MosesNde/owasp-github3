     if not url:
         return jsonify({"error": "URL is required"}), 400
     
    # Validate the URL
    from urllib.parse import urlparse
     
    def is_valid_url(url):
        """Validate the URL to prevent SSRF attacks."""
        allowed_domains = {"example.com", "api.example.com"}
         parsed_url = urlparse(url)
         
        # Ensure the scheme is http or https
         if parsed_url.scheme not in {"http", "https"}:
            return False
        
        # Ensure the hostname is in the allowed domains
        if parsed_url.hostname not in allowed_domains:
            return False
        
        return True
    
    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400
    allowed_domains = ["example.com", "api.example.com"]
    
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ["http", "https"]:
            return jsonify({"error": "Invalid URL scheme"}), 400
         
        # Check hostname directly against allowed domains without DNS resolution
         hostname = parsed_url.hostname
         if not hostname:
             return jsonify({"error": "Invalid URL: missing hostname"}), 400
             
        # Strict domain validation with exact matching
        if hostname not in allowed_domains and not any(hostname.endswith('.' + domain) for domain in allowed_domains):
             return jsonify({"error": "URL domain is not allowed"}), 400
        
        # Reject IP addresses in URL
        import re
        ip_pattern = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
        if ip_pattern.match(hostname):
            return jsonify({"error": "IP addresses not allowed in URL"}), 400
             
     except Exception as e:
         return jsonify({"error": f"Invalid URL: {str(e)}"}), 400
         # Store original socket.create_connection function
         original_create_connection = socket.create_connection
         
        # Override socket connection creation to prevent SSRF
         def patched_create_connection(address, *args, **kwargs):
             host, port = address
            if host not in allowed_domains and not any(host.endswith('.' + domain) for domain in allowed_domains):
                 raise ValueError(f"Connection to {host} is not allowed")
             return original_create_connection(address, *args, **kwargs)
         
         # Apply patch