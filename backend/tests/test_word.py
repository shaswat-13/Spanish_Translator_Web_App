from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# tests if it returns a word of the day or not
def test_word_of_the_day():
    response = client.get("/word_of_the_day")
    assert response.status_code == 200
    data = response.json()
    assert "spanish" in data
    assert "english" in data


# tests if it correctly translates hola
def test_translate_word():
    response = client.get("/translate/hola")
    assert response.status_code == 200
    data = response.json()
    assert "spanish" in data
    assert "english" in data
    assert data["english"] == "hello!, hi!"


# tests if a random word is returned or not
def test_random_word():
    response = client.get("/random")
    assert response.status_code == 200
    data = response.json()
    assert "spanish" in data
    assert "english" in data
