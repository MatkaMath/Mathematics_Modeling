#  Creating a signal composed of two sine waves with different frequencies, 
#  computing the FFT of the signal and visualizing the frequency spectrum.
import numpy as np
import matplotlib.pyplot as plt

fs = 1000  # Sampling frequency (samples per second)
t = np.arange(0, 1, 1/fs)  # Time array from 0 to 1 second

f1 = 5   # Frequency of the first sine wave (5 Hz)
f2 = 100  # Frequency of the second sine wave (100 Hz)
signal = 1 * np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(signal), 1/fs)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(fft_freq[:len(fft_freq)//2], np.abs(fft_result)[:len(fft_result)//2])
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
