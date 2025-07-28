import pytest
import requests


# список пивоварен из города Сан-Диего -лимит 3
def test_get_breweries_by_city_with_limit(base_url):
    url = f"{base_url}/breweries?by_city=san_diego&per_page=3"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 3

    for brewery in data:
        assert "san diego" in brewery["city"].lower()

# одна случайная пивоварня
def test_get_random_brewery(base_url):
    url = f"{base_url}/breweries/random"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1

    brewery = data[0]
    assert "name" in brewery
    assert "city" in brewery
    assert "state" in brewery
    assert "brewery_type" in brewery

# поиск по имени - часть
@pytest.mark.parametrize("query", ["dog", "cooper", "blue"])
def test_search_brewery_by_name(base_url, query):
    url = f"{base_url}/breweries/search?query={query}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# кол-во пивоварен в ЮК
@pytest.mark.parametrize("state, expected_count", [
    ("Busan", 9),
    ("Seoul", 14),
    ("Jejudo", 3)
])
def test_breweries_count_by_state(base_url, state, expected_count):
    url = f"{base_url}/breweries/meta?by_country=south_korea"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert "by_state" in data
    assert data["by_state"][state] == expected_count


# проверка ключевых полей
def test_get_brewery_by_id(base_url):
    brewery_id = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    url = f"{base_url}/breweries/{brewery_id}"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == brewery_id
    assert "name" in data
    assert "city" in data
    assert "state" in data
    assert "brewery_type" in data


