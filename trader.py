# -*- coding: UTF-8 -*-
# @yasinkuyu

import sys
import argparse

sys.path.insert(0, './app')

from Trading import Trading
      
if __name__ == '__main__':
    
    # Set parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--quantity', type=float, help='300', default=0)
    parser.add_argument('--amount', type=float, help='0', default=0)
    parser.add_argument('--symbol', type=str, help='XVGBTC', required=True)
    parser.add_argument('--profit', type=float, help='0.5', default=1.3)

    parser.add_argument('--stop_loss', type=float, help='0', default=0) 

    parser.add_argument('--increasing', type=float, help='Buy Price +Increasing (0.00000001)', default=0.00000001)
    parser.add_argument('--decreasing', type=float, help='Sell Price -Decreasing (0.00000001)', default=0.00000001)

    # Manually defined --orderid try to sell 
    parser.add_argument('--orderid', type=int, help='Target Order Id (use balance.py)', default=0)

    parser.add_argument('--wait_time', type=float, help='1', default=0.7)
    parser.add_argument('--test_mode', type=bool, help='False', default=False)
    parser.add_argument('--prints', type=bool, help='Scanning Profit Screen Print True/False', default=True)
    parser.add_argument('--debug', type=bool, help='Debug True/False', default=True)
    parser.add_argument('--loop', type=int, help='Loop (0 unlimited)', default=0)

    # Working Modes
    #  - profit: Profit Hunter. Find defined profit, buy and sell. (Ex: 1.3% profit)
    #  - range: Between target two price, buy and sell. (Ex: <= 0.00100 buy - >= 0.00150 sell )
    parser.add_argument('--mode', type=str, help='Working Mode', default='profit')
    parser.add_argument('--buyprice', type=float, help='474', default=0)
    parser.add_argument('--sellprice', type=float, help='475', default=0)
    
    option = parser.parse_args()
    
    # Get start
    t = Trading(option)
    t.run()
