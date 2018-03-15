import sys
import argparse
from math import factorial
from decimal import Decimal, getcontext


def calculate_pi(size):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for _ in range(size):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

parser = argparse.ArgumentParser(description='Python Chudnovsky')
parser.add_argument('size', metavar='s', type=int, help='The accuracy to calculate')
args = parser.parse_args()

for i in calculate_pi(args.size):
    print(str(i), flush=True, end='')