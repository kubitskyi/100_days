import requests
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
CRAPH_ID = os.getenv("CRAPH_ID")

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config ={
    "id": CRAPH_ID,
    "name": "Runing graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers={
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{CRAPH_ID}"
pixela_data = {
    "date": "20241029",
    "quantity": "1.24",
}
response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
print(response.text)