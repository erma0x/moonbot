#!/usr/bin/env python3.7
# coding: utf-8
"""
in the shell 
export binance_api="your_api_key_here"
export binance_secret="your_api_secret_here"
"""
import time
import os
import asyncio
from copy import deepcopy
from modules.utils_bot import *
import time

from binance.enums import *
from binance import AsyncClient

async def main():
    api_key = os.environ.get('binance_api') 
    api_secret = os.environ.get('binance_secret')
    client = await AsyncClient.create(api_key, api_secret)

    commissionSpotMaker = 0.075 # %
    commissionSpotTaker = 0.075 # %

    investment= 12 # $                       # 0.0075
    effective_investment = investment- (commissionSpotMaker/100) * investment
    open_price_buy = 0 

    min_gain_perc_buy = 0.09 # %[0,100] + commissions 
    min_gain_perc_sell = 0.1 # %[0,100]

    max_open_orders = 1 # open orders at the same time
    my_symbol = 'ETH'

    Orderbook = []


    while True:
        priceBUSD = await get_data(client,token_pair=my_symbol+'BUSD')
        priceUSDT = await get_data(client,token_pair=my_symbol+'USDT')
        
        print(my_symbol+'USDT ',priceUSDT,'\t|\t',my_symbol+'BUSD : ',priceBUSD)
        
        lower_price_stablecoin = min(priceUSDT,priceBUSD)
        
        coin_quantity = effective_investment/lower_price_stablecoin

        estimed_abs_gain = coin_quantity*max(priceUSDT,priceBUSD) - effective_investment
        estimed_perc_gain = estimed_abs_gain/effective_investment*100
        
        print('estimed gain: % ',estimed_perc_gain,': $ ',estimed_abs_gain)



# BUY TOKEN
        if estimed_perc_gain+commissionSpotMaker >= min_gain_perc_buy and len(Orderbook)<=max_open_orders:
            if priceUSDT > priceBUSD:
                buy_stablecoin='BUSD'

            if priceUSDT < priceBUSD:
                buy_stablecoin='USDT'

            buy_symbol = my_symbol + buy_stablecoin


            order = await client.order_limit_buy(timeInForce='TOC',
                                symbol = buy_symbol,
                                quantity = await format_coin_quantity(coin_quantity, symbol = buy_symbol),
                                price = round(float(min(priceBUSD,priceUSDT)),2))

            
            print_OPEN(order)
            Orderbook.append(order)

            for n_order in range(len(Orderbook)):

                if Orderbook[n_order]['status']=='CANCELED':
                    Orderbook.remove(Orderbook[j])

                elif Orderbook[n_order]['status']=='FILLED':
                    print_FILLED(Orderbook[n_order])
                    if priceUSDT < priceBUSD:
                        sell_stablecoin='BUSD'

                    if priceUSDT > priceBUSD:
                        sell_stablecoin='USDT'

                    price_sell = (( (min_gain_perc_sell+commissionSpotMaker)/100) + 1) * open_price_buy

                    order = await client.order_limit_sell(timeInForce='IOC',
                                        symbol = sell_symbol,
                                        quantity = await format_coin_quantity(coin_quantity,symbol=sell_symbol),
                                        price = round(float(price_sell),2))

                    Orderbook.remove(Orderbook[n_order])

                    sell_symbol = deepcopy(my_symbol+sell_stablecoin)
                                    
                                              # 0.1                          + 0.075         => 0.175 %
                    price_sell = (( (min_gain_perc_sell+commissionSpotMaker)/100) + 1) * open_price_buy


                else:
                    pass



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())