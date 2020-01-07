
import requests
import pytest
import json

from resources import config
from tests.support.assertions import assert_valid_schema


@pytest.mark.location
def test_get_location_details():
    get_location_details_request = config.BASEURL + config.LocationDetailsResource + config.BengaluruEntityIdQuery + \
                                   '&' + config.BengaluruEntityTypeQuery
    location_details_response = requests.get(get_location_details_request,
                                             headers={'Content-Type': 'application/json',
                                                      'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert location_details_response.status_code == 200, 'status code is not equal to 200'
    location_details_response_json = json.loads(location_details_response.content)
    assert_valid_schema(location_details_response_json, 'LocationDetailsResponseSchema.json')


@pytest.mark.location
def test_get_locations():
    get_locations_request = config.BASEURL + config.LocationsResource + config.BengaluruCityQuery
    locations_response = requests.get(get_locations_request, headers={'Content-Type': 'application/json',
                                                                      'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert locations_response.status_code == 200, 'status code is not equal to 200'
    locations_response_json = json.loads(locations_response.content)
    assert_valid_schema(locations_response_json, 'LocationsResponseSchema.json')