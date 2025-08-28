 from bson import ObjectId
 from urllib.parse import urlparse
 import os
 
 rental_bp = Blueprint('rentals', __name__)
 
     
     allowed_domains = ["mybookrental.s3.amazonaws.com"]
     parsed_url = urlparse(pdf_url)
     
    if parsed_url.netloc not in allowed_domains:
        return jsonify({'error': 'Domain not allowed'}), 400
     
     response = requests.get(pdf_url)
     #response = requests.get(parsed_url.geturl())
     if response.status_code != 200:
         return jsonify({'error': 'Failed to fetch PDF'}), 500
 