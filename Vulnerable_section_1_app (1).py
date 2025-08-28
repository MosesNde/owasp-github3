 import cv  # Import the CV module
 import cover_letter  # Import the cover letter module
 
 @st.cache_data
 def load_data():
     return pd.read_csv("vgsales.csv")
 
 # Load dataset
 df = load_data()
 
# Set wide mode
st.set_page_config(layout="wide")

 # Streamlit Sidebar
 st.sidebar.title("📊 Video Game Sales Dashboard")
 page = st.sidebar.radio("Select Analysis", ["Dashboard",  "CV", "Cover Letter"])