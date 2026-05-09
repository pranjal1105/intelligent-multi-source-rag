from app.ingestion.markdown_loader import markdown_loader
from app.ingestion.chunking import recursive_chunking
from app.retrieval.vectorstore import create_vectorstore
from app.retrieval.retrieval import get_retrieved_chunks
docs=markdown_loader(r"data\raw\TechNova_HR_Policy_Document.md")
print(docs[0].metadata)
chunks=recursive_chunking(docs)
print(chunks[0].page_content)
print(f"\n\nTotal chunks: {len(chunks)}")
# embeddings=create_hugging_face_embeddings(chunks)
# print(f"Dimension of embeddings: {len(embeddings[0])}")
# print(f"First 6 embeddings of first chunk : {embeddings[0][:6]}")

vector_db, retriever= create_vectorstore(chunks)

retrieved_chunk=get_retrieved_chunks("What is the maternity leave policy in the company?",retriever)

for i,doc in enumerate(retrieved_chunk):
    print(f"Chunk {i}: {doc.page_content}")

