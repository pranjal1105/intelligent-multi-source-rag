from app.ingestion.pipelines.pdf_ingestion_pipeline import run_pdf_ingestion_pipeline


source={"path": r"data\raw\HDFC_Bank_Annual_Report_2024_25-310202.pdf"
        ,"type":"pdf"
        ,"source_name":"HDFC Bank Annual Report 2024-25"}

chunks=run_pdf_ingestion_pipeline(source)
print(f"Number of chunks generated: {len(chunks)}\n")
print("Top 5 chunks: \n")
for i,chunk in enumerate(chunks[:5]):
    print(f"Chunk {i+1}:")
    print(f"Content: {chunk.page_content}")
    print(f"Metadata: {chunk.metadata}")
    print("\n")

print("Test middle chunks: \n")
for i,chunk in enumerate(chunks[len(chunks)//2:len(chunks)//2+5]):
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