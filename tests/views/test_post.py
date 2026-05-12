import pytest

from django.urls import reverse

from blog.factories import PostFactory


@pytest.mark.django_db
def test_post_view(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Backend Python - EBAC" in response.content
    assert b"Welcome to my awesome Blog" in response.content


@pytest.mark.django_db
def test_post_detail_view(client):
    post = PostFactory(title="Detail page title", slug="detail-page-title")
    response = client.get(reverse("post_detail", kwargs={"slug": post.slug}))
    assert response.status_code == 200
    assert b"Detail page title" in response.content