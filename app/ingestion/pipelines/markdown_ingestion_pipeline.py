import logging

from app.ingestion.chunking.markdown_chunker import recursive_markdown_chunker
from app.ingestion.loaders.markdown_loader import markdown_loader
from app.ingestion.metadata.metadata_enricher import enrich_markdown_metadata
from app.ingestion.preprocessing.preprocessing import remove_table_of_contents
from app.ingestion.validators.chunk_validator import validate_chunks

logger=logging.getLogger(__name__)

def run_markdown_ingestion_pipeline(source):
    source_path=source["path"]
    logger.info(f"Starting markdown ingestion pipeline for {source_path}")
    docs=markdown_loader(source_path)
    logger.info(f"Loaded {len(docs)} documents from {source_path}")
    #remove table of contents
    docs=remove_table_of_contents(docs) 
    logger.info(f"Chunking documents from {source_path}")
    chunks=recursive_markdown_chunker(docs)
    logger.info(f"Generated {len(chunks)} chunks from {source_path}")
    logger.info(f"Enriching metadata for chunks from {source_path}")
    enriched_chunks=enrich_markdown_metadata(chunks,source)
    logger.info(f"Enriched metadata for {len(enriched_chunks)} chunks from {source_path}")
    logger.info(f"Validating chunks from {source_path}")
    validated_chunks=validate_chunks(enriched_chunks)
    logger.info(f"Validated {len(validated_chunks)} chunks from {source_path}")
    return validated_chunks