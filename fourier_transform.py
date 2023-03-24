import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# Generate a 2 hertz sine wave that lasts for 5 seconds
x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('time (s)')
ax.set_ylabel('signal amplitude (db)')

# Mixing Audio Signals
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone

# Normalization
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

fig, ax = plt.subplots()
ax.plot(normalized_tone[:1000])
ax.set_xlabel('time (s)')
ax.set_ylabel('signal amplitude (db)')

# Save File
from scipy.io.wavfile import write

# Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)

# Using FFT
from scipy.fft import fft, fftfreq
# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION
yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE) # 1/SAMPLE_RATE = time between samples
fig, ax = plt.subplots()
ax.plot(xf, np.abs(yf))
ax.set_xlabel('frequency (Hz)')
ax.set_ylabel('signal amplitude (db) ?')

# Using RFFT
yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE)
from scipy.fft import rfft, rfftfreq

# Note the extra 'r' at the front
yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

fig, ax = plt.subplots()
ax.plot(xf, np.abs(yf), 'o-')
ax.set_xlabel('frequency (Hz)')
ax.set_ylabel('signal amplitude (db) ?')
