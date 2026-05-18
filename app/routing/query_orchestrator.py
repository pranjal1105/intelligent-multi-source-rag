from app.generation.response_generator import generate_response
from app.generation.sql_generator import generate_sql_query
from app.generation.sql_response_generator import generate_sql_response
from app.llm.llm_initializer import initialize_llm
from app.retrieval.retrieval import get_retrieved_chunks
from app.retrieval.sql_retrieval import execute_sql_query
from app.routing.query_router import route_query
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def orchestrate_query(question,llm,retriever):
    route=route_query(question)
    logger.info(f"Query routed to: {route} for the question: {question}")
    if route=="sql":
        sql_query=generate_sql_query(llm,question)
        result=execute_sql_query(sql_query)
        response=generate_sql_response(question,sql_query, result ,llm, retriever)
        return response
    elif route=="vector":
        retrieved_chunks=get_retrieved_chunks(question,retriever)
        if len(retrieved_chunks)==0:
            return "I couldn't find relevant information."
        response=generate_response(llm,question,retrieved_chunks)
        return response
    