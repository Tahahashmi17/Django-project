import requests

url = 'http://127.0.0.1:8000/api/login/'
data = {
    'username': 'edward',
    'password': 'edward@123'
}
response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
