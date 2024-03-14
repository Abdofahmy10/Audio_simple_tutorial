import librosa
import numpy as np
import matplotlib.pyplot as plt


audio_file = 'sample.wav'
signal_array, freq_rate = librosa.load(audio_file, sr=None)

time_audio = len(signal_array) / freq_rate
print(time_audio, "seconds")

# Plot the waveform
plt.figure(figsize=(15, 5))
plt.plot(np.linspace(0, time_audio, num=len(signal_array)), signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, time_audio)
plt.savefig('audio_plot_librosa.png') 
plt.show()

# Plot the spectrogram
plt.figure(figsize=(15, 5))
plt.specgram(signal_array, NFFT=2048, Fs=freq_rate, vmin=-20, vmax=50)
plt.title('Spectrogram')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, time_audio)
plt.colorbar()
plt.savefig('spectrogram_plot_librosa.png') 
plt.show()