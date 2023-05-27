import json


async def test_create_orders(test_app):
    content = {
        "volume": 1000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "BUY",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    global post_orders
    post_orders = []
    for i in response.json():
        post_orders.append(dict(list(i.items())[:4]))
    assert response.status_code == 201


async def test_get_orders(test_app):
    response = await test_app.get(f"/api/get_orders")
    get_orders = []
    for i in response.json():
        get_orders.append(dict(list(i.items())[:4]))
    get_orders = sorted(get_orders, key=lambda k: k['orderId'])
    print(get_orders)
    print(post_orders)
    assert response.status_code == 200
    assert post_orders == get_orders


async def test_create_orders_missing_value(test_app):
    content = {
        "number": 5,
        "amountDif": 50.0,
        "side": "SELL",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    assert response.status_code == 422
    assert response.json() == {"ValidationError": "volume field required"}


async def test_create_orders_wrong_type_value(test_app):
    content = {
        "volume": "hgjgk",
        "number": 5,
        "amountDif": 50.0,
        "side": "BUY",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    assert response.status_code == 422
    assert response.json() == {
        "ValidationError": "volume value is not a valid integer"}


async def test_create_orders_invalid_side(test_app):
    content = {
        "volume": 1000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "hgffk",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    assert response.status_code == 400
    assert response.json() == {
        "BinanceAPIException": "Invalid side."}


async def test_create_orders_margin(test_app):
    content = {
        "volume": 100000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "BUY",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    assert response.status_code == 400
    assert response.json() == {
        "BinanceAPIException": "Margin is insufficient."}


async def test_create_orders_leverage(test_app):
    content = {
        "volume": 1000000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "BUY",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    assert response.status_code == 400
    assert response.json() == {
        "BinanceAPIException": "Exceeded the maximum allowable position at current leverage."}


async def test_create_orders_max_quantity(test_app):
    content = {
        "volume": 1000000000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "BUY",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    assert response.status_code == 400
    assert response.json() == {
        "BinanceAPIException": "Quantity greater than max quantity."}


async def test_create_orders_max_price(test_app):
    content = {
        "volume": 1000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "BUY",
        "priceMin": 20000.0,
        "priceMax": 30000.0
    }
    response = await test_app.post(f"/api/create_orders", content=json.dumps(content))
    assert response.status_code == 400
    assert response.json() == {
        "BinanceAPIException": "Price greater than max price."}


async def test_cancel_orders(test_app):
    response = await test_app.delete(f"/api/cancel_orders")
    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "msg": "The operation of cancel all open order is done."
    }
