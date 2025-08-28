 from django.test import RequestFactory
 
 from .models import Item, Price
from .utils.utils import collect_products, track_price
 
 
 @shared_task
 
     for item in items:
         # Scraping the webpage
        response = requests.get(item.item_url, timeout=10)
         soup = BeautifulSoup(response.content, "html.parser")
 
         # Extracting price and currency information