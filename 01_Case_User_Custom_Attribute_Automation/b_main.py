# main.py
from b_data_retrieval import get_user_data
from b_braze_interaction import update_user_profile_in_braze
from b_database_connection import get_database_connection
def main():
    print("Starting the process...")

    # Obtaining the database connection
    conn = get_database_connection()
    if conn is not None:
        print("Connected to the database successfully.")

        # Create a cursor and retrieve user data:
        cursor = conn.cursor()
        print("Retrieving user data...")
        users = get_user_data(cursor)

        # If users found, update them:
        if users:
            print(f"Updating profiles for {len(users)} users in Braze...")
            update_user_profile_in_braze(users)
        else:
            print("No user data to update.")

        # Create the cursor and the connection:
        cursor.close()
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to connect to the database.")


if __name__ == "__main__":
    main()
