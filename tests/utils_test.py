import pytest
import json
from utils import *


def test_get_posts_all():
    assert type(get_posts_all()) == list, 'Файл не того типа'


def test_get_comments_all():
    file = open('./data/comments.json')
    file = json.load(file)
    assert file == get_comments_all(), 'Не удалось открыть файл с комментариями'


def test_get_bookmarks_all():
    file = open('./data/bookmarks.json')
    file = json.load(file)
    assert file == get_bookmarks_all(), 'Не удалось открыть файл с закладками'


def test_get_posts_by_user():
    with pytest.raises(ValueError):
        get_posts_by_user('nwl')


def test_get_comments_by_post_id():
    with pytest.raises(ValueError):
        get_comments_by_post_id('123456')
