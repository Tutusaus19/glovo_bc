# This script updates user data in Braze.
import requests

def update_data_in_braze(api_key, user_id, data):
    """Update the user data in Braze."""
    # Here we have to replace with the actual Braze API endpoint and request structure from Glovo platform
    api_url = "https://rest.iad-01.braze.com/users/track"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"user_id": user_id, "data": data}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.status_code
