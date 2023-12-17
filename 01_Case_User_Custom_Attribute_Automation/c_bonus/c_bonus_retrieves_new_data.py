import psycopg2

def get_new_data(cursor):
    """Retrieve new data from the PostgreSQL database."""
    try:
        # Establish the connection to your PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="glovo_database_BC",
            user="postgres",
            password="232425"
        )
        cursor = conn.cursor()

        # SQL to get users data:
        query = "SELECT * FROM user_data"

        # Execute the query
        cursor.execute(query)

        # Retrieve the results
        new_data = cursor.fetchall()

        # Closes the cursor and the connection
        cursor.close()
        conn.close()

        return new_data
    except psycopg2.DatabaseError as e:
        print(f"Error connecting to the database: {e}")
        return None
