 
 from .models import Item, Price
 from .forms import ItemPriceGraphForm, BulkTrackForm, SignUpForm
 
 # Create your views here.
 
 @login_required
 def track_price(request):
     if request.method == "POST":
        url = request.POST.get("url")
         item_name = request.POST.get(
             "item_name"
         )  # Optional: if you want to get item name from the form
             if name_element:
                 item_name = name_element.text.strip()
             else:
                 return render(
                     request,
                    "error.html",
                     {"message": "Failed to extract item name from the webpage."},
                 )
         if len(item_name) > 500:
             return render(
                 request,
                "error.html",
                 {"message": "Item name exceeds the maximum length of 500 characters."},
             )
         # Extracting price and currency information
         price_meta = soup.find("meta", itemprop="price")
             if len(item_name) > 500:
                 return render(
                     request,
                    "error.html",
                     {
                         "message": "Item name exceeds the maximum length of 500 characters."
                     },
         else:
             return render(
                 request,
                "error.html",
                 {"message": "Failed to extract price or currency from the webpage."},
             )
 
     page_obj = paginator.get_page(page_number)
 
     return render(request, "app/list_items.html", {"page_obj": page_obj})