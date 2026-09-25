# Loss Functions: MSE vs MAE on delivery-time data
# Question: when a few trucks break down, which loss keeps our ETA model honest?
import numpy as np

rng = np.random.default_rng(42) #is a random-number generator started from a fixed "seed" (42). The same seed gives the same "random" data every time, so anyone who runs it gets your exact numbers.
km = rng.uniform(5, 100, 100)                    # feature: delivery distance (km)
minutes = 2 * km + 30 + rng.normal(0, 5, 100)    # hidden rule: 2 min per km + 30 min loading
minutes[:3] += 400                               # 3 breakdowns: huge outliers

# lr (learning rate) sets how big each correction step is.
def train(loss, lr=0.0002, epochs=20000):
    # w (weight) means "minutes per km". The model should find about 2.
    # b (bias) means "fixed minutes per trip". The model should find about 30.
    w, b = 0.0, 0.0
    for _ in range(epochs):
        err = (w * km + b) - minutes             # prediction minus truth
        if loss == "mse":
            g = 2 * err                          # big errors pull HARD (squared)
        else:
            g = np.sign(err)                     # every error pulls the same (absolute)
        w -= lr * np.mean(g * km)
        b -= lr * 50 * np.mean(g)                # bias learns faster (different scale)
    return w, b

for loss in ["mse", "mae"]:
    w, b = train(loss)
    typical = np.median(np.abs((w * km + b) - minutes)[3:])
    print(f"{loss.upper()}: minutes = {w:.2f} * km + {b:.1f}  | typical error on normal trips: {typical:.1f} min")

print("Truth: minutes = 2.00 * km + 30.0")

# 5-minute tweak challenge:
# 1) Change minutes[:3] += 400 to minutes[:10] += 400 (and [3:] to [10:]). Which model breaks?
# 2) Remove the outliers entirely. Do MSE and MAE now agree?
