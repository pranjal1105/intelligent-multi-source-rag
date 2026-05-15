import os 
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
postgres_host=os.getenv("POSTGRES_HOST")
postgres_port=os.getenv("POSTGRES_PORT")
postgres_db=os.getenv("POSTGRES_DB")
postgres_user=os.getenv("POSTGRES_USER")
postgres_password=os.getenv("POSTGRES_PASSWORD")




MARKDOWN_CHUNK_SIZE=400
MARKDOWN_CHUNK_OVERLAP=50

PDF_CHUNK_SIZE=1000
PDF_CHUNK_OVERLAP=100