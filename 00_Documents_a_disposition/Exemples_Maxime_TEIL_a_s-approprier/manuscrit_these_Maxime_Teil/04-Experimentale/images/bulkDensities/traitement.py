# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:37:21 2019

@author: mteil
"""

import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/3S-LAB/mteil/Documents/These/manuscrit/04-Experimentale/images/bulkDensities')

ezz, d, marker = {}, {}, {}

tmp_ezz, tmp_d = np.loadtxt('1_a1.txt')*-1., np.loadtxt('1_bulk_density.txt')
ezz['1 MPa'], d['1 MPa'], marker['1 MPa'] = [0], [tmp_d[0]], 's'
for i in range(tmp_ezz.size):
    ezz['1 MPa'].append(tmp_ezz[i])
    d['1 MPa'].append(tmp_d[i+1])
del tmp_ezz, tmp_d

tmp_ezz, tmp_d = np.loadtxt('2_a1.txt')*-1., np.loadtxt('2_bulk_density.txt')
ezz['2 MPa'], d['2 MPa'], marker['2 MPa'] = [0], [tmp_d[0]], 'o'
for i in range(tmp_ezz.size):
    ezz['2 MPa'].append(tmp_ezz[i])
    d['2 MPa'].append(tmp_d[i+1])
del tmp_ezz, tmp_d

tmp_ezz, tmp_d = np.loadtxt('7_a1.txt')*-1., np.loadtxt('7_bulk_density.txt')
ezz['7 MPa'], d['7 MPa'], marker['7 MPa'] = [0], [tmp_d[0]], '^'
for i in range(tmp_ezz.size):
    ezz['7 MPa'].append(tmp_ezz[i])
    d['7 MPa'].append(tmp_d[i+1])
del tmp_ezz, tmp_d

plt.figure()
plt.subplots_adjust(top=0.95, right=0.95, bottom=0.12, left=0.12)
plt.grid(alpha=0.5)
legend = ezz.keys()
legend.reverse()
for i in legend:
    plt.plot(ezz[i], d[i], marker=marker[i])
plt.legend(legend, fontsize=12)
plt.xlabel(u"Déformation logarithmique axiale", fontsize=12)
plt.ylabel(u"Densité relative apparente", fontsize=12)
plt.savefig('bulk_densities.eps')