from app.ingestion.chunking.pdf_chunker import recursive_pdf_chunker
from app.ingestion.loaders.pdf_loader import pdf_loader
from app.ingestion.metadata.metadata_enricher import enrich_pdf_metadata
from app.ingestion.validators.chunk_validator import validate_chunks
from app.ingestion.preprocessing.preprocessing import cleanup_newlines,fix_hyphenation,fix_merged_numeric_words,normalize_whitespaces,remove_rbi_footer
import logging

logging.basicConfig
logger=logging.getLogger(__name__)

def run_pdf_ingestion_pipeline(source):
    logger.info(f"Starting PDF ingestion pipeline for {source['path']}")
    file=source["path"]

    logger.info(f"Loading PDF file: {file}")
    docs=pdf_loader(file)
    logger.info(f"Loaded {len(docs)} documents from PDF file: {file}")
    
    logger.info(f"Preprocessing PDF documents from file: {file}")
    cleaned_docs=cleanup_newlines(docs)
    cleaned_docs=fix_hyphenation(cleaned_docs)
    cleaned_docs=fix_merged_numeric_words(cleaned_docs)
    cleaned_docs=normalize_whitespaces(cleaned_docs)
    cleaned_docs=remove_rbi_footer(cleaned_docs)
    logger.info(f"Preprocessed PDF documents from file: {file}")
    
    logger.info(f"Chunking PDF documents from file: {file}")
    chunks=recursive_pdf_chunker(cleaned_docs)
    logger.info(f"Generated {len(chunks)} chunks from PDF file: {file}")
    
    logger.info(f"Enriching metadata for PDF chunks from file: {file}")
    enriched_chunks=enrich_pdf_metadata(chunks,source)
    logger.info(f"Enriched metadata for {len(enriched_chunks)} PDF chunks from file: {file}")
    
    logger.info(f"Validating PDF chunks from file: {file}")
    validated_chunks=validate_chunks(enriched_chunks)
    logger.info(f"Validated {len(validated_chunks)} PDF chunks from file: {file}")
    
    logger.info(f"Finished PDF ingestion pipeline for {source['path']}")
    return validated_chunks