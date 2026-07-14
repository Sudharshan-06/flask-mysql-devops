import sys
import os

sys.path.append(os.path.abspath("app"))

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200