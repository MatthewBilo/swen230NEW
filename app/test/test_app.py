import pytest
# import app
import sys
from os.path import dirname as d
from os.path import abspath, join
from unittest.mock import MagicMock
from flask import Flask
from util import fileStorage
from util.fileStorage import register_user
from util.fileStorage import check_credentials
from util.fileStorage import update_password
from util.fileStorage import clear_user

import server
from server import app
from util import Cipher


root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
cp = Cipher.Cipher()


@pytest.fixture
def client():
    # Mock the Flask app client
    app = Flask(__name__, template_folder='/swen230new/app/templates', static_folder='/swen230new/app/static', static_url_path='')
    with app.test_client() as client:
        yield client

def test_register(client, monkeypatch):
    # Mock the request object
    mock_request = MagicMock()
    mock_request.method = 'POST'
    mock_request.form = {
        'username': 'test_user',
        'password': 'test_password',
        'passkey': 'test_passkey'
    }
    # Patching request to return the mock_request
    monkeypatch.setattr('flask.request', mock_request)

    # Mock the register_user function
    mock_register_user = MagicMock()
    monkeypatch.setattr('util.fileStorage.register_user', mock_register_user)

    # Call the register function
    response = client.post('/register')

    # Assertions
    assert response.status_code == 302  # Redirect status code
    assert response.location == 'http://localhost/login'  # Redirect to login page

    # Check if register_user was called with the correct arguments
    mock_register_user.assert_called_once_with('test_user', 'test_password', 'test_passkey')
