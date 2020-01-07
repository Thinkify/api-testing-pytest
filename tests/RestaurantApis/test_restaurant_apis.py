
import requests
import pytest
import json

from resources import config
from tests.support.assertions import assert_valid_schema


@pytest.mark.restaurant
def test_get_dailymenu():
    get_dailymenu_request = config.BASEURL + config.DailyMenuResource + config.ResIdQuery
    dailymenu_response = requests.get(get_dailymenu_request, headers={'Content-Type': 'application/json',
                                                                      'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert dailymenu_response.status_code == 200, 'status code is not equal to 200'
    dailymenu_response_json = json.loads(dailymenu_response.content)
    assert_valid_schema(dailymenu_response_json, 'DailyMenuResponseSchema.json')


@pytest.mark.restaurant
def test_get_restaurant():
    get_restaurant_request = config.BASEURL + config.RestaurantResource + config.ResIdQuery
    restaurant_response = requests.get(get_restaurant_request, headers={'Content-Type': 'application/json',
                                                                        'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert restaurant_response.status_code == 200, 'status code is not equal to 200'
    restaurant_response_json = json.loads(restaurant_response.content)
    assert_valid_schema(restaurant_response_json, 'RestaurantResponseSchema.json')


@pytest.mark.restaurant
def test_get_reviews():
    get_reviews_request = config.BASEURL + config.ReviewsResource + config.ResIdQuery
    reviews_response = requests.get(get_reviews_request, headers={'Content-Type': 'application/json',
                                                                  'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert reviews_response.status_code == 200, 'status code is not equal to 200'
    reviews_response_json = json.loads(reviews_response.content)
    assert_valid_schema(reviews_response_json, 'ReviewsResponseSchema.json')


@pytest.mark.restaurant
def test_get_search():
    get_search_request = config.BASEURL + config.SearchResource + config.BengaluruCityQuery
    search_response = requests.get(get_search_request, headers={'Content-Type': 'application/json',
                                                                'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert search_response.status_code == 200, 'status code is not equal to 200'
    search_response_json = json.loads(search_response.content)
    assert_valid_schema(search_response_json, 'SearchResponseSchema.json')
