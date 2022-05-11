from typing import List
import requests
from requests import Response
from config import BASE_API_URL
from constants import SWAPI_RESOURCE

"""This module contains utility functions that wrap calls to the Star Wars API"""
"""SWAPI provides a library https://github.com/phalt/swapi-python that can be used instead of this"""
"""This was created for testing purposes"""


def get_resource_count(resource: SWAPI_RESOURCE) -> int:
    """Get count field from specific swapi resource"""
    url = f"{BASE_API_URL}/{resource}"
    response_json = requests.get(url).json()
    return response_json.get("count")


def get_full_resource_results(resource: SWAPI_RESOURCE) -> List:
    """Get full results list from swapi resource"""
    url = f"{BASE_API_URL}/{resource}"
    response_json = requests.get(url).json()
    full_results: List = response_json.get("results")
    next_url = response_json.get("next")
    # fetch all pages
    while next_url is not None:
        response_json = requests.get(next_url).json()
        full_results.extend(response_json.get("results"))
        next_url = response_json.get("next")
    return full_results


def search_resource(resource: SWAPI_RESOURCE, search_term: str):
    """Get json response from using the resource search endpoint"""
    url = f"{BASE_API_URL}/{resource}/?search={search_term}"
    return requests.get(url).json()


def get_schema(resource: SWAPI_RESOURCE) -> Response:
    """Get JSON schema for a resource"""
    url = f"{BASE_API_URL}/{resource}/schema"
    return requests.get(url)
