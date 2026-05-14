from langchain_community.vectorstores import FAISS
from app.retrieval.embeddings import load_embedding_model
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_vectorstore(chunks):

    try:
        logger.info("Loading embedding model")
        embedding_model = load_embedding_model()
        
        logger.info("Creating vector db from chunks")
        faiss_db = FAISS.from_documents(
            chunks,
            embedding_model
        )

        # retriever = faiss_db.as_retriever(
        #     search_type="similarity",
        #     search_kwargs={"k": 5}
        # )

        logger.info("Vector db created successfully")   
        return faiss_db

    except Exception as e:
        logger.exception("Failed to create vector db")
        raise e

def add_to_vectorstore(vectorstore, new_chunks):
    try:
        logger.info(f"Adding {len(new_chunks)} new chunks to vector db")
        vectorstore.add_documents(new_chunks)
        logger.info("Successfully added new chunks to vector db")
    except Exception as e:
        logger.exception("Failed to add new chunks to vector db")
        raise e
    
def get_retriever_from_vectorstore(vectorstore):
    try:
        logger.info("Creating retriever from vector db")
        retriever = vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 7}
        )
        logger.info("Retriever created successfully")
        return retriever
    except Exception as e:
        logger.exception("Failed to create retriever from vector db")
        raise e
    
def debug_retrieval(vectorstore, query):
    try:
        docs_with_scores = vectorstore.similarity_search_with_score(
    query,
    k=5)
        for doc, score in docs_with_scores:
            print(f"Score: {score}")
            print(f"Document content: {doc.page_content}")
            print(f"Document metadata: {doc.metadata}")
            print("------")    
    except Exception as e:
        logger.exception("Failed to debug retrieval")
        raise e