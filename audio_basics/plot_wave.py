import wave
import numpy as np
import matplotlib.pyplot as plt

wave_ex = wave.open('sample.wav', 'r')

freq_rate = wave_ex.getframerate()
print(freq_rate)

n_samples = wave_ex.getnframes()
print(n_samples)

time_audio = n_samples/freq_rate
print(time_audio, "seconds")

signal_wave = wave_ex.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print(signal_array.shape)


times = np.linspace(0, n_samples/freq_rate, num=n_samples)
# Plot the waveform
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, time_audio)
plt.savefig('audio_plot.png') 
plt.show()
# Plot the spectrogram
plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=freq_rate, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, time_audio)
plt.colorbar()
plt.savefig('specgram_plot.png') 
plt.show()