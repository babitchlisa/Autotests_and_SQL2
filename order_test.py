import send_request


def test_order_assert():
    track = send_request.create_order().json()['track']
    order = send_request.get_order(track)
    assert order.status_code == 200