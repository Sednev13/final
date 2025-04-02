import stand_requests




def test_order_track():
    create_response = stand_requests.post_new_order()
    track_number = create_response.json()["track"]
    get_response = stand_requests.get_orders_track(track_number)
    assert get_response.status_code == 200


    # Александр Седнев, 28-я когорта — Финальный проект. Инженер по тестированию плюс

