import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 51)
y = 15 * np.sin(10 * x) * np.cos(3 * x)

plt.plot(x, y, label='15*sin(10x)*cos(3x)', color='purple', linewidth=3)

plt.title('Графік функції Y(x) = 15*sin(10x)*cos(3x)', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')
plt.legend()
plt.grid(True)

plt.show()
