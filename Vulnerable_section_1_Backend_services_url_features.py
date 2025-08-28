 from bs4 import BeautifulSoup
 from urllib.parse import urlparse
 from datetime import datetime
 
 FEATURE_NAMES = [
     "having_IP_Address", "URL_Length", "Shortening_Service", "having_At_Symbol",
     "Links_pointing_to_page", "Statistical_report"
 ]
 
# Blocklist for potentially malicious domains
DOMAIN_BLOCKLIST = [
    'example-malicious-domain.com',
    'evil-domain.com',
    # Add more as needed
]

# Maximum number of external requests allowed per function call
MAX_EXTERNAL_REQUESTS = 5

 def is_url_safe(url):
     """
    Validate if a URL is safe to process.
    Returns (is_safe, reason) tuple.
     """
    # Check if URL is valid
     if not url or not isinstance(url, str):
         return False, "URL must be a non-empty string"
         
     # 2. URL Length
     features.append(1 if len(url) >= 75 else 0 if len(url) >= 54 else -1)
 
    # 3. Shortening service
    features.append(1 if re.search(r"(bit\.ly|goo\.gl|tinyurl|ow\.ly|t\.co)", url) else -1)

    # 4. '@' symbol
    features.append(1 if "@" in url else -1)
 
    # 5. Double slash redirect
    features.append(1 if url.rfind('//') > 6 else -1)
 
    # 6. Prefix/Suffix (hyphen)
    features.append(1 if '-' in domain else -1)
 
     # 7. Subdomain
     subdomain_count = domain.count('.')
         features.append(-1)
             total = 0
             external = 0
             for tag in soup.find_all(['img', 'script'], src=True):
                total += 1
                if domain not in tag['src']:
                    external += 1
            ratio = external / total if total else 0
            features.append(1 if ratio > 0.61 else 0 if 0.22 < ratio <= 0.61 else -1)
        else:
            features.append(1)  # Default to suspicious if no soup
    except:
         features.append(-1)
 
    # 14. Anchor tags pointing elsewhere
     try:
         if soup:
             anchors = soup.find_all('a', href=True)
            total = len(anchors)
            unsafe = sum(1 for a in anchors if "#" in a['href'] or "javascript" in a['href'].lower())
            ratio = unsafe / total if total else 0
            features.append(1 if ratio > 0.67 else 0 if 0.31 < ratio <= 0.67 else -1)
        else:
            features.append(1)  # Default to suspicious if no soup
     except:
         features.append(-1)
 
    # 15. Meta/script/link tags external
     try:
        if soup:
            tags = soup.find_all(['meta', 'script', 'link'])
            total = len(tags)
             unsafe = sum(1 for tag in tags if domain not in str(tag))
             ratio = unsafe / total if total else 0
             features.append(1 if ratio > 0.81 else 0 if 0.17 < ratio <= 0.81 else -1)
         features.append(-1)
 
     # 16. SFH (server form handler)
    try:
        if soup:
            forms = soup.find_all('form')
            for f in forms:
                if f.get('action') in ["", "about:blank"]:
                     features.append(1)
                     break
                 elif domain not in f.get('action', ''):