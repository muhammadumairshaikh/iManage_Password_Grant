import time
import requests
from app.config import (
    IMANAGE_HOSTNAME,
    CLIENT_ID,
    CLIENT_SECRET,
    SERVICE_USERNAME,
    SERVICE_PASSWORD,
)

TOKEN_URL = f"{IMANAGE_HOSTNAME}/auth/oauth2/token"

_token_cache = {
    "access_token": None,
    "refresh_token": None,
    "expires_at": 0,
}


def get_access_token() -> str:
    # Reuse token if still valid
    if _token_cache["access_token"] and not _is_expired():
        return _token_cache["access_token"]

    # Try refresh token
    if _token_cache["refresh_token"] and _refresh_token():
        return _token_cache["access_token"]

    # Otherwise login again
    _password_login()
    return _token_cache["access_token"]


def _password_login():
    payload = {
        "grant_type": "password",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": SERVICE_USERNAME,
        "password": SERVICE_PASSWORD,
    }

    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code != 200:
        raise RuntimeError(
            f"Password grant failed [{response.status_code}]: {response.text}"
        )

    _store_token(response.json())


def _refresh_token() -> bool:
    payload = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": _token_cache["refresh_token"],
    }

    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code != 200:
        return False

    _store_token(response.json())
    return True


def _store_token(data: dict):
    _token_cache["access_token"] = data["access_token"]
    _token_cache["refresh_token"] = data.get("refresh_token")
    _token_cache["expires_at"] = time.time() + int(data["expires_in"]) - 30


def _is_expired() -> bool:
    return time.time() >= _token_cache["expires_at"]
