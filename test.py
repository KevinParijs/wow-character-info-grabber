import requests

client_id = '8511945f6cbd402d9ece620e9cbfbb0b'
client_secret = 'Va3tC2lcWw7ydvb1b51ZAi834MXvP3RZ'

url = 'https://eu.battle.net/oauth/token'

# Prepare the data to be sent in the request body
data = {
    'grant_type': 'client_credentials'
}

# Include client ID and client secret in the request headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Include client ID and client secret in the request
auth = (client_id, client_secret)

# Make the request
response = requests.post(url, data=data, headers=headers, auth=auth)

# Check response status code
if response.status_code == 200:
    data = response.json()
    # Extract and print the access token
    access_token = data['access_token']
    print("Access Token:", access_token)
else:
    print("Error:", response.status_code)
