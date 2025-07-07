# Day 5: Working with JSON APIs (TMDb API) – 100 Days of Machine Learning

## Goal
Today, I explored how to fetch and handle JSON data from an external REST API using Python. Specifically, I used The Movie Database (TMDb) API to fetch data about popular people in film and worked with it using `requests` and `pandas`.

---

## Tools & Libraries Used
- Python
- [Requests](https://docs.python-requests.org/)
- [Pandas](https://pandas.pydata.org/)
- The Movie Database (TMDb) API

---

## Concepts Learned
- Making authenticated HTTP requests using bearer tokens
- Parsing JSON responses using `.json()`
- Extracting nested data from JSON
- Converting API response into a Pandas DataFrame for further analysis

---

## API Reference
- TMDb API endpoint used:
https://api.themoviedb.org/3/person/popular?language=en-US&page=1


- TMDb Official Docs: https://developer.themoviedb.org/reference/intro/getting-started

---

## Sample Code Snippet

```python
import requests
import pandas as pd

url = "https://api.themoviedb.org/3/person/popular?language=en-US&page=1"

headers = {
  "accept": "application/json",
  "Authorization": "Bearer <YOUR_ACCESS_TOKEN>"
}

response = requests.get(url, headers=headers)
data = response.json()
df = pd.DataFrame(data['results'])
df.head()
