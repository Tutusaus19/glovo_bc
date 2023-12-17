# braze_interaction.py
# Import request and json:  HTTP requests and to manage JSON data
import requests
import json
# Function to update user data. It receives user data as an argument:
def update_user_profile_in_braze(user_data):
    # endpoint url:
    url = "https://rest.iad-01.braze.com/users/track"
    # headers: We have to add the API Key of the Braze platform
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_REST_API_KEY"
    }

    for user in user_data:
        user_id, last_store_id_1, last_store_id_2, last_store_id_3 = user
        payload = {
            "attributes": [
                {
                    "external_id": str(user_id),
                    "last_3_store_ids": [last_store_id_1, last_store_id_2, last_store_id_3]
                }
            ]
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 201:
            print(f"Updated user profile: {user_id}")
        else:
            print(f"Error updating user {user_id}: {response.text}")