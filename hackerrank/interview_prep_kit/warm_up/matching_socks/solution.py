#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    n = len(ar)
    if n < 2:
        return 0

    matching_socks = 0

    sock_colors = dict()

    for sock in ar:
        current_number_for_this_color = sock_colors.get(sock, 0) + 1

        if current_number_for_this_color == 2:
            matching_socks += 1
            current_number_for_this_color = 0

        sock_colors[sock] = current_number_for_this_color

    return matching_socks