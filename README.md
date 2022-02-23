# Moonboot: let's arbitrage on Binance 

## RUN
```bash
source venv/bin/activate
export binance_api="your api key"
export binance_secret="your api secret"
python3 bot.py
```

# Costs
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

## Installation
```bash
python3 -m venv venv 
source venv/bin/activate
python3 -m pip install --upgrade pip 
python3 -m pip install --upgrade python-binance
export binance_api="your api key"
export binance_secret="your api secret"
```


