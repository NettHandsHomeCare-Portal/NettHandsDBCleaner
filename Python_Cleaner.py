#!/usr/bin/python3

import psycopg
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        
        with psycopg.connect(**params) as conn:

    # Open a cursor to perform database operations
            with conn.cursor() as cur:

        # Execute a command: this creates a new table
                cur.execute("""
                    DELETE FROM requests_requests  
                    WHERE to_timestamp(time) > NOW() - INTERVAL "30 days";
                    """)

        # display the PostgreSQL database server version
       
	# close the communication with the PostgreSQL
    except (Exception, psycopg .DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
