def get_list_of_data():
    coins = ['USDT', 'BTC', 'BUSD', "BNB", 'ETH', "RUB"]
    pay = ['BUY', 'SELL']
    list_sell = []
    list_buy = []
    for payment in pay:
        for coin in coins:
            for page in range(10):
                data = {
                        "asset": coin,
                        "fiat": "RUB",
                        "merchantCheck": False,
                        "page": page,
                        "payTypes": [],
                        "publisherType": None,
                        "rows": 20,
                        "tradeType": payment
                    }
                if payment == 'SELL':
                    list_sell.append(data)
                else:
                    list_buy.append(data)
                    
    return list_sell, list_buy



def get_url_for_okx():
    coins = ['USDT', 'BTC', 'USDC', "DAI", 'ETH', "TUSD"]
    payment = ['BUY', 'SELL']
    list_buy = []
    list_sell = []
    for pay in payment:
        for coin in coins:
            url = f"https://www.okx.com/v3/c2c/tradingOrders/books?t=1658134202115&quoteCurrency=RUB&baseCurrency={coin}&side={pay.lower()}&paymentMethod=all&userType=all&showTrade=false&showFollow=false&showAlreadyTraded=false&isAbleFilter=false"
            if pay == "BUY":
                list_buy.append(url)
            else:
                list_sell.append(url)
    return list_buy, list_sell


def get_url_for_bitzlato()-> list:
    coins = ['USDT', 'BTC', 'USDC', "DAI", 'ETH']
    payment = ['purchase', 'selling']
    list_buy = []
    list_sell = []
    for pay in payment:
        for coin in coins:
            url = f"https://bitzlato.bz/api2/p2p/public/exchange/dsa/?lang=en&limit=100&skip=0&type={pay}&currency=RUB&cryptocurrency={coin}&isOwnerVerificated=false&isOwnerTrusted=false&isOwnerActive=false"
            if pay == 'purchase':
                list_buy.append(url)
            else:
                list_sell.append(url)
    return list_buy, list_sell


def get_url_spot():
    coins = ["BTCUSDT", "ETHUSDT", "BUSDUSDT", "SHIBUSDT", "ETHBTC", "BTCBUSD", "ETHBUSD",
            "SHIBBUSD", "USDTRUB", "BTCRUB", "ETHRUB", "BUSDRUB", "SHIBRUB", "BNBUSDT", "BNBBTC"
            , "BNBBUSD", "BNBETH", "BNBRUB"]
    list_spot = [f"https://api.binance.com/api/v3/ticker/price?symbol={coin}" for coin in coins]
    return list_spot
   
    
def get_url_for_huobi():
    payments = ['buy', 'sell']
    #USDT=2, BTC=1, ETH=3, 
    coins = ['2', '1', '3']
    list_sell = []
    list_buy = []
    for pay in payments:
        for coin in coins:
            for page in range(5):
                url = f'https://otc-api.mycdncache.com/v1/data/trade-market?coinId={coin}&currency=11&tradeType={pay}&currPage={page}&payMethod=0&acceptOrder=-1&country=&blockType=general&online=1&range=0&amount=&onlyTradable=false'
                if pay ==  'buy':
                    list_buy.append(url)
                else:
                    list_sell.append(url)
    return list_buy, list_sell


def get_url_for_bybit():
    coins = ["USDT", "BTC", "ETH"]
    payments = ['1', '0']
    list_buy = []
    list_sell = []
    for pay in payments:
        for coin in coins:
            for page in range(5):
                data = {
                        "tokenId": coin,
                        "currencyId": "RUB",
                        'side': int(pay),
                        "size": 10,
                        "payment": [],
                        "page": int(page)
                    }
                if pay == "1":
                    list_buy.append(data)
                else: 
                    list_sell.append(data)
    return list_buy, list_sell



                      