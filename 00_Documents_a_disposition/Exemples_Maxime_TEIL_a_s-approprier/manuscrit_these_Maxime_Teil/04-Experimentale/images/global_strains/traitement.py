# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:50:30 2019

@author: mteil
"""

import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/3S-LAB/mteil/Documents/These/manuscrit/04-Experimentale/images/global_strains/')

ezz, edev, evol, marker = {}, {}, {}, {}
for i in ['1 MPa', '2 MPa', '7 MPa']:
    ezz[i] = (-1.*np.loadtxt(i[0]+'_e_zz.txt')).tolist()
    ezz[i].insert(0,0)
    edev[i] = np.loadtxt(i[0]+'_e_dev.txt').tolist()
    edev[i].insert(0,0)
    evol[i] = np.loadtxt(i[0]+'_e_vol.txt').tolist()
    evol[i].insert(0,0)

marker['1 MPa'] = 's'; marker['2 MPa'] = 'o'; marker['7 MPa'] = '^'

plt.figure()
plt.subplots_adjust(top=.95, right=.95, bottom=.12, left=.12)
legend = ezz.keys()
legend.reverse()
plt.grid(alpha=0.5)
for i in legend:
    plt.plot(ezz[i], evol[i], marker=marker[i])
plt.legend(legend, fontsize=12)
plt.xlabel(u'Déformation axiale', fontsize=12)
plt.ylabel(u'Déformation volumique', fontsize=12)
plt.savefig('global_volumetric.eps')

plt.figure()
plt.subplots_adjust(top=.95, right=.95, bottom=.12, left=.12)
legend = ezz.keys()
legend.reverse()
plt.grid(alpha=0.5)
for i in legend:
    plt.plot(ezz[i], edev[i], marker=marker[i])
plt.legend(legend, fontsize=12)
plt.xlabel(u'Déformation axiale', fontsize=12)
plt.ylabel(u'Déformation déviatoire', fontsize=12)
plt.savefig('global_deviatoric.eps')