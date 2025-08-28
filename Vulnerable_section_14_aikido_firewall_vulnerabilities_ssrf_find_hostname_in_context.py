 
 def find_hostname_in_context(hostname, context, port):
     """Tries to locate the given hostname from context"""
 
     # Punycode detected in hostname, while user input may not be in Punycode
     # We need to convert it to ensure we compare the right values