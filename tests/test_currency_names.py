import allure
import pytest
from dadata_api_tests_framework.api.response import ApiResponse
from dadata_api_tests_framework.schemas.currency_schema import CURRENCY_SCHEMA


@allure.title("Проверка названия валюты")
@allure.tag("api_tests")
@allure.feature("currency_api")
@allure.suite("test_currency_names")
@pytest.mark.parametrize("currency, expected_name",
                         [("rub", "Российский рубль"), ("CHF", "Швейцарский франк"), ("eur", "Евро")])
def test_get_currency_name(currency_api, currency, expected_name):
    with allure.step("Отправляем запрос"):
        response = ApiResponse(currency_api.api_call(query=currency))
    with allure.step("Проверяем название валюты"):
        assert response.response_json["suggestions"][0]["data"]["name"] == expected_name
        response.assert_status_code(200).validate(CURRENCY_SCHEMA)
