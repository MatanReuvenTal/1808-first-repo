import requests
response = requests.get("https://api.github.com/users/MatanReuvenTal/repos")
print(response.status_code)
print(response.text)
result =response.json()
for repo in result:
    print(repo["name"])