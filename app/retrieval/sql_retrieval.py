from app.database.postgres_connection import connect_to_db
import logging

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

def execute_sql_query(query):
    try:
        logger.info(f"Connecting to database to execute query: {query}")
        conn=connect_to_db()
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        raise e
    cursor=conn.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()    
    return result
