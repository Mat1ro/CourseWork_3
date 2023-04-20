import pytest
from app import app


def test_api_posts():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list
    assert response.json[0].get('pk') == 1


def test_api_posts_postid():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict
    assert response.json.get('pk') == 1