# script_name.py
#
# Usage: python3 eci_to_ecef.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Andrew McGrellis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv
import numpy as np

# "constants"
R_E_KM  = 6378.1363
EE_E    = 0.081819221456
W       = 7.292115e-5
C = 2.99792458e8

# helper functions

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
if len(sys.argv) == 8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 arg1 arg2 ...'\
  )
  exit()

# write script below this line

aper_wv = C / freq_hz
rx_gain_t = 10**(rx_gain_db/10)
tx_gain_t = 10**(tx_gain_db/10)
dist_m = dist_km * 1000

rx_w = tx_w * 10**(-1/10) * tx_gain_t * (aper_wv/(4*math.pi*dist_m))**2 * 10**(0/10) * rx_gain_t
print(rx_w)
rxN_w = n0_j * bw_hz
print(rxN_w)

r_max = bw_hz*math.log2(1 + rx_w/rxN_w)

print(math.floor(r_max))