 
 async def get_db_connection():
     return await asyncpg.connect(
        host="db",
         database="db",
         user="user",
         password="password"