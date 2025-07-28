import pytest
import requests

#
@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_user_by_id(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data



# удаление поста 22
def test_delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/22"

    response = requests.delete(url)
    assert response.status_code == 200


# cоздание поста с разными данными
@pytest.mark.parametrize("title, body, user_id", [
    ("Hello", "I am from russia", 101),
    ("Good buy", "I am here", 102),
])
def test_create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == title
    assert data["body"] == body
    assert data["userId"] == user_id
    assert "id" in data



# обновление
def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "id": 1,
        "title": "New Title",
        "body": "New body",
        "userId": 1
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200  # Успешное обновление
    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "New Title"
    assert data["body"] == "New body"
    assert data["userId"] == 1


# обновление только титла
def test_patch_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "title": "Updated only Title"
    }

    response = requests.patch(url, json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated only Title"
