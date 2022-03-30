# %%
from numpy import arange
from matplotlib import pyplot

# %%
def objective(x):
    return x[0]**2.0

r_min, r_max = -5.0, 5.0

inputs = arange(r_min, r_max, 0.1)

results = [objective([x]) for x in inputs]

pyplot.plot(inputs, results)

x_optima = 0.0

pyplot.axvline(x=x_optima, ls='--', color='red')

pyplot.show
# %%
