# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

x = [0., 0.015517, 3]
y = [0., 45., 70.]

plt.figure()
plt.subplots_adjust(top=0.95, right=0.98, left=0.10)
plt.plot(x,y)
plt.xlim(-0.05,3.05)
plt.ylim(0,71)
plt.xlabel(u'Déformation', fontsize=14)
plt.ylabel(u'Contrainte [MPa]', fontsize=14)
plt.savefig('plastic_curve.eps')
