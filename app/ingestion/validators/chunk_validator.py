from langchain_core.documents import Document
import logging

logger = logging.getLogger(__name__)


MIN_CHUNK_LENGTH = 20
MAX_CHUNK_LENGTH = 5000


def validate_chunks(chunks: list[Document]) -> list[Document]:
    """
    Validate chunks before embedding/indexing.
    """

    valid_chunks = []

    for chunk in chunks:
        content = chunk.page_content.strip()

        # Empty chunk check
        if not content:
            logger.warning("Empty chunk detected. Skipping chunk.")
            continue

        # Tiny chunk check
        if len(content) < MIN_CHUNK_LENGTH:
            logger.warning(
                f"Tiny chunk detected ({len(content)} chars). Skipping chunk."
            )
            continue

        # Giant chunk check
        if len(content) > MAX_CHUNK_LENGTH:
            logger.warning(
                f"Oversized chunk detected ({len(content)} chars)."
            )

        # Metadata validation
        required_metadata = ["chunk_id", "document_type", "source"]

        missing_fields = [
            field
            for field in required_metadata
            if field not in chunk.metadata
        ]

        if missing_fields:
            logger.warning(
                f"Chunk missing metadata fields: {missing_fields}"
            )
            continue

        valid_chunks.append(chunk)

    logger.info(f"Validated {len(valid_chunks)} chunks successfully.")

    return valid_chunks