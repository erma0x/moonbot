# Moonboot: let's arbitrage on Binance 


## Installation
```bash
python3 -m venv venv 
source venv/bin/activate
python3 -m pip install --upgrade pip 
python3 -m pip install --upgrade python-binance
export binance_api="your api key"
export binance_secret="your api secret"
```

### How to run
```bash
source venv/bin/activate
export binance_api="your api key"
export binance_secret="your api secret"
python3 bot.py
```

## Binance Informations
### Costs
swap 10 cents
spot 0.075% in BNB


### Pairs USDT/BUSD 
- X/BUSD
- X/usdt
- BUSD/usdt

### Pairs BNB/BUSD
- X/BUSD
- X/BNB
- BUSD/BNB

## Errors
APIError(code=-1013): Filter failure: MIN_NOTIONAL


## Get Binance WebSocket Data Stream
### Install
``` bash
npm install -g wscat
```
### Run
``` bash
wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade
```
OR
``` bash
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m
```

### Orders Examples
```python
{'symbol': 'ETHBUSD', 'orderId': 7760933105, 'orderListId': -1, 
'clientOrderId': 'RKPcQ9jAOT8LlUYK3xygGB', 'transactTime': 1644342622758, 
'price': '3040.28000000', 'origQty': '0.00490000', 'executedQty': '0.00000000', 
'cummulativeQuoteQty': '0.00000000', 'status': 'NEW', 'timeInForce': 'GTC',
 'type': 'LIMIT', 'side': 'BUY', 'fills': []}

{'symbol': 'ETHUSDT', 'orderId': 7760933105, 'orderListId': -1, 
'clientOrderId': 'RKPcQ9jAOT8LlUYK3xygGB', 'transactTime': 1644342622758, 
'price': '3040.28000000', 'origQty': '0.00490000', 'executedQty': '0.00490000', 
'cummulativeQuoteQty': '0.00000000', 'status': 'FILLED', 'timeInForce': 'GTC',
 'type': 'MARKET', 'side': 'SELL', 'fills': []}

{'symbol': 'ETHUSDT', 'orderId': 7760933105, 'orderListId': -1, 
'clientOrderId': 'RKPcQ9jAOT8LlUYK3xygGB', 'transactTime': 1644342622758, 
'price': '3040.28000000', 'origQty': '0.00490000', 'executedQty': '0.00000000', 
'cummulativeQuoteQty': '0.00000000', 'status': 'NEW', 'timeInForce': 'IOC',
 'type': 'LIMIT', 'side': 'SELL', 'fills': []}
```

