import re
import logging

logger=logging.getLogger(__name__)

def normalize_whitespaces(docs):
    try:
        logger.info("Cleaning whitespaces from doc")
        pattern=r'[ \t]+'
        for doc in docs:
            text=doc.page_content
            cleaned_text=re.sub(pattern," ",text,flags=re.MULTILINE)
            doc.page_content=cleaned_text
        return docs
        
    except Exception as e:
        logger.exception("Could not clean documents")
        raise e
    
def remove_rbi_footer(docs):

    try:

        logger.info("Removing footers from rbi circular")

        pattern = r"^.*(?:Amended|Inserted|Deleted)\s+vide\s+circular.*$"

        for doc in docs:

            text = doc.page_content

            cleaned_text = re.sub(
                pattern,
                "",
                text,
                flags=re.MULTILINE
            )

            doc.page_content = cleaned_text

        return docs

    except Exception as e:

        logger.exception("Could not remove footers")
        raise e
    
def fix_hyphenation(docs):
    try:
        logger.info("Fixing hyphenated words.")
        for doc in docs:
            text=doc.page_content
            cleaned_text=re.sub(r"(\w+)-\n(\w+)",r"\1\2",text)
            doc.page_content=cleaned_text
        return docs
    except Exception as e:

        logger.exception("Could not fix hyphens")
        raise e
    
def cleanup_newlines(docs):
    try:

        logger.info("Cleaning up new lines.")

        pattern = r'\n{3,}'

        for doc in docs:

            text = doc.page_content

            cleaned_text = re.sub(
                pattern,
                "\n\n",
                text
            )

            doc.page_content = cleaned_text

        return docs

    except Exception as e:

        logger.exception("Could not remove footers")
        raise e
            
def fix_merged_numeric_words(docs):
    try:
        logger.info("Cleaning up new lines.")
        for doc in docs:
            text=doc.page_content
            cleaned_text=re.sub(r"(\d+)([a-zA-Z]+)",r"\1 \2",text)
            doc.page_content=cleaned_text
        return docs
    except Exception as e:
        logger.exception("Could not remove merged numeric words")
        raise e