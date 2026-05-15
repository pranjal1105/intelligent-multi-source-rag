import logging
import psycopg2
from app.config.settings import postgres_host, postgres_port, postgres_db, postgres_user, postgres_password

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

def connect_to_db():
    try:
        logger.info("Attempting to connect to PostgreSQL database")
        connection = psycopg2.connect(
            host=postgres_host,
            port=postgres_port,
            database=postgres_db,
            user=postgres_user,
            password=postgres_password
        )
        logger.info("Successfully connected to PostgreSQL database")
        return connection
    except Exception as e:
        logger.exception("Failed to connect to PostgreSQL database")
        raise e