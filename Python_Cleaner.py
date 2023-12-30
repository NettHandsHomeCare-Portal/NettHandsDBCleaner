#!/usr/bin/python3

import psycopg2 as psycopg
from dotenv import load_dotenv
import os'
import queries
load_dotenv()


def clean_up():
    query = """
                    DELETE FROM requests_requests  
                    WHERE to_timestamp(time) > NOW() - INTERVAL "30 days";
                    """
    if queries.query(query, os.getenv("CONNECTION_STRING")):
        return "Cleaned Old Request Data"
    else:
        raise RuntimeError("Unabled to Clean!")

# def connect():
    # """ Connect to the PostgreSQL database server """
    # conn = None
    # try:
    #     # read connection parameters
        
    #     with psycopg.connect(conninfo=os.getenv("CONNECTION_STRING")) as conn:

    # # Open a cursor to perform database operations
    #         with conn.cursor() as cur:

    #     # Execute a command: this creates a new table
    #             print("Clearing Old Requests...")
    #             cur.execute("""
    #                 DELETE FROM requests_requests  
    #                 WHERE to_timestamp(time) > NOW() - INTERVAL "30 days";
    #                 """)

    #     # display the PostgreSQL database server version
       
	# # close the communication with the PostgreSQL
    # except (Exception, psycopg .DatabaseError) as error:
    #     print(error)
    # finally:
    #     if conn is not None:
    #         conn.commit()
    #         print('Database connection closed.')


if __name__ == '__main__':
    # connect()
    clean_up()
