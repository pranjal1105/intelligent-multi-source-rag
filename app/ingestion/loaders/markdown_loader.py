from langchain_community.document_loaders import UnstructuredMarkdownLoader
import logging

logger = logging.getLogger(__name__)

def markdown_loader(file):
    """
    Loads markdown file and returns LangChain documents.
    """

    try:
        logger.info(f"Loading file: {file}")

        loader = UnstructuredMarkdownLoader(file)

        docs = loader.load()

        logger.info(f"Successfully loaded {len(docs)} documents")

        return docs

    except Exception as e:
        logger.exception(f"Failed to load file: {file}")

        raise RuntimeError(f"Markdown loading failed for {file}") from e