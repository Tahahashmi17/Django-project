import requests

url = 'http://127.0.0.1:8000/api/register/'
data = {
    "username": "abcde123",
    "email": "abcde123@example.com",
    "password": "QWERTY@123"
}
response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
