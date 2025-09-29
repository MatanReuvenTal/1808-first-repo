import requests
response = requests.get("https://www.python.org/")
if response.status_code == 200:
    print("python is up and running")