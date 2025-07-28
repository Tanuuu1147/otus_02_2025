import pytest
import requests

@pytest.fixture
def base_url():
    return "https://api.openbrewerydb.org/v1"

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Target URL"
    )
    parser.addoption(
        "--status_code",
    type=int,
    default=200,
    help="Expected HTTP status code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

def test_status_code_check(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code, \
        (f"Expected {status_code}, "
         f"got {response.status_code}")