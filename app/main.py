from fastapi import FastAPI
import requests

from app.oauth_imanage import get_access_token
from app.config import IMANAGE_HOSTNAME, CUSTOMER_ID, LIBRARY_ID

app = FastAPI(title="iManage Integration")


@app.get("/imanage/token")
def fetch_token():
    token = get_access_token()
    return {"access_token": token}


@app.get("/imanage/test")
def test_imanage():
    token = get_access_token()

    url = f"{IMANAGE_HOSTNAME}/api/v2/customers/{CUSTOMER_ID}/libraries/{LIBRARY_ID}"
    headers = {"X-Auth-Token": token}

    response = requests.get(url, headers=headers)
    return response.json()
