import pytest
import allure
from dadata_api_tests_framework.api.response import ApiResponse
from dadata_api_tests_framework.schemas.metro_schema import METRO_SCHEMA


@allure.title("Получение данных о закрытых станциях метро: {metro_query}")
@allure.tag("api_tests")
@allure.feature("metro_api")
@allure.suite("test_get_closed_stations")
@pytest.mark.parametrize("metro_query", ["чернышевская", "ладожская"])
def test_get_closed_stations(metro_query, metro_api):
    with allure.step("Получаем данные о станции метро"):
        response = ApiResponse(metro_api.find_metro_station(query=metro_query, city='Санкт-Петербург'))

    with allure.step("Проверяем, что станция метро закрыта"):
        assert response.response_json["suggestions"][0]["data"]["is_closed"] is True
        response.assert_status_code(200).validate(METRO_SCHEMA)
