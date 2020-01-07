import requests
from resources import config
import pytest


@pytest.mark.restaurant
def test_get_dailymenu():
    get_dailymenu_request = config.BASEURL + config.DailyMenuResource + config.ResIdQuery
    response = requests.get(get_dailymenu_request, headers={'Content-Type': 'application/json',
                                                            'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.restaurant
def test_get_restaurant():
    get_restaurant_request = config.BASEURL + config.GeocodeResource + config.ResIdQuery
    response = requests.get(get_restaurant_request, headers={'Content-Type': 'application/json',
                                                             'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.restaurant
def test_get_reviews():
    get_reviews_request = config.BASEURL + config.ReviewsResource + config.ResIdQuery
    response = requests.get(get_reviews_request, headers={'Content-Type': 'application/json',
                                                          'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.restaurant
def test_get_search():
    get_search_request = config.BASEURL + config.SearchResource + config.BengaluruCityQuery
    response = requests.get(get_search_request, headers={'Content-Type': 'application/json',
                                                         'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'
