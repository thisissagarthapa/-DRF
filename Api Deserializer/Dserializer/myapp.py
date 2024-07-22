import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'name': 'sagar',
    'age': 22,
    'email': 'kingstonboysagar@gmail.com'
}

# Serialize data to JSON
json_data = json.dumps(data)

# Send POST request with JSON data
r = requests.post(url=URL, json=data)

# Check response status
print(f"Response status code: {r.status_code}")

# Check content-type header
content_type = r.headers.get('content-type', '')

# Print response data based on content-type
if 'application/json' in content_type:
    try:
        response_data = r.json()
        print("Response JSON data:")
        print(response_data)
    except json.JSONDecodeError:
        print("Invalid JSON format in response.")
else:
    print(f"Response content-type: {content_type}")
    print("Response body:")
    print(r.text)
