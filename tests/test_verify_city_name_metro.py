import allure
from dadata_api_tests_framework.schemas.metro_schema import METRO_SCHEMA
from dadata_api_tests_framework.api.response import ApiResponse


@allure.title("Валидация ответа api metro")
@allure.tag("api_tests")
@allure.feature("metro_api")
@allure.suite("test_validate_metro_api")
def test_verify_city_name(metro_api):
    with allure.step("Отправляем валидный запрсо"):
        response = ApiResponse(metro_api.find_metro_station(query='Москва'))
    with allure.step("Проверяем валидность ответа и статус код"):
        response.assert_status_code(200).validate(METRO_SCHEMA)
        city = [i["data"]["city"] for i in response.response_json["suggestions"]]

        expected_city = 'Москва'
        assert all(item == expected_city for item in city), (
            f"Ожидаемый город: {expected_city}, Фактический город: {city}"
        )
