import requests
from resources import config
import pytest


@pytest.mark.common
def test_get_cities():
    get_cities_request = config.BASEURL + config.CitiesResource + config.BengaluruCityQuery
    response = requests.get(get_cities_request, headers={'Content-Type': 'application/json',
                                                         'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.common
def test_get_categories():
    get_categories_request = config.BASEURL + config.CategoriesResource
    response = requests.get(get_categories_request, headers={'Content-Type': 'application/json',
                                                             'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.common
def test_get_collections():
    get_collections_request = config.BASEURL + config.CollectionsResource + config.BengaluruCityIdQuery
    print(get_collections_request)
    response = requests.get(get_collections_request, headers={'Content-Type': 'application/json',
                                                              'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.common
def test_get_establishments():
    get_establishments_request = config.BASEURL + config.EstablishmentsResource + config.BengaluruCityIdQuery
    response = requests.get(get_establishments_request, headers={'Content-Type': 'application/json',
                                                                 'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.common
def test_get_geocode():
    get_geocode_request = config.BASEURL + config.GeocodeResource
    response = requests.get(get_geocode_request, headers={'Content-Type': 'application/json',
                                                          'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'





