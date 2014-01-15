#
#  ystockquote : Python module - retrieve stock quote data from Yahoo Finance
#
#  Copyright (c) 2007,2008,2013 Corey Goldberg (cgoldberg@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  Requires: Python 2.7/3.3+


__version__ = '0.2.5dev'

try:
    # py3
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # py2
    from urllib2 import Request, urlopen
    from urllib import urlencode


def _request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    req = Request(url)
    resp = urlopen(req)
    content = resp.read().decode().strip()
    return content


def get_all(symbol):
    """
    Get all available quote data for the given ticker symbol.

    Returns a dictionary.
    """

    # Broken IDs down into sets of 5 to confirm alignment, resolves Issue #12
    ids = \
        'ydb2r1b3' \
        'qpoc1d1' \
        'cd2c6t1k2' \
        'p2c8m5gm7' \
        'hm8k1m3l' \
        'm4l1t8w1g1' \
        'w4g3p1g4m' \
        'g5m2g6kv' \
        'jj1j5j3k4' \
        'j6nk5n4' \
        'ws1xv' \
        'a5b6k3t7a2' \
        't6i5l2el3' \
        'e7v1e8v7e9' \
        's6b4j4p5p6' \
        'rr2r5r6r7s7'
        # 'ydb2r1b3qpoc1d1cd2c6t1k2p2c8m5c3m6gm7hm8k1m3lm4l1t8w1g1w4g3p' \
        # '1g4mg5m2g6kvjj1j5j3k4f6j6nk5n4ws1xj2va5b6k3t7a2t615l2el3e7v1' \
        # 'e8v7e9s6b4j4p5p6rr2r5r6r7s7'
    values = _request(symbol, ids).split(',')
    return dict(
        dividend_yield=values[0],  # y
        dividend_per_share=values[1],  # d
        ask_realtime=values[2],  # b2
        dividend_pay_date=values[3],  # r1
        bid_realtime=values[4],  # b3

        ex_dividend_date=values[5],  # q
        previous_close=values[6],  # p
        today_open=values[7],  # o
        change=values[8],  # c1
        last_trade_date=values[9],  # d1

        change_percent_change=values[10],  # c
        trade_date=values[11],  # d2
        change_realtime=values[12],  # c6
        last_trade_time=values[13],  # t1
        change_percent_realtime=values[14],  # k2

        change_percent=values[15],  # p2
        after_hours_change_realtime=values[16],  # c8
        change_200_sma=values[17],  # m5
        todays_low=values[18],  # g
        change_50_sma=values[19],  # m7

        todays_high=values[20],  # h
        percent_change_50_sma=values[21],  # m8
        last_trade_realtime_time=values[22],  # k1
        fifty_sma=values[23],  # m3
        last_trade_time_plus=values[24],  # l - el

        twohundred_sma=values[25],  # m4
        last_trade_price=values[26],  # l1 - el one
        one_year_target=values[27],  # t8
        todays_value_change=values[28],  # w1
        holdings_gain_percent=values[29],  # g1

        todays_value_change_realtime=values[30],  # w4
        annualized_gain=values[31],  # g3
        price_paid=values[32],  # p1
        holdings_gain=values[33],  # g4
        todays_range=values[34],  # m

        holdings_gain_percent_realtime=values[35],  # g5
        todays_range_realtime=values[36],  # m2
        holdings_gain_realtime=values[37],  # g6
        fiftytwo_week_high=values[38],  # k
        more_info=values[39],  # v

        fiftytwo_week_low=values[40],  # j
        market_cap=values[41],  # j1
        change_from_52_week_low=values[42],  # j5
        market_cap_realtime=values[43],  # j3
        change_from_52_week_high=values[44],  # k4

        float_shares=_request(symbol, 'f6'),  # ''.join(values[45:47]),  # f6
        percent_change_from_52_week_low=values[45],  # j6
        company_name=values[46],  # n
        percent_change_from_52_week_high=values[47],  # k5
        notes=values[48],  # n4

        fiftytwo_week_range=values[49],  # w
        shares_owned=values[50],  # s1
        stock_exchange=values[51],  # x
        shares_outstanding=_request(symbol, 'j2'),  # j2
        volume=values[52],  # v

        ask_size=values[53],  # a5
        bid_size=values[54],  # b6
        last_trade_size=values[55],  # k3
        ticker_trend=values[56],  # t7
        average_daily_volume=values[57],  # a2

        trade_links=values[58],  # t6
        order_book_realtime=values[59],  # i5
        high_limit=values[60],  # l2
        eps=values[61],  # e
        low_limit=values[62],  # l3

        eps_estimate_current_year=values[63],  # e7
        holdings_value=values[64],  # v1
        eps_estimate_next_year=values[65],  # e8
        holdings_value_realtime=values[66],  # v7
        eps_estimate_next_quarter=values[67],  # e9

        revenue=values[68],  # s6
        book_value=values[69],  # b4
        ebitda=values[70],  # j4
        price_sales=values[71],  # p5
        price_book=values[72],  # p6

        pe=values[73],  # r
        pe_realtime=values[74],  # r2
        peg=values[75],  # r5
        price_eps_estimate_current_year=values[76],  # r6
        price_eps_estimate_next_year=values[77],  # r7
        short_ratio=values[78],  # s7
    )


