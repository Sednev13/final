import configuration
import data
import requests

def post_new_order():
    req = requests.post(configuration.URL + configuration.CREATE_ORDERS,
                         json = data.orders_body).json()["track"]
    return req

#print(post_new_order())

def get_orders_track():
    params = post_new_order()
    req = requests.get(configuration.URL + configuration.ORDERS_TRACK, 
                       params ={"t":params})
    return req
    
#print(get_orders_track())