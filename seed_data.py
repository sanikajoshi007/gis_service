import requests
import random
import time

API_URL = "http://localhost:8000/api/hazards/"
HAZARD_TYPES = ["pothole", "waterlogging", "missing_sign"]

print("Injecting 50 simulated hazards into Pune...")

for _ in range(50):
    # Generate random coordinates around Pune center
    lat = 18.5204 + random.uniform(-0.05, 0.05)
    lon = 73.8567 + random.uniform(-0.05, 0.05)
    
    payload = {
        "hazard_type": random.choice(HAZARD_TYPES),
        "confidence": round(random.uniform(0.65, 0.99), 2),
        "latitude": lat,
        "longitude": lon
    }
    requests.post(API_URL, json=payload)
    time.sleep(0.1)

print("Done! Refresh your dashboard.")