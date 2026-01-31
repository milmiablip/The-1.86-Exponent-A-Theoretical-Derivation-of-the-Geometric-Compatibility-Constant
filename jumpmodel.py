import numpy as np
import matplotlib.pyplot as plt

# Marina's Fundamental Constants
PHI = (1 + 5**0.5) / 2
GOLDEN_NODE_X = 1 / PHI
THRESHOLD_5_6 = 5 / 6
N_IDEAL = 1.8617  # Your derived "Safe-Stitch" exponent

def f(x, n):
    return 1 - (1 - x)**n

x = np.linspace(0, 1, 500)
n_values = [1.2, N_IDEAL, 3.0]
labels = [
    'n = 1.2 (Insufficient)', 
    f'n = {N_IDEAL} (GOLDEN JUMP)', 
    'n = 3.0 (Metric Collapse)'
]
colors = ['gray', 'gold', 'red']

plt.figure(figsize=(12, 7))

for n, label, color in zip(n_values, labels, colors):
    y = f(x, n)
    lw = 3 if n == N_IDEAL else 1.5
    plt.plot(x, y, label=label, color=color, linewidth=lw)

# Boundary and Anchor Lines
plt.axvline(GOLDEN_NODE_X, color='green', linestyle='--', alpha=0.6, label='Golden Node (1/Φ)')
plt.axhline(THRESHOLD_5_6, color='blue', linestyle=':', alpha=0.6, label='Jump Threshold (5/6)')

# Transition Point (The Sync Point)
plt.scatter([GOLDEN_NODE_X], [f(GOLDEN_NODE_X, N_IDEAL)], color='black', zorder=5)
plt.annotate('SYNCHRONIZATION POINT', 
             xy=(GOLDEN_NODE_X, f(GOLDEN_NODE_X, N_IDEAL)), 
             xytext=(0.05, 0.9), 
             fontsize=10,
             fontweight='bold',
             arrowprops=dict(facecolor='black', shrink=0.05))

# Graph Styling
plt.title("Spacetime Transition Simulation (Exponent n = 1.86)", fontsize=14)
plt.xlabel("Deformation Progress (x)", fontsize=12)
plt.ylabel("Metric Density (p)", fontsize=12)
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)

# Save the plot for GitHub
plt.savefig('Figure_2.png', dpi=300)
plt.show()
