import pytest
from app.main import app
import json

@pytest.fixture
def test_app():
    return app

@pytest.mark.asyncio
async def test_health_check(test_app):
    test_client = test_app.test_client()
    response = await test_client.get('/health')
    assert response.status_code == 200
    data = await response.get_json()
    assert data['status'] == 'healthy'

@pytest.mark.asyncio
async def test_chat_endpoint_no_message(test_app):
    test_client = test_app.test_client()
    response = await test_client.post('/chat', json={})
    assert response.status_code == 400
    data = await response.get_json()
    assert 'error' in data

@pytest.mark.asyncio
async def test_chat_endpoint_with_message(test_app):
    test_client = test_app.test_client()
    test_message = {'message': 'Hello, how are you?'}
    response = await test_client.post('/chat', json=test_message)
    assert response.status_code == 200
    data = await response.get_json()
    assert 'response' in data
    assert 'status' in data
    assert data['status'] == 'success' 