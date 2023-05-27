from binance import AsyncClient


def session(func):
    async def wrapper(*args, **kwargs):
        client = await AsyncClient.create(api_key='4207c1571daf04d7f05281c041a60db19f54318ec34db5a18366f4295d7d31a4',
                                          api_secret='2e40bab840081af464d5357997dac367926bea90716df19f506813cb1674257b', testnet=True)
        result = await func(client, *args, **kwargs)
        await client.close_connection()
        return result
    return wrapper
