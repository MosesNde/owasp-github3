 import re
 import requests
 from urllib.parse import urlparse
 from bs4 import BeautifulSoup
 
     except:
         return False
 
def sanitize_for_prompt(text):
    """Sanitize text to be safely included in an AI prompt."""
    if not text:
        return ""
    
    # Strip any control characters
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)
    
    # Handle potential prompt injection markers
    text = re.sub(r'\[(?:SYSTEM|USER|ASSISTANT|INSTRUCTION|SEARCH|WEBSITE|END).*?\]', 
                  lambda m: '\\' + m.group(0), text, flags=re.IGNORECASE)
    
    return text

def duckduckgo_check(domain):
    import requests
    from bs4 import BeautifulSoup

     Check if the URL is safe to access:
     - Must be HTTP or HTTPS
     - Must not point to private IP ranges, localhost, or internal network resources
         try:
             resolved_ip = socket.gethostbyname(hostname)
             ip_obj = ipaddress.ip_address(resolved_ip)
     # Remove <think>...</think> block if it exists
     return re.sub(r"<think>.*?</think>\s*", "", response_text, flags=re.DOTALL).strip()
 
     if not is_valid_url(url):
         return {"error": "Malformed or invalid URL"}
     
     parsed = urlparse(url)
     domain = parsed.netloc or parsed.path  # fallback if scheme is missing
     
     # --- Step 1: DuckDuckGo keyword check ---
     duck_result = duckduckgo_check(safe_domain)
     search_summary = ""
    if duck_result["is_suspicious"]:
         search_summary = (
             f"\nSearch engine results indicate the domain may be suspicious. "
def duckduckgo_check(domain):
         )
 
     # --- Step 2: Fetch website content ---
 Based on the information above, provide your assessment of the website.
 """
 
    payload = {
        "model": "deepseek-r1:latest",
        "prompt": prompt,
        "stream": False
    # Validate URL is safe to access
    if not is_url_safe(url):
        return "[Error: Cannot access internal or private network resources]"
    
        response.raise_for_status()
        raw_text = response.json().get("response", "")
        return {"summary": extract_summary(raw_text)}
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return f"[Error fetching website: {e}]"

def extract_summary(response_text):
    # Remove <think>...</think> block if it exists
    return re.sub(r"<think>.*?</think>\s*", "", response_text, flags=re.DOTALL).strip()

def generate_response(url):
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path  # fallback if scheme is missing

    # --- Step 1: DuckDuckGo keyword check ---
    duck_result = duckduckgo_check(domain)
    search_summary = ""
    if duck_result["is_suspicious"]:
        search_summary = (
            f"\nSearch engine results indicate the domain may be suspicious. "
            f"Found keywords: {', '.join(duck_result['matched_keywords'])}.\n"
        )

    # --- Step 2: Fetch website content ---
    website_text = fetch_website_text(url)

    # --- Step 3: Create prompt for Ollama ---
    prompt = f"""
You are a cybersecurity AI assistant helping users evaluate the safety and legitimacy of websites.

A user has asked you to analyze this domain: {url}

Your tasks are:
1. Analyze the domain name structure and determine if it appears to impersonate a legitimate organization (e.g., government agency, company, university, or service).
2. Judge if the domain name uses typosquatting, brand impersonation, or misleading patterns to appear trustworthy.
3. Determine from online search results and website content whether the site is linked to known scams or phishing behavior.
4. Say whether it appears to be from an official or trustworthy source — or is pretending to be.
5. Summarize all findings clearly in a short paragraph, including why the site is or is not trustworthy.

Search engine findings:
{search_summary or "No clear scam indicators were found in web search."}

Website content:
----
{website_text[:4000]}
----

Give your assessment now.
"""


     payload = {
         "model": "deepseek-r1:latest",
         "prompt": prompt,
         "stream": False
     }
 
     try:
         response = requests.post(OLLAMA_URL, json=payload)
         response.raise_for_status()
         raw_text = response.json().get("response", "")