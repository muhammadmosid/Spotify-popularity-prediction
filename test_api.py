import requests

URL = "http://127.0.0.1:8000/predict"
base = {"danceability": 0.75, "energy": 0.80, "loudness": -5.0, "valence": 0.60,
        "tempo": 120.0, "acousticness": 0.10, "speechiness": 0.05, "genre": "k-pop"}

for genre in ["k-pop", "metal", "jazz", "iranian", "not-a-real-genre", "K-Pop"]:
    r = requests.post(URL, json={**base, "genre": genre})
    print(f"{genre:18} {r.status_code}  {r.json()}")

# validation checks
bad = {k: v for k, v in base.items() if k != "genre"}
print("missing genre ->", requests.post(URL, json=bad).status_code)
print("bad tempo     ->", requests.post(URL, json={**base, "tempo": "fast"}).status_code)