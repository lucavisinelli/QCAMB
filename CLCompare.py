# sample script to compare two standard _lensedCl results
# ncl=1 does just TT, ncl=3,4 does more
# see camPlots.py for function declaration

from cambPlots import *
from pylab import *


root  = r'../inifiles/test_lensing_lensedCls.dat'
root2 = r'../inifiles/test_lensing_lensedCls.dat'


plot_compare([root, root2], ncl=4, x='sqrt')


show()

