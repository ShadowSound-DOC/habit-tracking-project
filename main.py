"""Pixela habit tracker — log coding hours as graph pixels."""
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["PIXELA_TOKEN"]
USERNAME = os.environ["PIXELA_USERNAME"]
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID", "graph1")

pixela_endpoint = "https://pixe.la/v1/users"
headers = {"X-USER-TOKEN": TOKEN}

# One-time setup helpers (uncomment if you need to recreate user/graph):
# requests.post(pixela_endpoint, json={
#     "token": TOKEN, "username": USERNAME,
#     "agreeTermsOfService": "yes", "notMinor": "yes",
# })
# requests.post(f"{pixela_endpoint}/{USERNAME}/graphs", json={
#     "id": GRAPH_ID, "name": "Coding graph", "unit": "hour",
#     "type": "float", "color": "ajisai",
# }, headers=headers)

today = datetime.now()
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
