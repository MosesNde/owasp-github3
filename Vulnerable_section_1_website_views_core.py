     UserProfile,
     Wallet,
 )
from website.utils import analyze_pr_content, fetch_github_data, safe_redirect_allowed, save_analysis_report
 
 # from website.bot import conversation_chain, is_api_key_valid, load_vector_store
 
             messages.error(request, "Please provide a valid URL")
             return redirect("check_owasp_compliance")
 
         try:
             # Parse URL to determine if it's a GitHub repository
            is_github = "github.com" in url.lower()
            is_owasp_org = "github.com/owasp" in url.lower()
 
             # Fetch and analyze website content
            response = requests.get(url, timeout=10, verify=False)
             soup = BeautifulSoup(response.text.lower(), "html.parser")
             content = soup.get_text().lower()
 
                 recommendations.append("Check if the project has features behind a paywall")
 
             context = {
                "url": url,
                 "github_compliance": {
                     "github_hosted": is_github,
                     "under_owasp_org": is_owasp_org,