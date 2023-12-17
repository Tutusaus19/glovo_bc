# database_connection.py
# Import Psycopg2 to connect to the database and make queries
import psycopg2


# Create the function to connect to the database
def get_database_connection():
    # Create a try except to manage errors
    # Establish the parameters of the connection
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="glovo_database_BC",
            user="postgres",
            password="232425"
        )
        # Return the connection
        return conn
    # Manage exceptions: errors. If there is an error the function returns None
    except Exception as e:
        print(f"Something went wrong when connecting to the database :( : {e}")
        return None
