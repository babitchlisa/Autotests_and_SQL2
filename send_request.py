import requests
import configuration
import data


def create_order():
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_PATH, headers=data.headers)

def get_order(track):
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER_PATH, params={"t": track}, headers=data.headers)