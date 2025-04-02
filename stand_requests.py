import configuration
import data
import requests

def post_new_order():
    req = requests.post(configuration.URL + configuration.CREATE_ORDERS,
                         json = data.orders_body)
    return req


def get_orders_track(track_number):
    req = requests.get(configuration.URL + configuration.ORDERS_TRACK, 
                       params ={"t":track_number})
    return req
    
