import pytest
from dadata_api_tests_framework.api.response import ApiResponse
from dadata_api_tests_framework.schemas.metro_schema import METRO_SCHEMA
import allure


@allure.title("Поиск станции метро на ветке: {metro_query}")
@allure.tag("api_tests")
@allure.feature("metro_api")
@allure.suite("test_find_metro_station")
@pytest.mark.parametrize("metro_query", ["выборгская", "площадь ленина", "девяткино"])
def test_find_metro_station(metro_query, metro_api):
    with allure.step("Получаем данные о станции метро"):
        results = metro_api.find_metro_station(query=metro_query, city='Санкт-Петербург')

    with allure.step("Проверяем, что станции метро находятся на Кировско-Выборгской ветке"):
        response_handler = ApiResponse(results)
        line_name = response_handler.response_json["suggestions"][0]["data"]["line_name"]
        expected_line_name = 'Кировско-Выборгская'
        assert line_name == expected_line_name, (
            f"Ожидаемая ветка: {expected_line_name}, Фактическая ветка: {line_name}"
        )
        response_handler.assert_status_code(200).validate(METRO_SCHEMA)