def get_dividend_yield(symbol):
    return _request(symbol, 'y')


def get_dividend_per_share(symbol):
    return _request(symbol, 'd')


def get_ask_realtime(symbol):
    return _request(symbol, 'b2')


def get_dividend_pay_date(symbol):
    return _request(symbol, 'r1')


def get_bid_realtime(symbol):
    return _request(symbol, 'b3')


def get_ex_dividend_date(symbol):
    return _request(symbol, 'q')


def get_previous_close(symbol):
    return _request(symbol, 'p')


def get_today_open(symbol):
    return _request(symbol, 'o')


def get_change(symbol):
    return _request(symbol, 'c1')


def get_last_trade_date(symbol):
    return _request(symbol, 'd1')


def get_change_percent_change(symbol):
    return _request(symbol, 'c')


def get_trade_date(symbol):
    return _request(symbol, 'd2')


def get_change_realtime(symbol):
    return _request(symbol, 'c6')


def get_last_trade_time(symbol):
    return _request(symbol, 't1')


def get_change_percent_realtime(symbol):
    return _request(symbol, 'k2')


def get_change_percent(symbol):
    return _request(symbol, 'p2')


def get_after_hours_change(symbol):
    return _request(symbol, 'c8')


def get_change_200_sma(symbol):
    return _request(symbol, 'm5')


def get_commission(symbol):
    return _request(symbol, 'c3')


def get_percent_change_200_sma(symbol):
    return _request(symbol, 'm6')


def get_todays_low(symbol):
    return _request(symbol, 'g')


def get_change_50_sma(symbol):
    return _request(symbol, 'm7')


def get_todays_high(symbol):
    return _request(symbol, 'h')


def get_percent_change_50_sma(symbol):
    return _request(symbol, 'm8')


def get_last_trade_realtime_time(symbol):
    return _request(symbol, 'k1')


def get_50_sma(symbol):
    return _request(symbol, 'm3')


def get_last_trade_time_plus(symbol):
    return _request(symbol, 'l')


def get_200_sma(symbol):
    return _request(symbol, 'm4')


def get_last_trade_price(symbol):
    return _request(symbol, 'l1')


def get_1_year_target(symbol):
    return _request(symbol, 't8')


def get_todays_value_change(symbol):
    return _request(symbol, 'w1')


def get_holdings_gain_percent(symbol):
    return _request(symbol, 'g1')


def get_todays_value_change_realtime(symbol):
    return _request(symbol, 'w4')


def get_annualized_gain(symbol):
    return _request(symbol, 'g3')


def get_price_paid(symbol):
    return _request(symbol, 'p1')


def get_holdings_gain(symbol):
    return _request(symbol, 'g4')


def get_todays_range(symbol):
    return _request(symbol, 'm')


def get_holdings_gain_percent_realtime(symbol):
    return _request(symbol, 'g5')


def get_todays_range_realtime(symbol):
    return _request(symbol, 'm2')


def get_holdings_gain_realtime(symbol):
    return _request(symbol, 'g6')


def get_52_week_high(symbol):
    return _request(symbol, 'k')


def get_more_info(symbol):
    return _request(symbol, 'v')


