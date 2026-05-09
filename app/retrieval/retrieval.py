import logging

logger=logging.getLogger(__name__)

def get_retrieved_chunks(query, retriever):
    try:
        retrieved_chunks=retriever.invoke(query)
        return retrieved_chunks
    except Exception as e:
        logger.exception("Failed to retrieve relevant chunks")