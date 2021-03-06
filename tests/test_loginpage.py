import pytest
from mygame.models import User
import conftest
from mygame import app

#tests that the login page loads correctly
#and that Username and Password fields show up

def test_get_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

@pytest.fixture
def client():
  client = app.test_client()
  return client
