from langchain_community.vectorstores import FAISS
from app.retrieval.embeddings import load_embedding_model
import logging

logger = logging.getLogger(__name__)

def create_vectorstore(chunks):

    try:
        embedding_model = load_embedding_model()

        faiss_db = FAISS.from_documents(
            chunks,
            embedding_model
        )

        retriever = faiss_db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}
        )

        return faiss_db, retriever

    except Exception as e:
        logger.exception("Failed to create vector db")
        raise e