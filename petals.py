import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

rng = np.random.default_rng(14)
N = 1500

# heart equation: where each petal lands
p = rng.uniform(-1.3, 1.3, (9000, 2))
x, y = p.T
ok = (x*x + y*y - 1)**3 - x*x*y**3 < 0
hx, hy = p[ok][:N].T * 20

# petals start high up in the sky
x0 = rng.uniform(-24, 24, N)
y0 = rng.uniform(52, 90, N)
wait = rng.uniform(0, 6, N)
col = rng.choice(["#ff9f1c", "#ffd23f",
                  "#e85d04", "#ff4d6d"],
                 N, p=[.4, .3, .2, .1])

fig = plt.figure(figsize=(10.8, 19.2))
ax = fig.add_axes([0, 0, 1, 1])
fig.patch.set_facecolor("#0b0614")
ax.set_xlim(-27, 27)
ax.set_ylim(-42, 54)
ax.axis("off")
glow = ax.scatter([], [], s=260, alpha=.1)
dots = ax.scatter([], [], s=75)
txt = ax.text(0, -27, "HAPPY DIWALI",
    ha="center", color="#ffd46b", fontsize=80,
    fontweight="bold")

def frame(i):
    sec = i / 30
    q = np.clip((sec - wait) / 5, 0, 1)
    e = 1 - (1 - q)**3
    sway = np.sin(sec*2 + wait*9)*(1 - e)*3
    beat = 1 + .05*np.sin(sec*5)*(sec > 9)
    x = x0 + (hx*beat - x0)*e + sway
    y = y0 + (hy*beat + 4 - y0)*e
    xy = np.c_[x, y]
    for d in (dots, glow):
        d.set_offsets(xy)
        d.set_color(col)
    txt.set_alpha(np.clip((sec - 10) / 2, 0, 1))

anim = FuncAnimation(fig, frame, frames=510)
anim.save("petals.mp4", fps=30, dpi=100)
