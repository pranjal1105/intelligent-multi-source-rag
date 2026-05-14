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
    
import re
import logging

logger = logging.getLogger(__name__)

def remove_table_of_contents(docs):

    try:

        logger.info("Removing table of contents.")

        # Detect TOC heading
        toc_heading_pattern = re.compile(
            r"(table\s+of\s+contents|contents)",
            re.IGNORECASE
        )

        # Detect TOC entry lines
        toc_entry_pattern = re.compile(
            r"""
            ^\s*
            (
                \d+[\.\)]?          # 1 or 1.
                |
                [A-Z]\.             # A.
                |
                Chapter\s+\d+       # Chapter 1
            )
            .*?
            (\.{2,}|\s{2,})        # dots or spacing
            \d+\s*$                # page number
            """,
            re.IGNORECASE | re.VERBOSE
        )

        for doc in docs:

            text = doc.page_content

            lines = text.splitlines()

            cleaned_lines = []

            inside_toc = False

            for line in lines:

                # Detect TOC start
                if toc_heading_pattern.search(line):
                    inside_toc = True
                    continue

                # Skip TOC entries
                if inside_toc:

                    if toc_entry_pattern.search(line):
                        continue

                    # Stop TOC removal when normal paragraph starts
                    if len(line.strip()) > 50 and not toc_entry_pattern.search(line):
                        inside_toc = False

                if not inside_toc:
                    cleaned_lines.append(line)

            doc.page_content = "\n".join(cleaned_lines)

        return docs

    except Exception as e:

        logger.exception("Could not remove table of contents")
        raise e