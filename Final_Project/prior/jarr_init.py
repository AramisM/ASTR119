# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import numpy.random as rand

rho = 2.65 # grams per cubic centimeter for granite
moon = 7.35*10**22 # lunar mass in grams
moon_dist = 384400000. # lunar distance in m
#deimos = 1.48*10**18 # smallest moon in solar system in grams
N = 1000 # number of objects

mu = moon/N # average mass of an object
print mu


def grandom(mu):
    # Mean (“centre”) of the distribution, Std, Output shape
    noise = np.random.normal(loc=mu, scale=np.sqrt(mu), size=len(x))
    return noise


rand_mass = grandom(mu)
rand_a = grandom(moon_dist)
rand_e = rand.rand(N)

