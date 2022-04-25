import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def auth():
    api_key = os.getenv("PINATA_API_KEY")
    api_secret = os.getenv("PINATA_API_SECRET")
    jwt_token = os.getenv("PINATA_JWT_TOKEN")

    return (api_key, api_secret, jwt_token)
