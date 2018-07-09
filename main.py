#!/usr/bin/python
# -*- coding: utf-8 -*-

from synch import *
from calc import *


data1 = sys.argv[1]
data2 = sys.argv[2]
x = synchro(data1, data2)
x = cal(x[0],x[1], float(sys.argv[3]))
print "Odległość 1. telefonu od źródła dźwięku = %.2f" % x[0]+" m, dźwięk dochodzi pod kątem %.2f" %x[2]+" stopni"
print "Odległość 2. telefonu od źródła dźwięku = %.2f" %x[1]+" m, dźwięk dochodzi pod kątem %.2f" %x[3]+" stopni"
