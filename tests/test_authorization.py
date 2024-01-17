from dadata_api_tests_framework.schemas.error_schema import ERROR_SCHEMA
import allure
from dadata_api_tests_framework.api.response import ApiResponse


@allure.title("Отсутствие доступа для юзера без токена")
@allure.tag("api_tests")
@allure.feature("metro_api")
@allure.suite("test_access_metro_method")
def test_authorization_error_metro(metro_api_unauthorized):
    with allure.step("Отправляем запрос неавторизованным юзером"):
        response = ApiResponse(metro_api_unauthorized.find_metro_station(query='Москва'))

    with allure.step("Проверяем ошибку доступа"):
        response.assert_status_code(401).validate(ERROR_SCHEMA)


@allure.title("Отсутствие доступа для юзера без токена")
@allure.tag("api_tests")
@allure.feature("currency_api")
@allure.suite("test_access_currency_method")
def test_authorization_error_currency(currency_api_unauthorized):
    with allure.step("Отправляем запрос неавторизованным юзером"):
        response = ApiResponse(currency_api_unauthorized.api_call(query="rub"))
    with allure.step("Проверяем ошибку доступа"):
        response.assert_status_code(401).validate(ERROR_SCHEMA)
