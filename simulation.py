import numpy as np
import matplotlib.pyplot as plt

# 1. Основные константы
phi = (1 + 5**0.5) / 2
x_g = 1 / phi           # Золотое сечение (0.618)
p_0 = 5 / 6             # Порог насыщения (0.833)
n_theoretical = np.log(1 - p_0) / np.log(1 - x_g)

print(f"Теоретический экспонент n: {n_theoretical:.4f}")

# 2. Функция профиля f_n(x)
def f_n(x, n):
    return 1 - (1 - x)**n

# 3. Функция стоимости (кривизна)
def cost_functional(n):
    # Аналитическое решение интеграла второй производной в квадрате
    return (n**2 * (n - 1)**2) / (2 * n - 3)

# --- ВИЗУАЛИЗАЦИЯ ---
x = np.linspace(0, 1, 500)
n_range = np.linspace(1.51, 2.5, 100) # Диапазон для поиска минимума

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Левый график: Профиль и золотая точка
ax[0].plot(x, f_n(x, n_theoretical), label=f'n = {n_theoretical:.2f}', color='blue', lw=2)
ax[0].scatter([x_g], [p_0], color='red', zorder=5, label='Golden Point (1/φ, 5/6)')
ax[0].set_title('Accelerating Profile f_n(x)')
ax[0].set_xlabel('Scale (x)')
ax[0].set_ylabel('Intensity (f)')
ax[0].grid(True, alpha=0.3)
ax[0].legend()

# Правый график: Оптимизация энергии
costs = [cost_functional(n) for n in n_range]
ax[1].plot(n_range, costs, color='green', lw=2, label='Curvature Cost C(n)')
ax[1].axvline(n_theoretical, color='red', linestyle='--', label=f'n_theory ≈ 1.86')
ax[1].set_title('Energy Cost Functional Optimization')
ax[1].set_xlabel('Exponent (n)')
ax[1].set_ylabel('Structural Stress C(n)')
ax[1].grid(True, alpha=0.3)
ax[1].legend()

plt.tight_layout()
plt.show()
