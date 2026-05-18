from app.llm.llm_initializer import initialize_llm
from app.retrieval.vectorstore import get_retriever_from_vectorstore, load_vectorstore
from app.routing.query_orchestrator import orchestrate_query


vector_db=load_vectorstore(r"data\vectorstores\faiss_index")
retriever=get_retriever_from_vectorstore(vector_db)

query_1="What are RBI KYC limits for small accounts?"
query_2="Who has the highest salary?"
query_3="What is maternity leave policy?"
query_4="Explain TechNova leave policy"
query_5="Average salary by department?"
query_6="Which employee took most leaves?"
query_7="Tell me about employee leave"
query_8="What is TechNova stock price?"


llm=initialize_llm()

result=orchestrate_query(query_1,llm,retriever)
result_2=orchestrate_query(query_2,llm,retriever)
result_3=orchestrate_query(query_3,llm,retriever)
result_4=orchestrate_query(query_4,llm,retriever)
result_5=orchestrate_query(query_5,llm,retriever)
result_6=orchestrate_query(query_6,llm,retriever)
result_7=orchestrate_query(query_7,llm,retriever)
result_8=orchestrate_query(query_8,llm,retriever)


print(f"Question: {query_1}")
print(f"Answer: {result}")
print(f"Question: {query_2}")
print(f"Answer: {result_2}")
print(f"Question: {query_3}")
print(f"Answer: {result_3}")
print(f"Question: {query_4}")
print(f"Answer: {result_4}")
print(f"Question: {query_5}")
print(f"Answer: {result_5}")
print(f"Question: {query_6}")
print(f"Answer: {result_6}")
print(f"Question: {query_7}")
print(f"Answer: {result_7}")
print(f"Question: {query_8}")
print(f"Answer: {result_8}")
