 import os
 load_dotenv()
 
# Create a connection to the database
engine = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
 
 # Create a session
 Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
 
# Create a base class
 Base = declarative_base()
 
 
 # Create the tables in the database
 class Task(Base):
     __tablename__ = 'task'