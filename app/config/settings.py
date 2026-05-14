import os 
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

MARKDOWN_CHUNK_SIZE=400
MARKDOWN_CHUNK_OVERLAP=50

PDF_CHUNK_SIZE=1000
PDF_CHUNK_OVERLAP=100