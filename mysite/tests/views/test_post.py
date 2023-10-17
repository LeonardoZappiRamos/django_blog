import json, datetime
from django.urls import reverse
import pytest

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    
    now = datetime.datetime.now()
    html = "<html><body>Hello !! It %s now.</body></html>" % now
    
    assert response.status_code == 200