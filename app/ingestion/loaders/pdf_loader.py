from langchain_community.document_loaders import PyPDFLoader
import logging

logger=logging.getLogger(__name__)

def pdf_loader(file):
    try:
        logger.info(f"Loading pdf file {file}")
        loader=PyPDFLoader(file)
        docs=loader.load()
        logger.info(f"Successfully loaded {len(docs)} documents")
        return docs
    except Exception as e:
        logger.exception(f"Failed to load {file}")
        raise e
    