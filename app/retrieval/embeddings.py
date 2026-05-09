from langchain_huggingface import HuggingFaceEmbeddings
import logging

logger=logging.getLogger(__name__)
def load_embedding_model():
    try:
        embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        # texts=[chunk.page_content for chunk in chunks]
        # embeddings=embedding_model.embed_documents(texts)
        # return embeddings
        return embedding_model
    except Exception as e:
        logger.exception(f"Failed to create embedding")
