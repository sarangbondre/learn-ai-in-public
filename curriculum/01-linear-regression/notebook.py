"""
Linear Regression from Scratch (NumPy only)
Phase 1: Foundations — Chapter 1.1
A blindfolded walk down a hill, in 40 lines.
100 students: hours studied -> marks scored. Hidden rule: marks = 8 * hours + 20.
"""
import numpy as np

np.random.seed(42)

# ---------- THE DATA ----------
hours = np.random.uniform(0, 10, 100)                 # FEATURE  (what we know)
marks = 8 * hours + 20 + np.random.normal(0, 4, 100)  # LABEL    (what we predict)
# The +noise is real life: two students who studied 5 hours don't score identically.

# ---------- THE MODEL: two numbers, both starting at zero ----------
w = 0.0   # WEIGHT — how steeply marks rise per extra hour
b = 0.0   # BIAS   — where the line starts when hours = 0

lr = 0.01       # LEARNING RATE — how big each downhill step is
epochs = 2000   # EPOCH — one full pass over all 100 students

def mse(w, b):
    """LOSS: average squared distance between our line and reality."""
    return np.mean((marks - (w * hours + b)) ** 2)

print(f"Before training: w={w:.2f}, b={b:.2f}, loss={mse(w, b):.2f}")

# ---------- THE BLINDFOLDED WALK ----------
for epoch in range(epochs):
    predictions = w * hours + b
    error = predictions - marks
    grad_w = 2 * np.mean(error * hours)   # GRADIENT: which way is uphill for w?
    grad_b = 2 * np.mean(error)           # GRADIENT: which way is uphill for b?
    w -= lr * grad_w                      # step the OPPOSITE way — downhill
    b -= lr * grad_b
    if epoch % 500 == 0:
        print(f"  epoch {epoch:4d}: w={w:.3f}, b={b:.3f}, loss={mse(w, b):.2f}")

print(f"After training : w={w:.3f}, b={b:.3f}, loss={mse(w, b):.2f}")
print(f"Hidden rule was: w=8.000, b=20.000  <- we never told the model this")

# ---------------------------------------------------------------------
# 5-MINUTE TWEAK CHALLENGE
# Change lr from 0.01 to 0.5 and re-run.
# The loss explodes immediately and w, b overflow to `-inf` by epoch 205.
# Steps too big don't descend the hill — they leap clean over the valley
# and land higher up the far slope, every single time. That is DIVERGENCE.
# ---------------------------------------------------------------------
