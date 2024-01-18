import pytest
import allure
from dadata_api_tests_framework.schemas.currency_schema import CURRENCY_SCHEMA
from dadata_api_tests_framework.api.response import ApiResponse


@allure.title("Названия стран для валют")
@allure.tag("api_tests")
@allure.feature("currency_api")
@allure.suite("test_verify_currency_country")
@pytest.mark.parametrize("currency, expected_country", [("rub", "Россия"), ("ars", "Аргентина"), ("jpy", "Япония")])
def test_verify_currency_country(currency_api, expected_country, currency):
    with allure.step("Отправляем запрос"):
        response = ApiResponse(currency_api.api_call(query=currency))
    with allure.step("Проверяем статус-код и валидацию полей"):
        response.assert_status_code(200).validate(CURRENCY_SCHEMA)
        assert response.response_json["suggestions"][0]["data"]["country"] == expected_country
