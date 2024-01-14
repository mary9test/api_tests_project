import allure
import pytest
from api.response import Response


@allure.title("Проверка названия валюты")
@allure.tag("api_tests")
@allure.feature("currency_api")
@allure.suite("test_find_metro_station")
@pytest.mark.parametrize("currency, expected_name",
                         [("rub", "Российский рубль"), ("CHF", "Швейцарский франк"), ("eur", "Евро")])
def test_get_currency_name(currency_api, currency, expected_name):
    with allure.step("Отправляем запрос"):
        response = Response(currency_api.api_call(query=currency))
    with allure.step("Проверяем название валюты"):
        assert response.response_json["suggestions"][0]["data"]["name"] == expected_name