def get_52_week_low(symbol):
    return _request(symbol, 'j')


def get_market_cap(symbol):
    return _request(symbol, 'j1')


def get_change_from_52_week_low(symbol):
    return _request(symbol, 'j5')


def get_market_cap_realtime(symbol):
    return _request(symbol, 'j3')


def get_change_from_52_week_high(symbol):
    return _request(symbol, 'k4')


def get_float_shares(symbol):
    return _request(symbol, 'f6')


def get_percent_change_from_52_week_low(symbol):
    return _request(symbol, 'j6')


def get_company_name(symbol):
    return _request(symbol, 'n')


def get_percent_change_from_52_week_high(symbol):
    return _request(symbol, 'k5')


def get_notes(symbol):
    return _request(symbol, 'n4')


def get_52_week_range(symbol):
    return _request(symbol, 'w')


def get_shares_owned(symbol):
    return _request(symbol, 's1')


def get_stock_exchange(symbol):
    return _request(symbol, 'x')


def get_shares_outstanding(symbol):
    return _request(symbol, 'j2')


def get_volume(symbol):
    return _request(symbol, 'v')


def get_ask_size(symbol):
    return _request(symbol, 'a5')


def get_bid_size(symbol):
    return _request(symbol, 'b6')


def get_last_trade_size(symbol):
    return _request(symbol, 'k3')


def get_ticker_trend(symbol):
    return _request(symbol, 't7')


def get_average_daily_volume(symbol):
    return _request(symbol, 'a2')


def get_trade_links(symbol):
    return _request(symbol, 't6')


def get_order_book_realtime(symbol):
    return _request(symbol, 'i5')


def get_high_limit(symbol):
    return _request(symbol, 'l2')


def get_eps(symbol):
    return _request(symbol, 'e')


def get_low_limit(symbol):
    return _request(symbol, 'l3')


def get_eps_estimate_current_year(symbol):
    return _request(symbol, 'e7')


def get_holdings_value(symbol):
    return _request(symbol, 'v1')


def get_eps_estimate_next_year(symbol):
    return _request(symbol, 'e8')


def get_holdings_value_realtime(symbol):
    return _request(symbol, 'v7')


def get_eps_estimate_next_quarter(symbol):
    return _request(symbol, 'e9')


def get_revenue(symbol):
    return _request(symbol, 's6')


def get_book_value(symbol):
    return _request(symbol, 'b4')


def get_ebitda(symbol):
    return _request(symbol, 'j4')


def get_price_sales(symbol):
    return _request(symbol, 'p5')


def get_price_book(symbol):
    return _request(symbol, 'p6')


def get_pe(symbol):
    return _request(symbol, 'r')


def get_pe_realtime(symbol):
    return _request(symbol, 'r2')


def get_peg(symbol):
    return _request(symbol, 'r5')


def get_price_eps_estimate_current_year(symbol):
    return _request(symbol, 'r6')


def get_price_eps_estimate_next_year(symbol):
    return _request(symbol, 'r7')


def get_short_ratio(symbol):
    return _request(symbol, 's7')


def get_historical_prices(symbol, start_date, end_date):
    """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYY-MM-DD'

    Returns a nested dictionary (dict of dicts).
    outer dict keys are dates ('YYYY-MM-DD')
    """
    params = urlencode({
        's': symbol,
        'a': int(start_date[5:7]) - 1,
        'b': int(start_date[8:10]),
        'c': int(start_date[0:4]),
        'd': int(end_date[5:7]) - 1,
        'e': int(end_date[8:10]),
        'f': int(end_date[0:4]),
        'g': 'd',
        'ignore': '.csv',
    })
    url = 'http://ichart.yahoo.com/table.csv?%s' % params
    req = Request(url)
    resp = urlopen(req)
    content = str(resp.read().decode('utf-8').strip())
    daily_data = content.splitlines()
    hist_dict = dict()
    keys = daily_data[0].split(',')
    for day in daily_data[1:]:
        day_data = day.split(',')
        date = day_data[0]
        hist_dict[date] = \
            {keys[1]: day_data[1],
             keys[2]: day_data[2],
             keys[3]: day_data[3],
             keys[4]: day_data[4],
             keys[5]: day_data[5],
             keys[6]: day_data[6]}
    return hist_dict
