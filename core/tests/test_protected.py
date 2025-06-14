import requests

token = '9f7f1c4813977ee868c5d9dad377a9d56fdcedce'
url = 'http://127.0.0.1:8000/api/protected/'
headers = {
    'Authorization': f'Token {token}'
}
response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.json())
