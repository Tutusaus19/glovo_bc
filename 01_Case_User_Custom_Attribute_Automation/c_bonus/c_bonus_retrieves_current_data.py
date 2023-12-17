import requests


def get_current_data_from_braze(api_key, user_id):
    """Retrieve the current data for a user from Braze."""
    api_url = "https://rest.iad-01.braze.com/users/data"
    headers = {
        "Authorization": f"Bearer {api_key}", # We don´t know de apiKey from Braze, so here it should be change.
        "Content-Type": "application/json"
    }
    params = {
        "user_id": user_id  # Identifying user in Braze.
    }
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  # Returns data in JSON format.
    else:
        print(f"Error retrieving data for user {user_id}: {response.text}")
        return None
