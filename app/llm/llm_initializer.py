import logging
from langchain_openai import ChatOpenAI
from app.config.settings import api_key
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_llm():
    # Placeholder for LLM initialization logic
    try:
        logger.info("Initializing LLM...")
        llm=ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)
        logger.info("LLM initialized successfully.")
        return llm
    except Exception as e:
        logger.error(f"Error initializing LLM: {e}")
        raise