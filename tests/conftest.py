import pytest
from dadata_api_tests_framework.api.metro_api import MetroApi
from dadata_api_tests_framework.api.currency_api import CurrencyApi
from dotenv import load_dotenv
import os


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def metro_api():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs"
    api_token = os.getenv('API_TOKEN')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_token}'
    }

    return MetroApi(base_url=base_url, headers=headers)


@pytest.fixture
def metro_api_unauthorized():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    return MetroApi(base_url=base_url, headers=headers)


@pytest.fixture
def currency_api():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs"
    api_token = os.getenv('API_TOKEN')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_token}'
    }

    return CurrencyApi(base_url=base_url, headers=headers)


@pytest.fixture
def currency_api_unauthorized():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    return CurrencyApi(base_url=base_url, headers=headers)
