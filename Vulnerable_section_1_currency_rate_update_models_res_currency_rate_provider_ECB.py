 from collections import defaultdict
 from datetime import date, timedelta
 from urllib.request import urlopen
 
 from odoo import fields, models
 
 
         handler = EcbRatesHandler(currencies, date_from, date_to)
         with urlopen(url, timeout=10) as response:
            xml.sax.parse(response, handler)
         content = handler.content
         if invert_calculation:
             for k in content.keys():