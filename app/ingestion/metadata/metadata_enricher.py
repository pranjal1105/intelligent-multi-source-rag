from uuid import uuid4
from langchain_core.documents import Document


def enrich_pdf_metadata(chunks: list[Document], source: dict) -> list[Document]:
    """
    Enrich PDF chunks with standardized metadata.
    """

    enriched_chunks = []

    for index, chunk in enumerate(chunks):
        metadata = chunk.metadata.copy()

        metadata.update(
            {
                "chunk_id": str(uuid4()),
                "chunk_index": index,
                "document_type": "pdf",
                "source": source["path"],
                "source_name": source.get("source_name", ""),
                "chunk_size": len(chunk.page_content)
            }
        )

        chunk.metadata = metadata
        enriched_chunks.append(chunk)

    return enriched_chunks


def enrich_markdown_metadata(
    chunks: list[Document], source: dict
) -> list[Document]:
    """
    Enrich markdown chunks with standardized metadata.
    """

    enriched_chunks = []

    for index, chunk in enumerate(chunks):
        metadata = chunk.metadata.copy()

        metadata.update(
            {
                "chunk_id": str(uuid4()),
                "chunk_index": index,
                "document_type": "markdown",
                "source": source["path"],
                "source_name": source.get("source_name", ""),
                "chunk_size": len(chunk.page_content)
            }
        )

        chunk.metadata = metadata
        enriched_chunks.append(chunk)

    return enriched_chunks