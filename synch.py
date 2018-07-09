# -*- coding: utf-8 -*-
import sys
import numpy as np
from scipy.io import wavfile
import scipy
import math


#odległosc między telefonami w centymetrach
def synchro(name1, name2):
	pr_dz = 340 #m/s
	#analiza w pierwszych 200000 próbek w celu znalezienia przesunięcia w czasie nagrania
	synchr = 200000
	#ucinamy ostanie ~ 20000 próbek odsiew zakłóceń jakie pojawiają się pod koniec nagrywania
	cat = 20000
	#wczytywanie pierwszego sygnału
	fs1, data1 = wavfile.read(name1)
	l_audio = len(data1.shape)
	data1 = data1
	if l_audio == 2:
   		data1 = data1.sum(axis=1) / 2
	Ts1 = 1.0/fs1
	N1 = data1.shape[0]
	secs1 = N1 / float(fs1)
	t1 = scipy.arange(0, secs1, Ts1)
	#wczytywanie drugiego sygnału
	fs2, data2 = wavfile.read(name2)
	l_audio = len(data1.shape)
	if l_audio == 2:
		data2 = data2.sum(axis=1) / 2
	Ts2 = 1.0/fs2
	N2 = data1.shape[0]
	secs2 = N2 / float(fs2)
	t2 = scipy.arange(0, secs2, Ts2)
	if synchr > N1:
		synchr = int(len(data1))
		print synchr
	if synchr > N2:
		synchr = int(len(data2))
		print synchr
	arg_max2 = np.argmax(data2[:synchr])
	if arg_max2 > len(data2):
		arg_max2 = int(len(data2)-1)
	arg_max1 = np.argmax(data1[:synchr])
	if arg_max1 > len(data1):
		arg_max1 = int(len(data1)-1)
	delta = arg_max2-arg_max1
	conf_rat = abs(data1[arg_max1]/float(data2[arg_max2][0]))
	#obliczanie różnicy i stosunku
	index = np.argmax(data1[synchr:N1-cat])
	if index > len(data1):
		index = len(data1)-1
	index1 = np.argmax(data2[synchr:N2-cat])
	if index1 > len(data2):
		index1 = len(data2)-1
	rat = abs(data1[index]**2/float(data2[index1][0]**2))

	if delta <0:
		index1 = index1+delta
	else:
		index = index-delta
	dif = (index-index1)
	if (dif < 0):
		dif= t1[-1*dif]
	else:
		dif= t1[dif]

	return math.sqrt(dif), rat #*conf_rat

