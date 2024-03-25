import pytest
from app import create_app

def test_create_app():
    app = create_app()
    assert app is not None

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

# def test_home_page(client):
#     rv = client.get('/')
#     assert rv.status_code == 200