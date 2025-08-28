     UserProfile,
     Wallet,
 )
from website.utils import is_valid_https_url, rebuild_safe_url
 
 logger = logging.getLogger(__name__)
 
         domain = None
         if email:
             domain = email.split("@")[-1]
            try:
                full_url_domain = "https://" + domain + "/favicon.ico"
                if is_valid_https_url(full_url_domain):
                    safe_url = rebuild_safe_url(full_url_domain)
                    response = requests.get(safe_url, timeout=5)
                    if response.status_code == 200:
                        exists = "exists"
            except:
                pass
         context = {
            "exists": exists,
             "domain": domain,
             "email": email,
         }