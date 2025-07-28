import pytest
import requests


# список всех породы
def test_get_all_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "akita" in data["message"]

# рандомное изображение собак
def test_get_random_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https://")

# одно рандомные изображения по породе
@pytest.mark.parametrize("breed", ["spaniel", "retriever", "pug"])
def test_random_image_by_breed(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "https://" in data["message"]


#  изображения sub-breed
@pytest.mark.parametrize("breed, sub_breed", [
    ("bulldog", "english"),
    ("bulldog", "boston"),
    ("bulldog", "french"),
])
def test_images_by_sub_breed(breed, sub_breed):
    url = (f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images")
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)





# рандомное изображение под-породы afghan
def test_random_image_from_sub_breed():
    url = "https://dog.ceo/api/breed/hound/afghan/images/random"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "success"










