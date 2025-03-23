import requests
import random

tenor_key = "AIzaSyAJl8nWNLfxskvo4McCyWy1ixoJwiUw4do"
tenor_url = "https://tenor.googleapis.com/v2/search"

def get_gif(search_term):
    params = {
        "key": tenor_key,
        "q": search_term,
        "limit": 10,  
    }
    
    response = requests.get(tenor_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "results" in data and data["results"]:
            gif = random.choice(data["results"])
            return gif["media_formats"]["gif"]["url"]  
    
    return None

print(get_gif("crazy bench press"))
