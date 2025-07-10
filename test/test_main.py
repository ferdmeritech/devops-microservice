import pytest
from fastapi.testclient import TestClient
from app.main import app
import jwt
import uuid
import datetime

client = TestClient(app)

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
JWT_SECRET = "tu_secreto_muy_seguro"

def generate_valid_jwt():
    payload = {
        "jti": str(uuid.uuid4()),
        "iat": datetime.datetime.now(datetime.timezone.utc),
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=60)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

def test_successful_post():
    jwt_token = generate_valid_jwt()
    response = client.post(
        "/DevOps",
        headers={
            "X-Parse-REST-API-Key": API_KEY,
            "X-JWT-KWY": jwt_token
        },
        json={
            "message": "This is a test",
            "to": "Juan Perez",
            "from": "Rita Asturia",
            "timeToLifeSec": 45
        }
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Hello Juan Perez your message will be send"

def test_invalid_api_key():
    jwt_token = generate_valid_jwt()
    response = client.post(
        "/DevOps",
        headers={
            "X-Parse-REST-API-Key": "invalid-key",
            "X-JWT-KWY": jwt_token
        },
        json={
            "message": "This is a test",
            "to": "Juan Perez",
            "from": "Rita Asturia",
            "timeToLifeSec": 45
        }
    )