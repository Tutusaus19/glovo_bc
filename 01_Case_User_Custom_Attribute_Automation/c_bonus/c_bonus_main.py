# Main script to coordinate the data update process.
from c_bonus_retrieves_new_data import get_new_data
from c_bonus_retrieves_current_data  import get_current_data_from_braze
from c_bonus_data_compare import compare_and_update_data
from c_bonus_update_data import update_data_in_braze


def main():
    # Define the Braze API key and other necessary parameters
    api_key = "api_key_Braze" # Here is important to include de Api Key connection from Braze Glovo platform.

    # Connect to the database to retrieve new data
    conn = get_new_data()
    cursor = conn.cursor()

    # Retrieve new data from the PostgreSQL database
    new_data = get_new_data(cursor)

    # Assuming new_data is a dictionary with user_id as key
    for user_id, data in new_data.items():
        # Retrieve the current data from Braze for each user
        current_data = get_current_data_from_braze(api_key, user_id)

        # Compare current data with new data and update in Braze if necessary
        compare_and_update_data(api_key, user_id, current_data, data)

    # Close the database connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
