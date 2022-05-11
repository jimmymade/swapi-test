import pytest
import requests
from requests import Response
from config import BASE_API_URL
from constants import SWAPI_RESOURCE
from swapi import get_full_resource_results, get_resource_count


def test_can_connect_to_api():
    """Validate we are able to connect to api"""
    response: Response = requests.get(BASE_API_URL)
    assert response.status_code == 200


# Build resource list to into parameterized test
resource_list = [resource.value for resource in SWAPI_RESOURCE]
@pytest.mark.parametrize("resource", resource_list)
def test_resource_count(resource: SWAPI_RESOURCE):
    """Validate the provided count is equal to the actual number of results provided"""
    provided_count = get_resource_count(resource)
    full_results = get_full_resource_results(resource)
    assert provided_count == len(full_results)
