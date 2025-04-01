import stand_requests




def test_order_track():
    req = stand_requests.get_orders_track()

    assert req.status_code == 200