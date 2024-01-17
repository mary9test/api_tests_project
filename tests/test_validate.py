import pytest
import allure
from dadata_api_tests_framework.schemas.currency_schema import CURRENCY_SCHEMA
from dadata_api_tests_framework.schemas.metro_schema import METRO_SCHEMA
from dadata_api_tests_framework.api.response import ApiResponse


@allure.title("Валидация ответа api metro")
@allure.tag("api_tests")
@allure.feature("metro_api")
@allure.suite("test_validate_metro_api")
def test_validate(metro_api):
    with allure.step("Отправляем валидный запрсо"):
        response = ApiResponse(metro_api.find_metro_station(query='Москва'))
    with allure.step("Проверяем валидность ответа и статус код"):
        response.assert_status_code(200).validate(METRO_SCHEMA)


@allure.title("Валидация ответа api currency")
@allure.tag("api_tests")
@allure.feature("currency_api")
@allure.suite("test_validate_metro_api")
@pytest.mark.parametrize("currency", ["rub", "usd", "eur"])
def test_validation(currency_api, currency):
    with allure.step("Отправляем запрос"):
        response = ApiResponse(currency_api.api_call(query=currency))
    with allure.step("Проверяем статус-код и валидацию полей"):
        response.assert_status_code(200).validate(CURRENCY_SCHEMA)
