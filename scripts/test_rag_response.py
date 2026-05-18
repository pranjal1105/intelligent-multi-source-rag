
from app.generation.response_generator import generate_response
from app.llm.llm_initializer import initialize_llm
from app.retrieval.retrieval import get_retrieved_chunks
from app.retrieval.vectorstore import get_retriever_from_vectorstore, load_vectorstore


faiss_db=load_vectorstore(r"data\vectorstores\faiss_index")
retriever=get_retriever_from_vectorstore(faiss_db)
query="What are the maternity leave rules at TechNova?"
query2="What is TechNova's stock price?"
query3="What are the four key elements that a KYC policy of Regulated Entities (REs) must include according to the RBI KYC Directions?"
query4="What are the transaction and balance limits applicable to a ‘Small Account’ under RBI KYC guidelines?"
query5="What is the RBI-prescribed minimum CIBIL score required for approving a personal loan?"
retrieved_chunks=get_retrieved_chunks(query, retriever)
retrieved_chunks2=get_retrieved_chunks(query2, retriever)
retrieved_chunks3=get_retrieved_chunks(query3, retriever)
retrieved_chunks4=get_retrieved_chunks(query4, retriever)
retrieved_chunks5=get_retrieved_chunks(query5, retriever)
llm=initialize_llm()

response=generate_response(llm, query, retrieved_chunks)
response2=generate_response(llm, query2, retrieved_chunks2)
response3=generate_response(llm, query3, retrieved_chunks3)
response4=generate_response(llm, query4, retrieved_chunks4)
response5=generate_response(llm, query5, retrieved_chunks5)


print("Question:", query)
print("Answer:", response)
print("Question:", query2)
print("Answer:", response2)
print("Question:", query3)
print("Answer:", response3)
print("Question:", query4)
print("Answer:", response4)
print("Question:", query5)
print("Answer:", response5)