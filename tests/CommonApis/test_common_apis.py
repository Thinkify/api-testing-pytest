
import requests
import pytest
import json

from resources import config
from tests.support.assertions import assert_valid_schema


@pytest.mark.common
def test_get_cities():
    get_cities_request = config.BASEURL + config.CitiesResource + config.BengaluruCityQuery
    cities_response = requests.get(get_cities_request, headers={'Content-Type': 'application/json',
                                                                'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert cities_response.status_code == 200, 'status code is not equal to 200'
    cities_response_json = json.loads(cities_response.content)
    assert_valid_schema(cities_response_json, 'CitiesResponseSchema.json')


@pytest.mark.common
def test_get_categories():
    get_categories_request = config.BASEURL + config.CategoriesResource
    categories_response = requests.get(get_categories_request, headers={'Content-Type': 'application/json',
                                                                        'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert categories_response.status_code == 200, 'status code is not equal to 200'
    categories_response_json = json.loads(categories_response.content)
    assert_valid_schema(categories_response_json, 'CategoriesResponseSchema.json')


@pytest.mark.common
def test_get_collections():
    get_collections_request = config.BASEURL + config.CollectionsResource + config.BengaluruCityIdQuery
    collections_response = requests.get(get_collections_request,
                                        headers={'Content-Type': 'application/json',
                                                 'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert collections_response.status_code == 200, 'status code is not equal to 200'
    collections_response_json = json.loads(collections_response.content)
    assert_valid_schema(collections_response_json, 'CollectionsResponseSchema.json')


@pytest.mark.common
def test_get_establishments():
    get_establishments_request = config.BASEURL + config.EstablishmentsResource + config.BengaluruCityIdQuery
    establishments_response = requests.get(get_establishments_request,
                                           headers={'Content-Type': 'application/json',
                                                    'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert establishments_response.status_code == 200, 'status code is not equal to 200'
    establishments_response_json = json.loads(establishments_response.content)
    assert_valid_schema(establishments_response_json, 'EstablishmentsResponseSchema.json')


@pytest.mark.common
def test_get_cuisines():
    get_cuisines_request = config.BASEURL + config.CuisinesResource + config.BengaluruCityIdQuery
    cuisines_response = requests.get(get_cuisines_request, headers={'Content-Type': 'application/json',
                                                                    'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert cuisines_response.status_code == 200, 'status code is not equal to 200'
    cuisines_response_json = json.loads(cuisines_response.content)
    assert_valid_schema(cuisines_response_json, 'CuisinesResponseSchema.json')





