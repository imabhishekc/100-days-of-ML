import requests

url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer token *********************"
}

response = requests.get(url, headers=headers)

print(response.json())