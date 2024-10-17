import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000
T = 1 / fs
t = np.arange(0, 1 + 0.001, 0.001)
fm = 5
mt = np.sin(2 * np.pi * fm * t)
n = np.arange(0, 1 + T, T)

# Impulse train delta_n
delta_n = np.zeros_like(t)
for i in range(len(n)):
    delta_n[np.abs(t - n[i]) < T/2] = 1

# Sampled signal ms
ms = mt * delta_n

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, mt, linewidth=1.5)
plt.title('Original Signal m(t)')
plt.ylabel('Amplitude')
plt.xlabel('Time')

plt.subplot(3, 1, 2)
(stemlines, stemmarkers, baseline) = plt.stem(t, delta_n, 'r', markerfmt='ro', basefmt=" ")
plt.setp(stemlines, linewidth=1.5)
plt.title('Impulse Train')
plt.ylabel('Amplitude')
plt.xlabel('Time')

plt.subplot(3, 1, 3)
(stemlines, stemmarkers, baseline) = plt.stem(t, ms, 'g', markerfmt='go', basefmt=" ")
plt.setp(stemlines, linewidth=1.5)
plt.title('Sampled Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time')

plt.tight_layout()
plt.show()
