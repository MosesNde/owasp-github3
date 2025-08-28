     
     # Database settings
     # Development settings (Docker/SQL Server)
    DEV_SQL_SERVER: str = os.getenv("DEV_SQL_SERVER", "20.243.151.161")
     DEV_SQL_PORT: str = os.getenv("DEV_SQL_PORT", "1433")
     DEV_SQL_DB: str = os.getenv("DEV_SQL_DB", "FujiSmileV")
     DEV_SQL_USER: str = os.getenv("DEV_SQL_USER", "test_user")
     DEV_SQL_PASSWORD: str = os.getenv("DEV_SQL_PASSWORD", "ZQfgwV7axZPd")
     
     # Production settings (Remote server)
    PROD_SQL_SERVER: str = os.getenv("PROD_SQL_SERVER", "20.243.151.161")
     PROD_SQL_PORT: str = os.getenv("PROD_SQL_PORT", "1433")
     PROD_SQL_DB: str = os.getenv("PROD_SQL_DB", "FujiSmileV")
     PROD_SQL_USER: str = os.getenv("PROD_SQL_USER", "test_user")