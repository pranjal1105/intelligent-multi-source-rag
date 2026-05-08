from app.ingestion.markdown_loader import markdown_loader
from app.ingestion.chunking import recursive_chunking
docs=markdown_loader(r"data\raw\TechNova_HR_Policy_Document.md")
print(docs[0].metadata)
chunks=recursive_chunking(docs)
print(chunks[0].page_content)