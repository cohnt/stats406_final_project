import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.kernel_regression import KernelReg

x = np.sort(np.random.rand(400) * 10 - 2)
y = x**4 - 8*(x**3) + 14*(x**2) - 32*(x) + 14 + ((np.random.rand(len(x))-0.5)*50)
y_clean = x**4 - 8*(x**3) + 14*(x**2) - 32*(x) + 14

reg = KernelReg(y, x, 'c')
[mean, mfx] = reg.fit()

plt.figure()
plt.scatter(x, y)
plt.plot(x, mean, color="red")
plt.plot(x, y_clean, color="green")
plt.show()