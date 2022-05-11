import pytest
import requests
from requests import Response
from config import BASE_API_URL
from constants import SWAPI_RESOURCE
from swapi import get_full_resource_results, get_resource_count, search_resource

"""Contains tests that validate the Star Wars API"""

# Build resource list to into parameterized test
resource_list = [resource.value for resource in SWAPI_RESOURCE]


def test_can_connect_to_api():
    """Validate we are able to connect to api"""
    response: Response = requests.get(BASE_API_URL)
    assert response.status_code == 200


# Using a parameterized approach here to validate the same thing except across multiple endpoints
# This increase code resuse also makes it easy to add an additional resource in the SWAPI_RESOURCE class when needed
@pytest.mark.parametrize("resource", resource_list)
def test_resource_count(resource: SWAPI_RESOURCE):
    """Validate the provided count is equal to the actual number of results provided"""
    provided_count = get_resource_count(resource)
    full_results = get_full_resource_results(resource)
    assert provided_count == len(full_results)


def test_people_search():
    """Validates that the search term is contained in the results"""
    search_term = "r2"
    json_response = search_resource(SWAPI_RESOURCE.PEOPLE.value, search_term)
    results = json_response.get("results")
    for result in results:
        assert search_term in result.get("name").lower()
