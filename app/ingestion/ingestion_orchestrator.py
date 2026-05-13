from app.ingestion.pipelines.pdf_ingestion_pipeline import run_pdf_ingestion_pipeline
from app.ingestion.pipelines.markdown_ingestion_pipeline import run_markdown_ingestion_pipeline
import logging

logging.basicConfig(level=logging.INFO)

logger=logging.getLogger(__name__)


def detect_document_type(source):
    """
    Detects the document type based on the file extension.
    """
    logger.info(f"Detecting document type for source: {source['path']}")
    doc_type=source["type"]

    if doc_type=="pdf":
        logger.info(f"Detected document type: pdf")
        return "pdf"
    elif doc_type=="markdown":
        logger.info(f"Detected document type: markdown")
        return "markdown"
    else:
        logger.error(f"Unsupported document type: {doc_type}")
        raise ValueError(f"Unsupported document type: {doc_type}")
    
def run_ingestion_pipeline(source):
    """
    Runs the appropriate ingestion pipeline based on the document type.
    """
    doc_type=detect_document_type(source)

    if doc_type=="pdf":
        logger.info(f"Running PDF ingestion pipeline for source: {source['path']}")
        return run_pdf_ingestion_pipeline(source)
    elif doc_type=="markdown":
        logger.info(f"Running Markdown ingestion pipeline for source: {source['path']}")
        return run_markdown_ingestion_pipeline(source)