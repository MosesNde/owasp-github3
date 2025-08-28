 from auth import get_current_user
 
 
 # TestClient is a wrapper around the FastAPI app that allows us to make requests to it
 client = TestClient(app)
 