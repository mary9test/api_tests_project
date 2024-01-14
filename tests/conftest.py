import pytest
from api.metro_api import MetroAPI
from api.currency_api import CurrencyAPI
from dotenv import load_dotenv
import os


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def metro_api():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/metro"
    api_token = os.getenv('API_TOKEN')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_token}'
    }

    return MetroAPI(base_url=base_url, headers=headers)


@pytest.fixture
def metro_api_unauthorized():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/metro"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    return MetroAPI(base_url=base_url, headers=headers)


@pytest.fixture
def currency_api():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/currency"
    api_token = os.getenv('API_TOKEN')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_token}'
    }

    return CurrencyAPI(base_url=base_url, headers=headers)


@pytest.fixture
def currency_api_unauthorized():
    base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/currency"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    return CurrencyAPI(base_url=base_url, headers=headers)
