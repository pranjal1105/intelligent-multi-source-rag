from app.ingestion.ingestion_orchestrator import run_ingestion_pipeline


source={"path":r"data\raw\TechNova_HR_Policy_Document.md"
        ,"type":"markdown"
        ,"source_name":"TechNova HR Policy Document"}

chunks=run_ingestion_pipeline(source)
print(f"Number of chunks generated: {len(chunks)}\n")
print("Top 5 chunks: \n")
for i,chunk in enumerate(chunks[:5]):
    print(f"Chunk {i+1}:")
    print(f"Content: {chunk.page_content}")
    print(f"Metadata: {chunk.metadata}")
    print("\n")
print("Test middle chunks: \n")

for i,chunk in enumerate(chunks[len(chunks)//2:len(chunks)//2 +5]):
    print(f"Chunk {i+1}:")
    print(f"Content: {chunk.page_content}")
    print(f"Metadata: {chunk.metadata}")
    print("\n")

print("Test last 5 chunks: \n")
for i,chunk in enumerate(chunks[-5:]):  
    print(f"Chunk {len(chunks)-5+i+1}:")
    print(f"Content: {chunk.page_content}")
    print(f"Metadata: {chunk.metadata}")
    print("\n")

