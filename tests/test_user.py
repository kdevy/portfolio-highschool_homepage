import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from werkzeug.security import check_password_hash
from app import create_app
from app.models import db
from app.models.user_model import User
from app.services.user_service import UserService

@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    with app.test_client() as client:
        yield client

def test_create_user(app):
    with app.app_context():
        UserService.register({"username": "testuser01", "password": "testpass"})

        u = User.query.filter_by(username="testuser01").first()
        assert u is not None
        assert u.username == "testuser01"
        assert check_password_hash(u.password, "testpass")

def test_register_view(client):
    response = client.get('/user/register')
    assert response.status_code == 200
    assert b'Register' in response.data

    response = client.post('/user/register', data={'username': 'testuser02', 'password': 'testpass'})
    assert response.status_code == 201
    assert b'Registered' in response.data

    response = client.post('/user/register', data={'username': '', 'password': ''})
    assert response.status_code == 400
    assert b'Username and password are required' in response.data

def test_login_view(client):
    response = client.get('/user/login')
    assert response.status_code == 200
    assert b'Login' in response.data

    UserService.register({"username": "testuser03", "password": "testpass"})

    response = client.post('/user/login', data={'username': 'testuser03', 'password': 'testpass'})
    assert response.status_code == 200
    assert b'Logged in' in response.data

    response = client.post('/user/login', data={'username': '', 'password': ''})
    assert response.status_code == 400
    assert b'Invalid credentials' in response.data