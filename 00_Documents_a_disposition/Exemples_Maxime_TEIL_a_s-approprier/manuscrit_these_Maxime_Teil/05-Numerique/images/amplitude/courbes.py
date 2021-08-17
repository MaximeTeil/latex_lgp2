# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import spline

ampX, ampY, ampZ = np.loadtxt('ampX.txt', delimiter=','), np.loadtxt('ampY.txt', delimiter=','), np.loadtxt('ampZ.txt', delimiter=',')

time, X, Y, Z = [], [], [], []

for i in range(ampX.size-1):
    if i%4==0:
        time.append(ampX[i]/60.)
        X.append(ampX[i+1])
        Y.append(ampY[i+1])
        Z.append(ampZ[i+1])

time_new = np.linspace(0, max(time), 50)
Xnew = spline(time,X,time_new)
Ynew = spline(time,Y,time_new)
Znew = spline(time,Z,time_new)

plt.figure()
plt.subplots_adjust(top=0.98, right=0.95)
plt.plot(time, X, ls='-', color='k')
plt.plot(time, Y, ls='--', color='k')
plt.plot(time, Z, ls=':', color='k')
plt.legend([u'suivant $(Ox)$', u'suivant $(Oy)$', u'suivant $(Oz)$'], fontsize=14, loc='lower left')
plt.xlabel(u'Temps [min]', fontsize=14)
plt.ylabel(u'Déplacement [mm]', fontsize=14)
plt.savefig(u'courbes_amplitude.eps')

plt.figure()
plt.subplots_adjust(top=0.98, right=0.95)
plt.plot(time_new, Xnew, ls='-', color='k')
plt.plot(time_new, Ynew, ls='--', color='k')
plt.plot(time_new, Znew, ls=':', color='k')
plt.legend([u'suivant $(Ox)$', u'suivant $(Oy)$', u'suivant $(Oz)$'], fontsize=14, loc='lower left')
plt.xlabel(u'Temps [min]', fontsize=14)
plt.ylabel(u'Déplacement [mm]', fontsize=14)
plt.savefig(u'courbes_amplitude_smooth.eps')