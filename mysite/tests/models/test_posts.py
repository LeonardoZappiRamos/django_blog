import pytest

from blog.factories import PostFactory

@pytest.fixture
def post_creation():
    return PostFactory(title='Post creates by Pytest')

@pytest.mark.django_db
def test_create_post(post_creation):
    assert post_creation.title == 'Post creates by Pytest'
    