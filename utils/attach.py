import json
import allure
import requests
from allure_commons.types import AttachmentType
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def api_request(base_url, endpoint, method, headers, **kwargs):
    url = f'{base_url}/{endpoint}'
    logger.info(f"Using headers in api_request: {headers}")
    logger.info(f"Request URL in api_request: {url}")
    logger.info(f"Request body in api_request: {kwargs.get('json')}")
    results = getattr(requests, method)(url, headers=headers, **kwargs)
    allure.attach(body=json.dumps(results.json(), indent=4, ensure_ascii=False), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")
    allure.attach(body=str(results.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=results.url, name="API URL", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(kwargs, indent=4, ensure_ascii=False), name="Request body",
                  attachment_type=AttachmentType.JSON, extension="json")

    logger.info("Request: " + results.request.url)
    if results.request.body:
        logger.info("INFO Request body: " + results.request.body.decode('utf-8'))
    logger.info("Request headers: " + str(results.request.headers))
    logger.info("Response code " + str(results.status_code))
    logger.info("Response: " + results.text)

    return results
