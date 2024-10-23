import pytest
from main import app

@pytest.fixture
def client():
    # Setting up the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_load(client):
    """Test if the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Medicine Search' in response.data

def test_search_existing_medicine(client):
    """Test searching for an existing medicine (Aspirin)."""
    response = client.post('/', data={'medicine_name': 'Aspirin'})
    assert response.status_code == 200
    assert b'Aspirin is a widely used over-the-counter medication' in response.data
    assert b'Price: $4.99' in response.data
    assert b'Add to Cart' in response.data

def test_search_non_existing_medicine(client):
    """Test searching for a non-existing medicine (NonExistent)."""
    response = client.post('/', data={'medicine_name': 'NonExistent'})
    assert response.status_code == 200
    assert b'Aspirin is a widely used over-the-counter medication' not in response.data
    assert b'Ibuprofen is a nonsteroidal anti-inflammatory drug' not in response.data
    assert b'Paracetamol is used to treat mild to moderate pain' not in response.data

def test_add_to_cart_message(client):
    """Test that the 'Added to cart!' message appears after clicking 'Add to Cart'."""
    response = client.post('/', data={'medicine_name': 'Aspirin'})
    assert response.status_code == 200
    assert b'Add to Cart' in response.data
