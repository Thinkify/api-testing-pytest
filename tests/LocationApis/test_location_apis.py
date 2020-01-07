import requests
from resources import config
import pytest


@pytest.mark.location
def test_get_location_details():
    get_location_details_request = config.BASEURL + config.LocationDetailsResource +config.BengaluruEntityIdQuery + '&'\
                                   + config.BengaluruEntityTypeQuery
    response = requests.get(get_location_details_request, headers={'Content-Type': 'application/json',
                                                                   'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'


@pytest.mark.location
def test_get_locations():
    get_locations_request = config.BASEURL + config.LocationsResource + config.BengaluruCityQuery
    response = requests.get(get_locations_request, headers={'Content-Type': 'application/json',
                                                            'user-key': '31f6ec0e0eed0b5624414a8229146b01'})
    assert response.status_code == 200, 'status code is not equal to 200'