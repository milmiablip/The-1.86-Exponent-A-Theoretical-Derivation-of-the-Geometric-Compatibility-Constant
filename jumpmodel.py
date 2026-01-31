import numpy as np
import matplotlib.pyplot as plt

# Константы Марины
PHI = (1 + 5**0.5) / 2
GOLDEN_NODE_X = 1 / PHI
THRESHOLD_5_6 = 5 / 6
N_IDEAL = 1.8617  # Твоя выведенная константа

def f(x, n):
    return 1 - (1 - x)**n

x = np.linspace(0, 1, 500)
n_values = [1.2, N_IDEAL, 3.0]
labels = ['n = 1.2 (Недостаточно)', f'n = {N_IDEAL} (ЗОЛОТОЙ ПРЫЖОК)', 'n = 3.0 (Коллапс)']
colors = ['gray', 'gold', 'red']

plt.figure(figsize=(10, 6))

for n, label, color in zip(n_values, labels, colors):
    y = f(x, n)
    lw = 3 if n == N_IDEAL else 1.5
    plt.plot(x, y, label=label, color=color, linewidth=lw)

# Линии ограничений
plt.axvline(GOLDEN_NODE_X, color='green', linestyle='--', alpha=0.6, label='Золотой Узел (1/Φ)')
plt.axhline(THRESHOLD_5_6, color='blue', linestyle=':', alpha=0.6, label='Порог Прыжка (5/6)')

# Точка перехода
plt.scatter([GOLDEN_NODE_X], [f(GOLDEN_NODE_X, N_IDEAL)], color='black', zorder=5)
plt.annotate('ТОЧКА СИНХРОНИЗАЦИИ', xy=(GOLDEN_NODE_X, f(GOLDEN_NODE_X, N_IDEAL)), 
             xytext=(0.1, 0.9), arrowprops=dict(facecolor='black', shrink=0.05))

plt.title("Моделирование межпространственного перехода (Экспонента 1.86)")
plt.xlabel("Прогресс деформации (x)")
plt.ylabel("Плотность метрики (p)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
