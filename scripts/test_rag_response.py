
from app.generation.response_generator import generate_response
from app.llm.llm_initializer import initialize_llm
from app.retrieval.retrieval import get_retrieved_chunks
from app.retrieval.vectorstore import get_retriever_from_vectorstore, load_vectorstore


faiss_db=load_vectorstore(r"data\vectorstores\faiss_index")
retriever=get_retriever_from_vectorstore(faiss_db)
query="What are the maternity leave rules at TechNova?"

retrieved_chunks=get_retrieved_chunks(query, retriever)

llm=initialize_llm()

response=generate_response(llm, query, retrieved_chunks)

print("Question:", query)
print("Answer:", response)