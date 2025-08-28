 from dotenv import load_dotenv
 import os
 load_dotenv()
 firewall_disabled = os.getenv("FIREWALL_DISABLED")
 if firewall_disabled is not None:
     cursor.close()
     conn.close()
     return f'Dog {dog_name} created successfully'